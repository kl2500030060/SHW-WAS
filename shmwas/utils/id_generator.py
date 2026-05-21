
import uuid

def generate_id(prefix="ID"):
    """
    Generates a unique 8-character ID.
    Example output: PAT-A1B2C3D4
    """
    return f"{prefix}-{str(uuid.uuid4())[:8].upper()}"
