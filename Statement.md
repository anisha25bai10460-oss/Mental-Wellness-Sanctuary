  
**🌟PROBLEM STATEMENT**

Individuals frequently struggle with identifying the root causes of fluctuating mental well-being, stress, and anxiety. This is primarily due to a lack of **systematic, quantitative self-monitoring**, which prevents them from establishing clear correlations between lifestyle factors (such as sleep quality, stress exposure, and anxiety triggers) and their resulting emotional state. Without actionable, historical data, effective self-management and intervention are reduced to guesswork.

**🌟SCOPE OF MY PROJECT**

The scope of this project is limited to a single-page client-side application focused on personal data logging, analysis, and visualization.

#### **1\. Included Functional Scope (What the Project Does)**

* **Core Metrics Tracking:** The system supports logging and tracking five specific wellness metrics: Mood (1-5), Sleep (Hours), Stress (1-10), and Anxiety (1-10).  
* **Full CRUD Lifecycle:** Implementation of Create, Read, Update, and Delete operations for individual wellness entries.  
* **User-Isolated Data Persistence:** Utilization of Google Firestore to securely store data, ensuring each user's data is isolated and persistent across sessions.  
* **Real-time Analytics:** Calculation and display of summary statistics, specifically the **Weekly Mood Average** and **Weekly Sleep Average**.  
* **Visualization:** Dynamic generation of a multi-axis line chart (using Chart.js) to show **Mood vs. Sleep Trends** over the last 10 entries.  
* **Predictive Mock:** Implementation of a simple **JavaScript heuristic** to demonstrate the *concept* of Machine Learning prediction (forecasting next-day mood based on recent historical metrics).

#### **2\. Excluded Functional Scope (What the Project Does Not Do)**

* **No Multi-User Authentication:** The project uses simple Firebase Authentication mechanisms (tokens/anonymous sign-in) and **does not include a full username/password registration system** or user management interface.  
* **No External Data Integration:** The application does not interface with external APIs (e.g., fitness trackers, weather services) to automatically collect data. All data is user-inputted.  
* **No Server-Side Processing:** All analytical and predictive logic is executed client-side via JavaScript; the project **does not include a dedicated Python Flask/FastAPI backend** for complex, server-side ML models.  
* **No Advanced Reporting:** The reporting is limited to basic averages and the primary chart; it does not include exporting data (CSV/PDF) or generating complex comparative reports.  
* **No Notification System:** The application does not send email, push, or in-app notifications or reminders.

**🌟TARGET USERS**

The target users for the **Mental Wellness Sanctuary** are individuals seeking to gain objective, data-driven insight into their own emotional and physiological patterns.

The primary and secondary target users are:

### 

###  **Primary Target Users**

These individuals have a clear, immediate need for the core tracking and correlation features.

1. **The Self-Optimizer (Ages 20–40):**  
   * **Need:** Highly interested in self-improvement, bio-hacking, and quantifying their lifestyle. They use data to optimize performance but recognize that mental health is a critical, often ignored variable.  
   * **Why the Project Appeals:** They appreciate the **Chart.js visualizations** and the **Predictive Mock** feature because it turns abstract feelings (mood, stress) into actionable numbers and trends they can control.  
2. **The Overwhelmed Professional or Student (Ages 18–35):**  
   * **Need:** Experiencing high stress, burnout, or difficulty maintaining a stable routine. They need a simple, low-effort tool to identify which factors (e.g., poor sleep before a deadline) directly trigger mood dips.  
   * **Why the Project Appeals:** The simple **CRUD Logging** is fast and non-judgmental. The **Weekly Averages** offer quick feedback on whether their efforts to manage stress are actually working.

### **Secondary Target Users**

These users might adopt the tool for specific, less frequent needs, or as part of a larger plan.

3. **The Clinically Curious (Any Age):**  
   * **Need:** Individuals already working with a therapist or counselor who need concrete, quantitative data to report during sessions (e.g., "My anxiety peaked on days when I got less than 6 hours of sleep").  
   * **Why the Project Appeals:** The structured input fields (Mood 1-5, Stress 1-10) and the **Historical Data Read** feature provide an objective record, making subjective symptoms easier to discuss and analyze.  
4. **The Tech-Learning Enthusiast (Any Age):**  
   * **Need:** Users who are themselves learning software development or data science and want a simple, personal tool to run their own internal experiments.  
   * **Why the Project Appeals:** They value the transparency of the structure (easy to log, easy to view) and the **Firebase-based security**, which they trust for sensitive, personal information.

**🌟HIGH-LEVEL FEATURES**

1. **Full-Cycle Wellness Data Management (CRUD):** The application provides comprehensive **Create, Read, Update, and Delete (CRUD)** capability for daily wellness entries, covering five key metrics (Mood, Sleep, Stress, Anxiety). This ensures data integrity and allows users to maintain a clean, accurate personal history.  
2. **Real-Time, Secure Data Persistence:** It utilizes **Google Firestore** and **Firebase Authentication** to provide reliable, real-time synchronization of all logged data. This guarantees that user information is secured, isolated per user, and instantly available across sessions, eliminating manual saving.  
3. **Visual Trend Analysis:** The system instantly translates complex numerical data into actionable visual formats. It dynamically generates a multi-axis line chart (using Chart.js) that visualizes **Mood and Sleep trends** over time, allowing users to quickly spot correlations and patterns.  
4. **Instant Reporting and Metrics:** The application provides instant, high-level reporting by calculating and displaying summary statistics, such as the **Weekly Mood Average** and **Weekly Sleep Average**. This serves as a quick, data-driven "pulse check" of the user's well-being.  
5. **Conceptual Predictive Modeling:** It includes a demonstration of predictive capabilities through a **JavaScript heuristic (mock ML)** feature. This allows the system to analyze recent historical metrics (e.g., last night's sleep) and **forecast the user's likely mood for the upcoming day**, introducing the concept of data science into personal health management.

