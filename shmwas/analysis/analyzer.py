# analysis/analyzer.py
import pandas as pd
import os
from storage.csv_store import VITALS_FILE
from utils.exceptions import PatientNotFoundError

def generate_health_summary(patient_id):
    """Uses Pandas for DataFrame manipulation and GroupBy analytics (Week 11)."""
    if not os.path.exists(VITALS_FILE):
        return "No vitals database found."

    df = pd.read_csv(VITALS_FILE)
    patient_df = df[df["PatientID"] == patient_id].copy()

    if patient_df.empty:
        raise PatientNotFoundError(patient_id)

    # Pandas Data Manipulation: Convert strings to actual DateTime objects
    patient_df["Timestamp"] = pd.to_datetime(patient_df["Timestamp"])

    # 1. GroupBy Operation: How often was this patient in 'CRITICAL' vs 'NORMAL' state?
    status_counts = patient_df.groupby("Status").size().to_dict()

    # 2. Filtering & Sorting: Get the absolute most recent reading
    latest_reading = patient_df.sort_values(by="Timestamp", ascending=False).iloc[0]

    return {
        "Status History Breakdown": status_counts,
        "Most Recent Blood Sugar": latest_reading["Sugar"],
        "Most Recent Temperature": latest_reading["Temp"],
        "Last Recorded Time": latest_reading["Timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    }