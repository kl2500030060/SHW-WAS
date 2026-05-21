
import csv
import os

VITALS_FILE = "data/vitals_log.csv"
VITALS_HEADERS = [
    "PatientID", "Timestamp", "Systolic", "Diastolic", 
    "HeartRate", "Sugar", "Temp", "Status"
]

def log_vitals(vitals_list):
    """Appends a new vitals record to the CSV log."""
    os.makedirs("data", exist_ok=True)
    file_exists = os.path.isfile(VITALS_FILE)
    
    try:
        with open(VITALS_FILE, mode='a', newline='') as f:
            writer = csv.writer(f)

            if not file_exists:
                writer.writerow(VITALS_HEADERS)
            writer.writerow(vitals_list)
    except IOError as e:
        print(f"CRITICAL ERROR: Failed to append to {VITALS_FILE}. Details: {e}")
