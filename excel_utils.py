from pathlib import Path
import pandas as pd

STUDENTS_XLSX = Path("students.xlsx")

def write_sheet(df, sheet_name, excel_path: Path = STUDENTS_XLSX):
    """
    Write/overwrite *sheet_name* inside students.xlsx
    """
    if not excel_path.exists():
        # first-time write → just create the file
        df.to_excel(excel_path, sheet_name, index=False)
        return

    # append & REPLACE if the sheet is already there
    with pd.ExcelWriter(
        excel_path,
        mode="a",                 # append to existing workbook
        engine="openpyxl",
        if_sheet_exists="replace" # <-- key line
    ) as writer:
        df.to_excel(writer, sheet_name, index=False)