
import os
from models.patient import Patient
from models.vitals import VitalsRecord
from storage.json_store import save_patient
from storage.csv_store import log_vitals
from analysis.vital_trends import detect_vital_anomalies
from analysis.analyzer import generate_health_summary
from visual.charts import generate_bp_chart
from utils.validators import validate_positive_number, validate_string
from utils.exceptions import MedicalRecordError, PatientNotFoundError, CriticalVitalError, InvalidInputError

def clear_screen():
    print("\n" * 2)

def register_patient_ui():
    print("\n--- Register New Patient Profile ---")
    try:
        name = validate_string(input("Full Name: "), "Name")
        age = int(validate_positive_number(input("Age: "), "Age"))
        gender = validate_string(input("Gender (M/F/O): "), "Gender")
        blood_group = validate_string(input("Blood Group: "), "Blood Group")
        height = validate_positive_number(input("Height (cm): "), "Height")
        weight = validate_positive_number(input("Weight (kg): "), "Weight")
        
        patient = Patient(name, age, gender, blood_group, height, weight)
        
    
        conditions = input("Enter any chronic conditions (comma separated, or press Enter to skip): ")
        if conditions:
            for cond in conditions.split(','):
                patient.add_condition(cond)
                
        save_patient(patient.to_dict())
        print(f"\n✅ SUCCESS: Patient registered. ID: {patient.patient_id}")
        print(f"Calculated BMI: {patient.calculate_bmi()}")
        
    except (InvalidInputError, ValueError) as e:
        print(f"\n❌ REGISTRATION FAILED: {e}")

def record_vitals_ui():
    print("\n--- Log Patient Vitals ---")
    pid = input("Enter Patient ID (e.g., PAT-XXXX): ").strip()
    
    try:
        sys = validate_positive_number(input("Systolic BP (Upper): "), "Systolic BP")
        dia = validate_positive_number(input("Diastolic BP (Lower): "), "Diastolic BP")
        hr = validate_positive_number(input("Heart Rate (BPM): "), "Heart Rate")
        sugar = validate_positive_number(input("Blood Sugar (mg/dL): "), "Blood Sugar")
        temp = validate_positive_number(input("Body Temp (F): "), "Temperature")
        
  
        record = VitalsRecord(pid, sys, dia, hr, sugar, temp)
        
        log_vitals(record.to_list())
        print(f"\n✅ VITALS LOGGED. System Evaluation: {record.status}")
        
    except CriticalVitalError as cve:
        print(f"\n🚨🚨 MEDICAL EMERGENCY DETECTED 🚨🚨")
        print(cve)
    except InvalidInputError as e:
        print(f"\n❌ LOGGING FAILED: {e}")

def run_analytics_ui():
    print("\n--- Run Health Intelligence Engine ---")
    pid = input("Enter Patient ID to analyze: ").strip()
    
    try:
        print("\n[ Pandas Summary Report ]")
        summary = generate_health_summary(pid)
        if isinstance(summary, dict):
            for k, v in summary.items():
                print(f" > {k}: {v}")
        else:
            print(summary)

        print("\n[ NumPy Anomaly Detection ]")
        anomalies = detect_vital_anomalies(pid)
        if isinstance(anomalies, dict):
            for k, v in anomalies.items():
                print(f" > {k}: {v}")
        else:
            print(anomalies)

        print("\n[ Matplotlib Visualization ]")
        chart_result = generate_bp_chart(pid)
        print(f" > {chart_result}")

    except PatientNotFoundError as pnf:
        print(f"\n❌ SYSTEM ERROR: {pnf}")
    except Exception as e:
        print(f"\n❌ AN UNEXPECTED ERROR OCCURRED: {e}")

def main():
    while True:
        clear_screen()
        print("==================================================")
        print("  SMART HEALTH & MEDICAL HISTORY TRACKER (SHM-WAS)")
        print("==================================================")
        print("1. Register New Patient Profile")
        print("2. Record Vital Signs")
        print("3. Run Health Analytics & Generate Charts")
        print("4. Exit System")
        print("==================================================")
        
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            register_patient_ui()
        elif choice == '2':
            record_vitals_ui()
        elif choice == '3':
            run_analytics_ui()
        elif choice == '4':
            print("\nShutting down SHM-WAS. Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please select 1, 2, 3, or 4.")
            
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":

    os.makedirs("data", exist_ok=True)
    os.makedirs("exports", exist_ok=True)
    main()
