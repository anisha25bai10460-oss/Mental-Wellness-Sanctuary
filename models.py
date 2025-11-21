# models.py
# Defines the data structures for the application

class User:
    """Represents a user of the application."""
    def __init__(self, user_id, username, password_hash):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash

class MoodEntry:
    """Represents a single daily mood entry."""
    def __init__(self, entry_id, user_id, date, mood, sleep_hours, stress_level, anxiety_level):
        self.id = entry_id
        self.user_id = user_id
        self.date = date  # Format: YYYY-MM-DD
        self.mood = mood          # 1 (Bad) to 5 (Great)
        self.sleep_hours = sleep_hours
        self.stress_level = stress_level  # 1 to 10
        self.anxiety_level = anxiety_level # 1 to 10

    def __str__(self):
        return (f"ID: {self.id} | Date: {self.date} | Mood: {self.mood}/5 | "
                f"Sleep: {self.sleep_hours}h | Stress: {self.stress_level}/10 | "
                f"Anxiety: {self.anxiety_level}/10")