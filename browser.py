from playwright.sync_api import Dialog,sync_playwright, TimeoutError as PWTimeout
from config import LOGIN_URL, USER_SEL, PASS_SEL, USER_ID, PASSWORD




def get_page(headless=False):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=headless)
    ctx = browser.new_context()
    page = ctx.new_page()
    return p, browser, page


def smart_login(page, max_wait=120):
    """Navigate, fill creds, then wait for manual captcha + JS alert OR console Enter."""
    page.goto(LOGIN_URL)

    # 1. fill in userid / password
    page.fill(USER_SEL, USER_ID, timeout=10_000)
    page.fill(PASS_SEL, PASSWORD, timeout=10_000)

    print("➡️  Credentials filled. Solve captcha manually…")

    done = False

    # 2. set up one-time dialog handler (alerts / confirms)
    def _on_dialog(dialog: Dialog):
        nonlocal done
        print(f"💬 JS alert: {dialog.message}")
        dialog.accept()
        done = True

    page.once("dialog", _on_dialog)

    try:
        # 3a. wait until `done` flips True (alert appeared) …
        page.wait_for_function("() => window.__playwrightLoginDone === true", timeout=10)
    except PWTimeout:
        pass  # ignore – user might press Enter instead

    if not done:
        # 3b. or user confirms in console
        input("✅  Hit Enter here AFTER captcha is solved and you hit the Login button…")
        done = True

    if not done:
        raise RuntimeError("Login not confirmed – aborting.")
