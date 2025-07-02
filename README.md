# SSA Student Updater

Automates updating of student records on government portal. Saves teachers from hours of tedious processing.

## 🚀 Features

- Logs into portal using Playwright
- Automatically updates selected fields based on `baseline.xlsx`
- Handles classes 11 & 12; skips class 9 entirely(ideally has new students already updated from site admin)
- Robust error-handling with logs written back to `students.xlsx`
- Lightweight: processes ≈ 50 sec/student vs 4 min manually

## ⚙️ Prerequisites

- Python 3.10+
- Git
- Internet access to gov portal
- Valid login credentials

## 🧩 Setup

```bash
git clone https://github.com/MihirZalavadia/SSA-Student-Updater.git
cd SSA-Student-Updater
python -m venv .venv
source .venv/bin/activate    # or `.venv\Scripts\activate` on Windows
pip install -r requirements.txt
playwright install
