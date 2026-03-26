# AI-Smart-Study-Scheduler
AI Smart Study Scheduler is a web-based app that creates an optimized timetable using inputs like subjects, priority, difficulty, and available time. It uses rule-based AI and adaptive learning to adjust schedules based on user performance, helping students improve time management and productivity.
AI Smart Study Scheduler

An intelligent web application that helps students generate an optimized study timetable based on subjects, priorities, difficulty levels, and available time.
The system also adapts using user behavior (completed/skipped tasks) to improve future schedules.

 
Features
- Multi-subject input with priority & difficulty
- AI-based timetable generation
- Automatic break scheduling
- 12-hour time format (AM/PM)
- Real-time UI updates (Done / Skipped)
- Adaptive learning (basic ML)
- Clean and responsive UI


AI & ML Concepts Used
- Rule-Based Scheduling
- Weighted Scoring Model
- Heuristic Optimization
- Adaptive Learning (behavior-based)
- Feedback Loop System
- Basic Reinforcement Learning (reward/penalty)


Technology used
- Backend: Python (Flask)
- Frontend: HTML, CSS, JavaScript
- Storage: JSON (for learning data)



 Project Structure

ai_study_scheduler/
│── app.py
│── data.json
│── requirements.txt
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css



 Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/ai-study-scheduler.git
cd ai-study-scheduler

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open in browser

http://127.0.0.1:5000/



How It Works

1. User inputs:
   - Subjects
   - Priority (High/Medium/Low)
   - Difficulty (Hard/Medium/Easy)
   - Total study hours

2. AI Logic:
   - Calculates score using priority + difficulty
   - Adjusts using past performance (ML)
   - Distributes study time accordingly

3. Output:
   - Generates optimized timetable
   - Includes breaks
   - Displays suggestions

4. ML Adaptation:
   - ✔ Completed → reduces future weight
   - ✖ Skipped → increases future weight



🎯 Example Output
Time| Subject| Status
06:00 AM–07:00 AM| Math| ✔ Done
07:00 AM–08:00 AM| Physics| ✖ Skipped
08:00 AM–08:15 AM| Break| -


Future Improvements
-  Calendar view (real dates)
-  Progress graphs & analytics
-  AI chatbot assistant
-  Reminder notifications
- Deployment (online hosting)
- Mobile-friendly UI



 Use Cases
 Students preparing for exams
- Daily study planning
- Time management improvement
- Productivity tracking



Developed as an AI-based to demonstrate practical application of intelligent scheduling and adaptive learning systems.
This project uses a lightweight ML approach (behavior-based learning).
It can be extended with advanced ML models for prediction and optimization
