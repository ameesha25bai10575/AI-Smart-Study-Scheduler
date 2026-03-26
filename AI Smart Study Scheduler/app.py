from flask import Flask, render_template, request
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)

DATA_FILE = "data.json"

# ---------- DATA ----------
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


# ---------- ML ----------
def get_learning_weight(subject, history):
    if subject not in history:
        return 1

    completed = history[subject]["completed"]
    skipped = history[subject]["skipped"]

    return 1 + (skipped * 0.5) - (completed * 0.2)


# ---------- AI ----------
def calculate_score(priority, difficulty, ml_weight):
    priority_map = {"High": 3, "Medium": 2, "Low": 1}
    difficulty_map = {"Hard": 2, "Medium": 1, "Easy": 0}

    return (priority_map[priority] + difficulty_map[difficulty]) * ml_weight


def format_time(dt):
    return dt.strftime("%I:%M %p")  # AM/PM


def generate_schedule(subjects, total_hours):
    history = load_data()

    for s in subjects:
        ml_weight = get_learning_weight(s['name'], history)
        s['score'] = calculate_score(s['priority'], s['difficulty'], ml_weight)

    total_score = sum(s['score'] for s in subjects)

    for s in subjects:
        s['allocated_time'] = round((s['score'] / total_score) * total_hours, 2)

    timetable = []
    current_time = datetime.strptime("06:00", "%H:%M")

    study_count = 0

    for s in subjects:
        sessions = int(s['allocated_time'])

        for _ in range(sessions):
            end_time = current_time + timedelta(hours=1)

            timetable.append({
                "start": format_time(current_time),
                "end": format_time(end_time),
                "subject": s['name'],
                "priority": s['priority'],
                "suggestion": get_suggestion(s['priority'])
            })

            current_time = end_time
            study_count += 1

            # Break after 2 study sessions
            if study_count % 2 == 0:
                break_end = current_time + timedelta(minutes=15)
                timetable.append({
                    "start": format_time(current_time),
                    "end": format_time(break_end),
                    "subject": "Break",
                    "priority": "-",
                    "suggestion": "Relax / Refresh"
                })
                current_time = break_end

    return timetable


def get_suggestion(priority):
    return {
        "High": "Deep Focus Study",
        "Medium": "Practice + Revision",
        "Low": "Light Study"
    }[priority]


# ---------- ROUTES ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    timetable = None

    if request.method == 'POST':
        names = request.form.getlist('subject')
        priorities = request.form.getlist('priority')
        difficulties = request.form.getlist('difficulty')
        total_hours = float(request.form['hours'])

        subjects = []
        for i in range(len(names)):
            subjects.append({
                "name": names[i],
                "priority": priorities[i],
                "difficulty": difficulties[i]
            })

        timetable = generate_schedule(subjects, total_hours)

    return render_template('index.html', timetable=timetable)


@app.route('/update', methods=['POST'])
def update():
    subject = request.form['subject']
    status = request.form['status']

    data = load_data()

    if subject not in data:
        data[subject] = {"completed": 0, "skipped": 0}

    if status == "completed":
        data[subject]["completed"] += 1
    else:
        data[subject]["skipped"] += 1

    save_data(data)
    return "OK"


if __name__ == '__main__':
    app.run(debug=True)