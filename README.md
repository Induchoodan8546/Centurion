# 🛡️ Centurion

**Centurion** is an AI-powered personal productivity analyzer that tracks user activity (active vs. idle), monitors foreground applications, and intelligently logs only meaningful changes. It helps you understand where your time goes, without overwhelming logs or distractions.

---

## 🚀 Features

- 🕒 Real-time tracking of user status (active/idle)
- 🪟 Foreground application title detection
- 🧠 Logs only when status or app changes (smart logging)
- 📊 Output stored in `activity_log.csv` for analysis
- 🔒 Lightweight, local, and privacy-focused

---

## 📁 Project Structure

Centurion/
├── tracker/
│ └── activity_logger.py # Main script for activity logging
├── .gitignore # Ignores cache & CSV logs
├── README.md # You're reading it


---

## 📦 Requirements

- Python 3.9+
- Required libraries:
  - pynput – for mouse/keyboard activity
  - pygetwindow – to fetch active window titles

Install them using:

```bash
pip install pynput pygetwindow

Run this command from the root of the project:
python tracker/activity_logger.py

The script will:

Monitor keyboard and mouse activity
Detect which app is currently in use
Log to activity_log.csv only when app or status changes


👤 Author
Induchoodan
🎓 B.Tech CSE (AI & ML), 3rd Year
🏫 College of Engineering Attingal, Kerala
🧠 Passionate about AI, productivity tools, and creative tech solutions
