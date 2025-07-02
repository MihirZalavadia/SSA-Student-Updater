import os
import json, re, pandas as pd
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

# ---------- 1. grab the HTML ------------------------------------------------
with sync_playwright() as p:
    browser  = p.chromium.launch(headless=False)
    context  = browser.new_context()
    page     = context.new_page()
    page.goto("about:blank")  # <-- paste the open form url if you like
    input("🛂  STOP here, log-in, navigate to ANY student-form,   "
          "then press ENTER ↵ in this terminal…")
    try:
        # wait for network to go quiet *and* that key field to exist
        page.wait_for_load_state("networkidle")  # AJAX & images done
        page.wait_for_selector(
            "input[name='ctl00$ContentPlaceHolder1$TxtAdmissionNo']", timeout=60000
        )
    except TimeoutError:
        print("⚠️  form never settled – is the edit page open?")
        context.close();
        browser.close();
        sys.exit(1)
    html = page.content()

# ---------- 2. mine all inputs/selects -------------------------------------
soup   = BeautifulSoup(html, "lxml")
form   = soup.select_one("form")          # outermost <form> tag
fields = []

for tag in form.find_all(["input", "select"]):
    # ignore hidden / submit / button etc.
    if tag.name == "input" and tag.get("type", "text") not in ("text", "number"):
        continue

    id_    = tag.get("id")
    if not id_:
        continue                         # skip nameless controls

    # label text → try <label for="…">  or nearest <label> sibling
    label = ""
    lab   = form.select_one(f"label[for='{id_}']")
    if not lab:                          # fallback: previous element text
        prev = tag.find_previous(string=True)
        label = prev.strip() if prev else id_
    else:
        label = lab.get_text(strip=True)

    kind  = "select" if tag.name == "select" else "text"
    opts  = {o.get("value"): o.text.strip()
             for o in tag.find_all("option")} if kind == "select" else {}

    fields.append(dict(id=id_, label=label, kind=kind, options=opts))

# ---------- 3. write helper artefacts --------------------------------------
with open("all_fields.json", "w", encoding="utf-8") as f:
    json.dump(fields, f, ensure_ascii=False, indent=2)

print(f"📝  {len(fields)} controls → all_fields.json")

# create an empty baseline file if none exists
xlsx = "baseline_values.xlsx"
if not os.path.exists(xlsx):
    cols = ["uid"] + [re.sub(r"[^0-9a-zA-Z]+", "_",
                             f["label"]).lower() for f in fields]
    pd.DataFrame(columns=cols).to_excel(xlsx, index=False)
    print(f"📄  created blank {xlsx} with {len(cols)-1} field columns")
