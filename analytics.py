# analytics.py
import db_manager
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def calculate_weekly_mood_average(user_id):
    """Calculates the average mood for the last 7 entries (Reporting)."""
    entries = db_manager.read_all_entries(user_id)
    
    if not entries:
        return 0.0
        
    recent_entries = entries[:7] 
    
    total_mood = sum(e.mood for e in recent_entries)
    average = total_mood / len(recent_entries)
    
    return round(average, 2)

def generate_mood_sleep_chart(user_id):
    """Generates a visualization of mood vs sleep (Visualization)."""
    entries = db_manager.read_all_entries(user_id)
    
    if len(entries) < 2:
        print("Not enough data (need at least 2 entries) for visualization.")
        return False

    recent_entries = entries[:30] # Limit to 30 days
    
    # Extracting and reversing data to show chronologically (oldest date first)
    dates = [e.date for e in recent_entries][::-1]
    moods = [e.mood for e in recent_entries][::-1]
    sleeps = [e.sleep_hours for e in recent_entries][::-1]

    plt.style.use('seaborn-v0_8-deep') # Using a modern, clean style
    fig, ax1 = plt.subplots(figsize=(10, 5))
    
    # Plot Mood (Primary Axis)
    ax1.plot(dates, moods, label='Mood (1-5)', marker='o', color='#0ea5e9') # Sky Blue
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Mood Score (1-5)", color='#0ea5e9')
    ax1.tick_params(axis='y', labelcolor='#0ea5e9')
    ax1.tick_params(axis='x', rotation=45)
    ax1.set_ylim(0.5, 5.5) 

    # Plot Sleep (Secondary Axis)
    ax2 = ax1.twinx()
    ax2.plot(dates, sleeps, label='Sleep (Hours)', marker='x', color='#10b981', linestyle='--') # Teal Green
    ax2.set_ylabel("Sleep Hours", color='#10b981')
    ax2.tick_params(axis='y', labelcolor='#10b981')
    ax2.set_ylim(0, 12) 

    plt.title("30-Day Trend: Mood & Sleep Correlation")
    fig.tight_layout()
    plt.show()
    
    return True