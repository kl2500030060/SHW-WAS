# utils/validators.py
from utils.exceptions import InvalidInputError

def validate_positive_number(value, field_name):
    """Ensures input is a number and is greater than or equal to zero."""
    try:
        val = float(value)
        if val < 0:
            raise InvalidInputError(f"{field_name} cannot be negative.")
        return val
    except ValueError:
        raise InvalidInputError(f"Invalid input for {field_name}. Must be a valid number.")

def validate_string(value, field_name):
    """Ensures input is not empty."""
    if not value or not str(value).strip():
        raise InvalidInputError(f"{field_name} cannot be empty.")
    return str(value).strip()