![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Playwright](https://img.shields.io/badge/Playwright-Automation-brightgreen)
![Status](https://img.shields.io/badge/Status-Production--ready-green)

# SSA Gujarat Student Updater

## 🤯 Why This Project Exists
Manually approving SSA student records is slow, repetitive, and time-consuming. This script automates the entire flow using Playwright—boosting speed and reducing human effort drastically.
A user-friendly Python automation script using Playwright that fills up student details on the SSA Gujarat web portal. Built to reduce teacher workload by automatically populating fields based on pre-prepared Excel sheets.

## 🎥 Demo
![SSA Demo](SSMGujarat.gif)

---

## 🔐 Security & Setup

Before proceeding, make sure to follow this securely and carefully:

### 1. Clone this repo:
```bash
git clone https://github.com/MihirZalavadia/SSA-Student-Updater.git
cd SSA-Student-Updater
```

### 2. Python Environment Setup (First-Time Only)
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
playwright install  # install browser drivers
```

### 3. Create a `.env` file in project root:
```ini
SSA_USER_ID=your-school-id-here
SSA_PASSWORD=your-secure-password-here
```
👉 Your credentials are only stored locally in `.env`, not shared.

### 4. Prepare Excel Files
- `baseline.xlsx` – contains desired field values for each student UID
- `students.xlsx` – original export from SSA site

Use the format from provided examples. Each student row should have at least:
- UID
- All field values to be updated (as per `config.py`)

### 5. Run the Script
```bash
python main.py
```

- The script will open the SSA portal
- You must solve the CAPTCHA manually
- It will update all students *except Std-9* (explained below)

---

## 💡 Why Std-9 Is Skipped
In SSA Gujarat, Std-9 students are treated as fresh entries. All their records are pre-filled and green-marked.
So, no update needed – we safely skip them.

---

## 📚 Requirements
```
pandas
openpyxl
python-dotenv
playwright
```
Use the included `requirements.txt` or run:
```bash
pip install -r requirements.txt
```

---

## 🧑‍🏫 Walkthrough for Non-Tech Users

1. **Download & Install Python 3.10+**: https://www.python.org/downloads/

2. **Open the Folder** in File Explorer:
   - Hold **Shift** + right click → choose **"Open PowerShell window here"**

3. **Setup Environment**:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

4. **Create a `.env` File**:
   - Open Notepad → paste:
```ini
SSA_USER_ID=your-id-here
SSA_PASSWORD=your-password-here
```
   - Save it as `.env` in the same folder

5. **Edit Excel Files**:
   - Use `baseline.xlsx` to set updated values
   - Use `students.xlsx` to keep UID and current comments

6. **Run It**:
```powershell
python main.py
```
   - A browser will open. Enter CAPTCHA and hit **Login** manually.
   - The bot does the rest!

---

## 📣 Contributions

If you’re a dev or a teacher who faced this issue and have ideas or suggestions, feel free to open Issues or PRs. Together, we can save many teachers from eye strain and frustration.

---

## 👏 Built With Love for My Mami
This tool was born when we saw how painful it is to update 350+ students manually. In one evening, we built it, tested it, and proudly saved hours of tedious form filling.

💻 Automation should serve the people who serve others.

---

## License
MIT – Use it freely, tweak it respectfully, and help others.

<!-- Tags: Gujarat SSA Automation, Playwright Python, School Admin Script, Student Record Bulk Approval -->

