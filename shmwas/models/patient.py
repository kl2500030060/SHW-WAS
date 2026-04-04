# models/patient.py
from utils.id_generator import generate_id

class Patient:
    def __init__(self, name, age, gender, blood_group, height, weight):
        self.patient_id = generate_id("PAT")
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_group = blood_group
        self.height = height  # in cm
        self.weight = weight  # in kg
        
        # Using Sets to ensure unique entries (Week 5)
        self.chronic_conditions = set()
        self.allergies = set()

    def add_condition(self, condition):
        self.chronic_conditions.add(condition.strip().title())

    def add_allergy(self, allergy):
        self.allergies.add(allergy.strip().title())

    def calculate_bmi(self):
        height_m = self.height / 100
        return round(self.weight / (height_m ** 2), 2)

    def to_dict(self):
        # Convert sets to lists for JSON serialization later
        data = self.__dict__.copy()
        data['chronic_conditions'] = list(self.chronic_conditions)
        data['allergies'] = list(self.allergies)
        return data