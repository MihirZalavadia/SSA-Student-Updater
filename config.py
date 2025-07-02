# login page bits
LOGIN_URL   = "https://www.ssgujarat.org/CTELogin.aspx"
USER_SEL    = '//*[@id="TxtUName"]'
PASS_SEL    = '//*[@id="TxtUPass"]'

# pull creds from environment so you never hard-code
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()                     # ← pulls keys from .env into os.environ

USER_ID  = os.getenv("SSG_USER")
PASSWORD = os.getenv("SSG_PASS")
if not USER_ID or not PASSWORD:
    raise RuntimeError("Missing SSG_USER / SSG_PASS in environment or .env file.")


DATE_DEFAULTS = {
    11: "13062024",   # Std-11
    12: "13062024",   # Std-12
}
# ─── config.py ──────────────────────────────────────────────────────────────
TARGET_FIELDS = {
    # ---------- ADDRESS / HABITATION ----------
    "Habitation": {
        "id": "ctl00_ContentPlaceHolder1_ddlHabitation",
        "kind": "select",
        "value": "2"                 # “2-Urban”
    },

    # ---------- DATES & NUMBERS ----------

    "AdmissionDate": {
        "id": "ctl00_ContentPlaceHolder1_TxtDateOfAddmission",
        "kind": "text",
    },

    "PrevYearAttendance": {
        "id": "ctl00_ContentPlaceHolder1_TxtPrevYearAtt",
        "kind": "text",
        "value": "250"
    },

    # ---------- EXAM / RESULT ----------
    "LastExamAppeared": {
        "id": "ctl00_ContentPlaceHolder1_ddlLastExamAppeared",
        "kind": "select",
        "value": "1"                 # “1 – Yes”
    },
    "LastExamResult": {
        "id": "ctl00_ContentPlaceHolder1_ddlResultOfLastExamination",
        "kind": "select",
        "value": "1"                 # “Promoted / Passed”
    },
    "MarksObtainedPct": {
        "id": "ctl00_ContentPlaceHolder1_txtmarksobtained",
        "kind": "text",
        "value": "75"
    },

    # ---------- LEARNING-DISABILITY CHECKS ----------
    "SLD_Check": {
        "id": "ctl00_ContentPlaceHolder1_ddlCheckup_Specific_Learning_Disability",
        "kind": "select",
        "value": "2"                 # “2-ના / No”
    },
    "ASD_Check": {
        "id": "ctl00_ContentPlaceHolder1_ddlCheckup_Autism_Spectrum_Disorder",
        "kind": "select",
        "value": "2"
    },
    "ADHD_Check": {
        "id": "ctl00_ContentPlaceHolder1_ddlCheckup_Attention_Deficit_Hyperactive_Disorder",
        "kind": "select",
        "value": "2"
    },

    # ---------- INCENTIVES / FACILITIES ----------
    "IncentivesProvided": {
        "id": "ctl00_ContentPlaceHolder1_ddlIncentive_Benefits_Facilities_Provided_Child",
        "kind": "select",
        "value": "1"
    },
    "FreeTextBookSet": {
        "id": "ctl00_ContentPlaceHolder1_TxtSetofFreeTextbox",
        "kind": "select",
        "value": "1"
    },
    "UniformPairs": {
        "id": "ctl00_ContentPlaceHolder1_TxtSchoolUniform",
        "kind": "select",
        "value": "2"                 # “2 – 2 pairs”
    },
    "FreeTransport": {
        "id": "ctl00_ContentPlaceHolder1_TxtFreeTransportFacility",
        "kind": "select",
        "value": "2"
    },
    "FreeEscort": {
        "id": "ctl00_ContentPlaceHolder1_TxtFreeEscortFacility",
        "kind": "select",
        "value": "2"
    },
    "MidDayMeal": {
        "id": "ctl00_ContentPlaceHolder1_ddlmiddaymeal",
        "kind": "select",
        "value": "2"
    },
    "FreeHostel": {
        "id": "ctl00_ContentPlaceHolder1_TxtFreeHostel",
        "kind": "select",
        "value": "0"                 # “Not applicable”
    },
	"FreeBicycle": {
		"id":"ctl00_ContentPlaceHolder1_ddlfreeBicycle",
		"kind":"select",
		"value":"2"
	},
    "FreeGadget": {
        "id": "ctl00_ContentPlaceHolder1_ddlFree_Mobile_Tablet_Computer",
        "kind": "select",
        "value": "2"
    },

    # ---------- SCHOLARSHIP ----------
    "ScholarshipReceived": {
        "id": "ctl00_ContentPlaceHolder1_ddlScholarship_Received_Previous_Academic_Year",
        "kind": "select",
        "value": "1"
    },
    "CentralScholarship": {
        "id": "ctl00_ContentPlaceHolder1_ddlCentral_Scholarship",
        "kind": "select",
        "value": "2"
    },
    "StateScholarship": {
        "id": "ctl00_ContentPlaceHolder1_ddlState_Scholarship",
        "kind": "select",
        "value": "1"
    },
    "OtherScholarship": {
        "id": "ctl00_ContentPlaceHolder1_ddlOther_Scholarship",
        "kind": "select",
        "value": "2"
    },
    "ScholarshipAmount": {
        "id": "ctl00_ContentPlaceHolder1_txt_Scholarship_Amount",
        "kind": "text",
        "value": "10000"
    },

    # ---------- ACTIVITIES ----------
    "Extracurricular": {
        "id": "ctl00_ContentPlaceHolder1_ddlInvolved_Extracurricular_Activity",
        "kind": "select",
        "value": "2"
    },
    "GiftedChild": {
        "id": "ctl00_ContentPlaceHolder1_ddlIdentified_Gifted_Talented_Child",
        "kind": "select",
        "value": "2"
    },
    "NCC_NSS": {
        "id": "ctl00_ContentPlaceHolder1_ddlParticipate_NCC_NSS_Scouts_Guides",
        "kind": "select",
        "value": "2"
    },

    # ---------- HEALTH TABLETS ----------
    "IronFolic": {
        "id": "ctl00_ContentPlaceHolder1_ddlIronFolicAcid",
        "kind": "select",
        "value": "1"
    },
    "Deworming": {
        "id": "ctl00_ContentPlaceHolder1_ddlDewormingTablets",
        "kind": "select",
        "value": "1"
    },
    "VitaminA": {
        "id": "ctl00_ContentPlaceHolder1_ddlVitaminATables",
        "kind": "select",
        "value": "1"
    },

    # ---------- CONTACT ----------
    "Email": {
        "id": "ctl00_ContentPlaceHolder1_txtEmailID",
        "kind": "text",
        "value": "SNGHRAJKOT@GMAIL.COM"
    },

    # ---------- CURRENT YEAR STATUS ----------
    "NewYrStatus": {
        "id": "ctl00_ContentPlaceHolder1_ddlNewYrStatus",
        "kind": "select",
        "value": "1"                 # “1 – આ શાળામાં જ”
    },
    "Stream":{         # only for 11 & 12
        "id": "ctl00_ContentPlaceHolder1_ddlStream",
        "kind": "select",
        "value": "3"
    }
}

# side-menu “Manage Students” link
MANAGE_STUDENTS_SEL = '#ctl00_ManageStudent'                  # ← CSS is simplest

# mapping of class-icons we’ll click after the Manage-page loads
STD_ICON_IDS = {
    9:  "#ctl00_ContentPlaceHolder1_gridstdwise_ctl02_Std9",
    10: "#ctl00_ContentPlaceHolder1_gridstdwise_ctl02_Std10",
    11: "#ctl00_ContentPlaceHolder1_gridstdwise_ctl02_Std11",
    12: "#ctl00_ContentPlaceHolder1_gridstdwise_ctl02_Std12",
}


BASE_DIR = Path(__file__).parent
TABLE_SEL = '#ctl00_ContentPlaceHolder1_GvReport'
PLUS_OFFSET = 12           # px from left inside UID cell
UPDATE_BTN      = "#ctl00_ContentPlaceHolder1_BtnSubmit"
EDIT_ICON_SEL   = 'input[title*="Edit"][type="image"]'
STUDENTS_XLSX   = "students.xlsx"
BASELINE_XLSX   = "baseline_values.xlsx"