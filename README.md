Mental Wellness Sanctuary


OVERVIEW

  The Mental Wellness Sanctuary is a complete, full-stack web application designed to help users track and analyze their personal mental health metrics, including mood, sleep, stress, and anxiety levels. The project is organized into three robust modules: Logging (CRUD operations) for data capture, Reporting for real-time calculation of weekly averages, and Insights for data visualization and predictive modeling concepts . Built using a clean, calming interface with HTML/Tailwind CSS and JavaScript, the application achieves high Reliability and Security by utilizing Google Firestore for real-time, user-isolated data persistence, resolving complex asynchronous data handling issues. This sanctuary serves as a strong portfolio piece demonstrating technical proficiency in cloud integration, data manipulation, and defensive programming practices.


FEATURES

  The Mental Wellness Sanctuary is your personal, real-time reflection tool, designed to help you discover hidden patterns in your well-being.
  Effortless Logging (CRUD): You can quickly log and manage five crucial metrics—Mood, Sleep, Stress, and Anxiety—with full control to easily edit or delete past entries.
  Real-time Insights: The app instantly calculates your Weekly Mood and Sleep Averages, offering an immediate health status report.
  Visual Discovery: An interactive chart overlays your metrics (like Mood vs. Sleep), making it easy to visualize correlations and understand what truly impacts your day.
  The Predictive Nudge: The Prediction Feature uses your historical data to forecast your likely mood for tomorrow, giving you a gentle, data-driven nudge to prioritize self-care today.
  Unbreakable Trust: All your private data is securely saved in the cloud (Firestore) and is protected by robust Error Handling, ensuring the application is always reliable and your          information is totally private.




TECHNOLOGIES / TOOLS USED

  I. Web Application (Functional Frontend & Cloud Backend)
    
    HTML5, JavaScript (ES6+): The core languages providing the structure and client-side logic for the functional web interface.
    
    Tailwind CSS (CDN): Used for all responsive styling and design, providing the custom calm, thematic aesthetic.
    
    Google Firestore: The NoSQL cloud database used for real-time data persistence (CRUD) and synchronization.
    
    Firebase Authentication SDK: Manages user identification and session security, ensuring data is isolated per user ID.
    
    Chart.js (CDN): Specialized JavaScript library used to dynamically generate the Mood vs. Sleep trend chart , which drives the visualization component.
    
    JavaScript Heuristics: Provides the simple, weighted calculations for the "Prediction Feature," demonstrating the logic required for an ML component.

  II. Python CLI Application (Initial Design & Advanced Logic)
  
    Python 3: The core language used for the initial modular design and the advanced logic (analytics, ML).
    
    Scikit-learn (ML): Library used for the conceptual Linear Regression model to predict next-day mood (found in prediction.py).
    
    NumPy: Used alongside Scikit-learn for high-performance numerical array operations in the prediction model.
    
    Matplotlib: Library used to generate the static trend charts in the Python CLI version (found in analytics.py).
    
    bcrypt: Library used for secure password hashing in the Python CLI authentication module (db_manager.py).
    
    SQLite3: The Python standard library used for file-based database persistence in the initial CLI application (db_manager.py).
    
    getpass: Used in main.py to securely hide password input in the console application.


STEPS TO INSTALL AND RUN THE PROJECT

  Step 1: Prepare the Project Files
  
    Create a Folder: Create a new directory on your computer named mental-wellness-sanctuary
    Save the File: Save the complete code for the single-file application into this folder as index.html.  (Ensure you use the latest version provided, which contains all the necessary         fixes.)
  Step 2: Install a Local Web Server
   
    Browsers restrict many JavaScript features (like modules and API calls) when files are opened directly via file: path. You need a simple local web server.
    Option A: Recommended (Using Python's Built-in Server)
    If you have Python installed (which you do!), you can start a server with a single command:
    Open your terminal or command prompt.
    Navigate to your project directory
    Start the simple HTTP server
    Option B: VS Code Live Server Extension
    If you use VS Code, install the "Live Server" extension. Right-click on index.html in the file explorer and select "Open with Live Server."
  Step 3: Run the Application
   
    After starting the server (using Option A or B), open your web browser.
    Navigate to the local address.
  Step 4: Verification and First Log
   
    Check Initialization: Upon loading, look for the temporary message banner (top center) that confirms: "Sanctuary initialized and connected to Firestore!" This confirms that Firebase       Authentication and the Firestore database are successfully connected using the global Canvas variables.
    Log an Entry (CRUD Create): Fill out the fields in the "1. Log Daily Entry" section and click "Save Entry."
    Verify History (CRUD Read): Your entry should instantly appear in the "2. Entry History" table and on the Chart.
    Test Analytics: Run the "Run Mood Prediction" feature (after logging 5+ entries) and review the Weekly Averages to ensure the JavaScript logic is processing the data correctly.

INSTRUCTIONS FOR TESTING
   
  Testing for the Mental Wellness Sanctuary must verify that all three functional modules work properly and that non-functional requirements are fulfilled, especially emphasizing reliability and usability. Testing starts with Setup and Initialization (Phase 1): After loading, check that Firebase connects properly and that the application shows the "Sanctuary initialized and connected to Firestore!" message, which verifies that essential security and data synchronization are functioning.
  Subsequently, CRUD Operations (Phase 2) need to be thoroughly verified. Initially, verify Creation by entering a valid entry and confirming it promptly shows up in the History table and on the chart (Real-time Read). It is essential to test Error Handling by trying to input data beyond the specified ranges (e.g., Mood 8/5) or using non-numeric values; the system should deny the entry and show a clear error message. Additionally, verify that the Date Conflict Check functions by blocking the storage of a repeated entry for the identical day. Lastly, confirm the Update and Delete functions by altering an existing record and witnessing the immediate change, along with verifying deletion functionality through the customized modal (Usability Assessment).
   The Analytics and Insights (Phase 3) stage confirms the data processing. Begin by recording a minimum of seven entries and check that the "Weekly Mood Average" and "Sleep Average" accurately compute and show the statistical outcomes. Verify Data Integrity by ensuring that the table entries are sorted accurately (in descending order by date). The Prediction Feature needs particular focus: make sure it remains locked until at least five entries are recorded, and when prepared, run the prediction to confirm it gives a restricted value (1.00 - 5.00) and does not fail.
  Finally, conduct Usability and Reliability Assessments (Phase 4). This involves verifying the Delete Modal to guarantee it functions as a neat, in-app UI element (not a browser pop-up) and checking that quickly clicking "Save Entry" right after the page prevents database crashes during the Firebase initialization race condition.
