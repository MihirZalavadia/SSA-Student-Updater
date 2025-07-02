# main.py
import argparse
import pandas as pd
from browser  import get_page, smart_login
from scraper  import scrape_students, save_students
from editor   import process_first_pending
from navigator import go_to_manage_students, open_std

def parse_cli():
    p = argparse.ArgumentParser(description="SSA Gujarat student updater")
    p.add_argument("--headless", action="store_true", help="run Chrome headless")
    p.add_argument("--scrape-only", action="store_true",
                   help="just capture Excel sheets, no editing")
    return p.parse_args()

def main():
    args = parse_cli()
    p, browser, page = get_page(headless=args.headless)

    try:
        smart_login(page)
        go_to_manage_students(page)

        for std in (9, 10, 11, 12):
            if std in (9,10,11):  # <<< NEW
                continue  # – nothing to scrape / edit
            print(f"➡️  Std-{std}")
            open_std(page, std)

            df = pd.DataFrame(scrape_students(page))       # ← grab full table
            save_students(df, std)                         # write/update sheet
            print(f"   ✔  {len(df)} rows saved to sheet Std{std}")

            if not args.scrape_only:
                process_first_pending(page, std)           # <-- run *only* if allowed

            page.go_back()                                 # go back to grid

        print("✅  Done – workbook built at students.xlsx")
    finally:
        browser.close(); p.stop()


if __name__ == "__main__":
    main()
