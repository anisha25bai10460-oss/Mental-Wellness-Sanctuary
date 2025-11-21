# main.py
import db_manager
import analytics
import prediction
from datetime import datetime
import sys

# Ensure all dependencies are available
try:
    import bcrypt
    import matplotlib
    import sklearn
except ImportError:
    print("FATAL ERROR: Missing required libraries (bcrypt, matplotlib, scikit-learn).")
    print("Please install them using: pip install bcrypt matplotlib scikit-learn")
    sys.exit(1)


# Global variable to track the currently logged-in user
CURRENT_USER_ID = None
CURRENT_USERNAME = None

def get_valid_input(prompt, data_type=str, min_val=None, max_val=None):
    """Handles common input validation (Error Handling NFR)."""
    while True:
        try:
            value = input(prompt).strip()
            
            if data_type == int:
                value = int(value)
            elif data_type == float:
                value = float(value)

            if min_val is not None and value < min_val:
                print(f"❌ Value must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Value must be at most {max_val}.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter the correct data type.")

# --- Authentication Module ---

def handle_authentication():
    """Handles login and registration before accessing the main system."""
    global CURRENT_USER_ID, CURRENT_USERNAME
    # This ensures the database file is created on first run (Reliability)
    db_manager.create_tables() 

    while CURRENT_USER_ID is None:
        print("\n=== Welcome to Mood Tracker ===")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            username = input("Username: ")
            password = input("Password: ")
            user_id, message = db_manager.login_user(username, password)
            print(message)
            if user_id:
                CURRENT_USER_ID = user_id
                CURRENT_USERNAME = username
        
        elif choice == '2':
            username = input("New Username: ")
            password = input("New Password: ")
            if not password:
                print("Password cannot be empty.")
                continue
            success, message = db_manager.register_user(username, password)
            print(message)
        
        elif choice == '3':
            print("Goodbye!")
            sys.exit(0)
        
        else:
            print("Invalid choice.")

# --- CRUD Module Functions ---

def display_entry_menu():
    """Allows user to create, read, update, or delete entries."""
    while True:
        print("\n=== 1. Log & Manage Entries ===")
        print("1. Log New Entry (C)")
        print("2. View All Entries (R)")
        print("3. Update an Entry (U)")
        print("4. Delete an Entry (D)")
        print("5. Back to Main Menu")
        
        choice = input("Enter choice: ")

        if choice == '1':
            log_new_entry()
        elif choice == '2':
            view_all_entries()
        elif choice == '3':
            update_existing_entry()
        elif choice == '4':
            delete_existing_entry()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def log_new_entry():
    """Handles the creation (C) of a new entry."""
    print("\n--- Log New Entry ---")
    date_str = datetime.now().strftime("%Y-%m-%d") # Default to today's date
    print(f"Logging for today: {date_str}")
    
    # Input Validation (Usability NFR)
    mood = get_valid_input("Mood (1=Bad to 5=Great): ", int, 1, 5)
    sleep = get_valid_input("Sleep (Hours): ", float, 0.0)
    stress = get_valid_input("Stress Level (1=Low to 10=High): ", int, 1, 10)
    anxiety = get_valid_input("Anxiety Level (1=Low to 10=High): ", int, 1, 10)
    
    if db_manager.create_entry(CURRENT_USER_ID, date_str, mood, sleep, stress, anxiety):
        print("✅ Entry saved successfully!")

def view_all_entries():
    """Handles the reading (R) of entries."""
    entries = db_manager.read_all_entries(CURRENT_USER_ID)
    if not entries:
        print("No entries logged yet.")
        return
        
    print("\n--- Your Historical Entries ---")
    # Display entries in a readable table-like format
    print("-----------------------------------------------------------------------------------------------------")
    print(f"{'ID':<4} | {'Date':<10} | {'Mood':<7} | {'Sleep':<7} | {'Stress':<7} | {'Anxiety':<7}")
    print("-----------------------------------------------------------------------------------------------------")
    for entry in entries:
        # Note: The __str__ method in models.py could also format this, but doing it here provides more control
        print(f"{entry.id:<4} | {entry.date:<10} | {entry.mood:<7} | {entry.sleep_hours:<7.1f} | {entry.stress_level:<7} | {entry.anxiety_level:<7}")
    print("-----------------------------------------------------------------------------------------------------")

def update_existing_entry():
    """Handles the update (U) of an entry."""
    view_all_entries()
    if not db_manager.read_all_entries(CURRENT_USER_ID):
        return
        
    entry_id = get_valid_input("Enter the ID of the entry to UPDATE: ", int)
    
    # New validated inputs
    mood = get_valid_input("New Mood (1-5): ", int, 1, 5)
    sleep = get_valid_input("New Sleep (Hours): ", float, 0.0)
    stress = get_valid_input("New Stress Level (1-10): ", int, 1, 10)
    anxiety = get_valid_input("New Anxiety Level (1-10): ", int, 1, 10)
    
    if db_manager.update_entry(entry_id, mood, sleep, stress, anxiety):
         print(f"✅ Entry ID {entry_id} updated successfully!")

def delete_existing_entry():
    """Handles the deletion (D) of an entry."""
    view_all_entries()
    entries = db_manager.read_all_entries(CURRENT_USER_ID)
    if not entries:
        return
        
    entry_id = get_valid_input("Enter the ID of the entry to DELETE: ", int)
    
    if db_manager.delete_entry(entry_id):
        print(f"🗑️ Entry ID {entry_id} deleted successfully!")

# --- Analytics Module Functions ---

def display_analytics_menu():
    """Allows user to view reports, charts, and predictions."""
    while True:
        print("\n=== 2. Analytics & Reporting ===")
        print("1. View Weekly Mood Average [Reporting]")
        print("2. Generate Mood/Sleep Chart [Visualization]")
        print("3. Predict Next Day's Mood [ML Prediction]")
        print("4. Back to Main Menu")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            avg = analytics.calculate_weekly_mood_average(CURRENT_USER_ID)
            print(f"\n📈 Your average mood over the last 7 entries was: **{avg}/5**")
        elif choice == '2':
            analytics.generate_mood_sleep_chart(CURRENT_USER_ID)
        elif choice == '3':
            result = prediction.predict_next_mood(CURRENT_USER_ID)
            print(result)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

# --- Main Application Loop ---

def main_app_loop():
    """The main loop after successful authentication."""
    global CURRENT_USER_ID, CURRENT_USERNAME
    
    while True:
        print(f"\n=== Main Menu (User: {CURRENT_USERNAME}) ===")
        print("1. Log & Manage Entries")
        print("2. Analytics & Reporting")
        print("3. Logout")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            display_entry_menu()
        elif choice == '2':
            display_analytics_menu()
        elif choice == '3':
            CURRENT_USER_ID = None
            CURRENT_USERNAME = None
            print("👋 Logged out successfully.")
            handle_authentication() # Go back to the login screen
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    handle_authentication() # Start the app at the login/register screen
    main_app_loop()