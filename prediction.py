# prediction.py
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import db_manager
import warnings

# Suppress warnings for cleaner CLI output
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)

def prepare_prediction_data(user_id):
    """Fetches historical data and formats it for the ML model."""
    entries = db_manager.read_all_entries(user_id)
    
    if len(entries) < 15: # Requirement for minimum data points
        return None, None, False
        
    entries.reverse() # Sort chronologically (oldest first)
    
    X = [] # Features: sleep, stress, anxiety on Day N
    Y = [] # Target: Mood on Day N+1
    
    for i in range(len(entries) - 1):
        # Features from entry at index i: [sleep_hours, stress_level, anxiety_level]
        current_features = [entries[i].sleep_hours, entries[i].stress_level, entries[i].anxiety_level]
        X.append(current_features)
        
        # Target is the mood from the next entry (index i+1)
        next_day_mood = entries[i+1].mood
        Y.append(next_day_mood)
        
    return np.array(X), np.array(Y), True

def predict_next_mood(user_id):
    """Trains a Linear Regression model and predicts the next day's mood (Prediction)."""
    X, Y, success = prepare_prediction_data(user_id)
    
    if not success:
        return "\n⚠️ Cannot run prediction. Need at least 15 historical entries to train the model."

    # Use a small test size (20%) 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
    
    # Initialize and Train the Model
    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    # Get the latest entry's features for the actual prediction
    latest_entry = db_manager.read_all_entries(user_id)[0] 
    latest_features = np.array([[latest_entry.sleep_hours, latest_entry.stress_level, latest_entry.anxiety_level]])
    
    # Make the prediction
    predicted_mood = model.predict(latest_features)[0]
    
    # Clamp the prediction to the 1-5 mood scale
    clamped_mood = max(1.0, min(5.0, predicted_mood))
    
    # Get the model's performance score on the test data (R² Score)
    score = model.score(X_test, Y_test)
    
    return (f"Based on your latest entry ({latest_entry.date}): \n"
            f"  - Sleep: {latest_entry.sleep_hours:.1f}h, Stress: {latest_entry.stress_level}, Anxiety: {latest_entry.anxiety_level}\n"
            f"🔮 Predicted Mood for Tomorrow (1-5 Scale): **{clamped_mood:.2f}**\n"
            f"(Model R² Score on Test Data: {score:.2f})")