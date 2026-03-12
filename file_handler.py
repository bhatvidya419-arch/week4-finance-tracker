import json
import os
import shutil

DATA_FILE = 'expenses.json'
BACKUP_FILE = 'expenses_backup.json'

def save_expenses(expenses):
    """Saves a list of Expense objects to a JSON file with an automatic backup."""
    try:
        # Step 3: Create a backup before overwriting the main file
        if os.path.exists(DATA_FILE):
            shutil.copy(DATA_FILE, BACKUP_FILE)
            
        with open(DATA_FILE, 'w') as f:
            json.dump([e.to_dict() for e in expenses], f, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def load_expenses():
    """Loads expense data from the JSON file or recovery backup."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("Main data file corrupted. Attempting to load from backup...")
        # Basic recovery logic
        if os.path.exists(BACKUP_FILE):
            with open(BACKUP_FILE, 'r') as f:
                return json.load(f)
        return []
