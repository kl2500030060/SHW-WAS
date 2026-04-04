# visual/charts.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from storage.csv_store import VITALS_FILE

def generate_bp_chart(patient_id):
    """Generates and saves a Matplotlib chart of Blood Pressure trends (Week 12)."""
    if not os.path.exists(VITALS_FILE):
        return "Error: No vitals data exists to chart."

    df = pd.read_csv(VITALS_FILE)
    patient_df = df[df["PatientID"] == patient_id].copy()

    if patient_df.empty:
        return f"Error: No vitals recorded for patient {patient_id}."

    # Convert to datetime and sort so the line chart flows correctly
    patient_df["Timestamp"] = pd.to_datetime(patient_df["Timestamp"])
    patient_df = patient_df.sort_values("Timestamp")

    # Matplotlib Configuration
    plt.figure(figsize=(10, 6))
    
    # Plotting both Systolic and Diastolic lines
    plt.plot(patient_df["Timestamp"], patient_df["Systolic"], 
             marker='o', linestyle='-', color='red', label='Systolic (Upper)')
    plt.plot(patient_df["Timestamp"], patient_df["Diastolic"], 
             marker='o', linestyle='-', color='blue', label='Diastolic (Lower)')

    # Adding threshold lines for visual reference
    plt.axhline(y=140, color='red', linestyle=':', alpha=0.5, label='High BP Threshold')
    plt.axhline(y=90, color='blue', linestyle=':', alpha=0.5)

    plt.title(f"Blood Pressure Trend Analysis: {patient_id}")
    plt.xlabel("Date & Time")
    plt.ylabel("Blood Pressure (mmHg)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Save the file
    os.makedirs("exports", exist_ok=True)
    file_path = f"exports/{patient_id}_BP_Chart.png"
    plt.savefig(file_path)
    plt.close() # Close memory buffer
    
    return f"Success! Chart exported to: {file_path}"