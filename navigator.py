# src/navigator.py
from playwright.sync_api import TimeoutError
from config import MANAGE_STUDENTS_SEL, STD_ICON_IDS


LENGTH_DROPDOWN = 'select[name="ctl00_ContentPlaceHolder1_GvReport_length"]'
def _select_show_all(page):
    """Choose 'All' in the length dropdown (value=-1) if present."""
    try:
        page.wait_for_selector(LENGTH_DROPDOWN, timeout=5_000)
        page.select_option(LENGTH_DROPDOWN, "-1")
        page.wait_for_load_state("networkidle")  # rows reload via Ajax
    except TimeoutError:
        print("⚠️  Length dropdown not found – skipping.")

def go_to_manage_students(page):
    page.wait_for_selector(MANAGE_STUDENTS_SEL, timeout=10_000)
    page.click(MANAGE_STUDENTS_SEL)
    page.wait_for_selector(next(iter(STD_ICON_IDS.values())), timeout=10_000)

def open_std(page, std: int):
    """Click Std icon, then set table length to All."""
    sel = STD_ICON_IDS[std]
    page.click(sel)
    page.wait_for_load_state("networkidle")
    _select_show_all(page)