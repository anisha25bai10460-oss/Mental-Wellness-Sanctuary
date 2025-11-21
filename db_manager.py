# db_manager.py
import sqlite3
import bcrypt
from datetime import datetime
# Ensure models.py is clean and this import works:
from models import User, MoodEntry 

DATABASE_NAME = 'mood_tracker.db'

def get_db_connection():
    """Returns a connection object to the database."""
    return sqlite3.connect(DATABASE_NAME)

def create_tables():
    """Initializes the database and creates the necessary tables."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. User Management Table (Security)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    # 2. Mood Log Table (Data Persistence)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            date TEXT UNIQUE NOT NULL,
            mood INTEGER NOT NULL,
            sleep_hours REAL,
            stress_level INTEGER,
            anxiety_level INTEGER,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    """)
    conn.commit()
    conn.close()

# --- User Management (Security) ---

def register_user(username, password):
    """Registers a new user, hashing the password."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Hash the password (Security NFR)
    password_bytes = password.encode('utf-8')
    # bcrypt.gensalt() generates the necessary salt for security
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')
    
    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed))
        conn.commit()
        return True, "User registered successfully!"
    except sqlite3.IntegrityError:
        return False, "Error: Username already exists."
    finally:
        conn.close()

def login_user(username, password):
    """Authenticates a user."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        user_id, password_hash = result
        # Check password against hash
        if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
            return user_id, f"Welcome back, {username}!"
    
    return None, "Invalid username or password."

# --- CRUD Operations for Entries ---

def create_entry(user_id, date, mood, sleep, stress, anxiety):
    """C: Creates a new mood entry."""
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO entries (user_id, date, mood, sleep_hours, stress_level, anxiety_level)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, date, mood, sleep, stress, anxiety))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("\n❌ Error: An entry for this date already exists. Use the Update function to modify.")
        return False
    finally:
        conn.close()

def read_all_entries(user_id):
    """R: Reads all entries for the user, ordered by date descending."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries WHERE user_id = ? ORDER BY date DESC", (user_id,))
    entries_data = cursor.fetchall()
    conn.close()
    # Convert tuple data to MoodEntry objects
    return [MoodEntry(*data) for data in entries_data]

def update_entry(entry_id, mood, sleep, stress, anxiety):
    """U: Updates an existing entry's details."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE entries 
        SET mood = ?, sleep_hours = ?, stress_level = ?, anxiety_level = ?
        WHERE id = ?
    """, (mood, sleep, stress, anxiety, entry_id))
    conn.commit()
    conn.close()
    return True

def delete_entry(entry_id):
    """D: Deletes an entry."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    return True