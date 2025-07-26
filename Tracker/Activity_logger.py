from pynput import keyboard, mouse



from datetime import datetime
import time
import pygetwindow as gw
import csv
import os


idle_threshhold = 60 # seconds

last_activity_time = datetime.now()
last_logged_status = None
last_logged_app = None



def on_active(x=None):
    global last_activity_time
    global last_logged_status, last_logged_app
    last_activity_time = datetime.now()
    last_logged_status = None
    last_logged_app = None


def start_listening():
    mouse_listener = mouse.Listener(on_move=on_active, on_click=on_active, on_scroll=on_active)
    keyboard_listener = keyboard.Listener(on_press=on_active, on_release=on_active)
    mouse_listener.start()
    keyboard_listener.start()
def user_status():
    now = datetime.now()
    elapsed_time = (now - last_activity_time).total_seconds()
    return "idle"if elapsed_time > idle_threshhold else "active"
def get_active_window():
    try:
        active_window = gw.getActiveWindow()
        if active_window:
            return active_window.title
        else:
            return "No active window"
    except Exception as e:
        return f"Error retrieving active window: {str(e)}"
def log_activity_to_csv(timestamp, status, app_name, file_path="activity_log.csv"):
    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)   
        if not file_exists:
            writer.writerow(["timestamp", "status", "application"])

        writer.writerow([timestamp, status, app_name])
        

    

if __name__ == "__main__": 
    print("starting activity tracker...")
    start_listening()

    try:
       while True:
           timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
           status = user_status()
           window_title = get_active_window()

           print(f"[{timestamp}] User is currently: {status} | App: {window_title}")

           #  Only log when status or app changes
           if status != last_logged_status or window_title != last_logged_app:
               log_activity_to_csv(timestamp, status, window_title)
               last_logged_status = status
               last_logged_app = window_title

           time.sleep(5)


    except KeyboardInterrupt:
        print("Activity tracker stopped by user.")
        
