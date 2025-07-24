from pynput import keyboard, mouse
from datetime import datetime
import time
import pygetwindow as gw



idle_threshhold = 60 # seconds

last_activity_time = datetime.now()

def on_active(x=None):
    global last_activity_time
    last_activity_time = datetime.now()

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
if __name__ == "__main__":
    print("starting activity tracker...")
    start_listening()

    try:
        while True:
            status = user_status()
            window_title = get_active_window()
            print(f"[{datetime.now().strftime(' %H:%M:%S')}] User is currently: {status} | Active Window: {window_title}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Activity tracker stopped by user.")
