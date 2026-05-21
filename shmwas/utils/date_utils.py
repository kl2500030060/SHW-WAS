
from datetime import datetime

def get_current_timestamp():
    """Returns the current date and time as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_date():
    """Returns only the current date as a string."""
    return datetime.now().strftime("%Y-%m-%d")
