import uuid
from datetime import datetime

def generate_workflow_id():
    """Generate a unique workflow identifier."""
    return f"workflow_{uuid.uuid4().hex[:8]}_{datetime.now().strftime('%Y%m%d%H%M%S')}"

def log(message, level="INFO"):
    """Structured console logger with timestamp and level."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{level}] {timestamp} — {message}")
