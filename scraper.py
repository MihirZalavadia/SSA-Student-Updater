import pandas as pd
from config import TABLE_SEL, STUDENTS_XLSX
from excel_utils import write_sheet

def _row_bg(row):
    style = row.get_attribute('style') or ''
    if 'LightGreen' in style: return 'green'
    if 'IndianRed'  in style: return 'red'
    return 'white'

def scrape_students(page):
    page.wait_for_selector(TABLE_SEL)
    trs = page.query_selector_all(f'{TABLE_SEL} > tbody > tr')
    data = []
    for r in trs:
        cols = [c.inner_text().strip() for c in r.query_selector_all('td')]
        data.append({'uid': cols[0], 'name': cols[1], 'bg': _row_bg(r), 'comment': "" })
    return data

def save_students(df, std):
    write_sheet(df, f"Std{std}")
