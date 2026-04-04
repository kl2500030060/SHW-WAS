# models/record.py
from utils.date_utils import get_current_timestamp

class ClinicalRecord:
    """Base class for all medical records demonstrating Inheritance."""
    
    def __init__(self, patient_id):
        # Protected attribute demonstrating Encapsulation
        self._patient_id = patient_id  
        self.timestamp = get_current_timestamp()

    def get_summary(self):
        """Base method to be overridden by subclasses (Polymorphism)."""
        raise NotImplementedError("Subclasses must implement this method.")

    def to_dict(self):
        return {
            "patient_id": self._patient_id,
            "timestamp": self.timestamp
        }