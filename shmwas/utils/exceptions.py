

class MedicalRecordError(Exception):
    """Base exception class for SHM-WAS."""
    pass

class PatientNotFoundError(MedicalRecordError):
    """Raised when a requested patient ID does not exist in the system."""
    def __init__(self, patient_id):
        super().__init__(f"Error: Patient ID '{patient_id}' not found in database.")

class CriticalVitalError(MedicalRecordError):
    """Raised when recorded vitals are dangerously outside human limits."""
    def __init__(self, metric, value):
        super().__init__(f"URGENT: {metric} value of {value} is in the critical danger zone! Seek immediate medical attention.")

class InvalidInputError(MedicalRecordError):
    """Raised when user input fails validation."""
    pass
