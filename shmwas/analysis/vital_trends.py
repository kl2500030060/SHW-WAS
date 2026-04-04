# analysis/vital_trends.py
import numpy as np
import pandas as pd
import os
from storage.csv_store import VITALS_FILE

def detect_vital_anomalies(patient_id):
    """Uses NumPy for vectorized statistical anomaly detection (Week 10)."""
    if not os.path.exists(VITALS_FILE):
        return "No vitals database found."

    df = pd.read_csv(VITALS_FILE)
    patient_data = df[df["PatientID"] == patient_id]

    if patient_data.empty:
        return "No vitals recorded for this patient yet."

    # Convert Pandas Series to NumPy arrays for fast vectorized operations
    systolic_arr = patient_data["Systolic"].to_numpy()
    heart_rate_arr = patient_data["HeartRate"].to_numpy()

    # NumPy Statistical Analysis
    sys_mean = np.mean(systolic_arr)
    sys_std = np.std(systolic_arr)
    
    hr_mean = np.mean(heart_rate_arr)
    hr_std = np.std(heart_rate_arr)

    # Vectorized condition: Flag anomalies that are > 1 standard deviation above mean
    # Adding a tiny epsilon (0.01) prevents issues if standard deviation is 0
    sys_spikes = np.sum(systolic_arr > (sys_mean + sys_std + 0.01))
    hr_spikes = np.sum(heart_rate_arr > (hr_mean + hr_std + 0.01))

    return {
        "Total Readings Analysed": len(systolic_arr),
        "Average Systolic BP": round(sys_mean, 2),
        "Systolic Spikes Detected": int(sys_spikes),
        "Average Heart Rate": round(hr_mean, 2),
        "Heart Rate Spikes Detected": int(hr_spikes)
    }