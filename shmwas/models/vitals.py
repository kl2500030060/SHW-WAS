
from models.record import ClinicalRecord
from utils.exceptions import CriticalVitalError

class VitalsRecord(ClinicalRecord):
    """Demonstrates Inheritance from ClinicalRecord."""
    
    def __init__(self, patient_id, systolic, diastolic, heart_rate, sugar, temp):
        super().__init__(patient_id)
        self.systolic = systolic
        self.diastolic = diastolic
        self.heart_rate = heart_rate
        self.sugar = sugar
        self.temperature = temp
        self.status = self._evaluate_vitals()

    def _evaluate_vitals(self):
        """Encapsulated internal logic for health checks."""
      
        if self.systolic > 200 or self.diastolic > 120:
            raise CriticalVitalError("Blood Pressure", f"{self.systolic}/{self.diastolic}")
        
        if self.systolic > 140 or self.diastolic > 90:
            return "CRITICAL: High BP"
        if self.sugar > 180:
            return "ALERT: High Blood Sugar"
        if self.heart_rate < 60 or self.heart_rate > 100:
            return "ALERT: Abnormal Heart Rate"
        return "NORMAL"

    def get_summary(self):
        """Demonstrates Polymorphism (Overriding base class method)."""
        return f"Vitals for {self._patient_id}: BP {self.systolic}/{self.diastolic}, Status: {self.status}"

    def to_list(self):
     
        return [self._patient_id, self.timestamp, self.systolic, self.diastolic, 
                self.heart_rate, self.sugar, self.temperature, self.status]
