import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
def print_activity_summary():
    df = pd.read_csv("activity_log.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    total_active_time = pd.Timedelta(0)
    total_idle_time = pd.Timedelta(0)

    # Calculate total active and idle time
    for i in range(len(df)-1):
        current_row = df.iloc[i]
        next_row = df.iloc[i+1]
        duration = next_row['timestamp'] - current_row['timestamp']
        if current_row['status'] == 'active':
            total_active_time += duration
        else:
            total_idle_time += duration
    
    print("Activity summary:....")
    print("Total tracked duration:", df['timestamp'].iloc[-1] - df['timestamp'].iloc[0])
    print("Total active duration:", total_active_time)
    print("Total idle duration:", total_idle_time)
    print("Number of entries:", len(df))


def print_app_usage_summary():
    df = pd.read_csv("activity_log.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.dropna(subset=['application'])

    app_usage ={}
    for i in range(len(df)-1):
        current = df.iloc[i]
        next = df.iloc[i + 1]
        duration = next['timestamp'] - current['timestamp']
        
        # Clean app title
        raw_app = current['application']
        if not isinstance(raw_app, str):
            continue
        if "Visual Studio Code" in raw_app:
            app = "VS Code"
        elif "Google Chrome" in raw_app:
            app = "Chrome"
        elif "Brave" in raw_app:
            app = "Brave"
        else:
            app = raw_app


        app_usage[app] = app_usage.get(app, pd.Timedelta(0)) + duration

    sorted_apps = sorted(app_usage.items(), key =lambda x: x[1], reverse=True)

    print("\n🖥️   Application usage summary:")
    for app, duration in sorted_apps:
        print(f"{app} | {duration}")

def plot_app_usage(file_path="activity_log.csv"):
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.dropna(subset=['application'])
    app_usage = {}

    app_usage = {}
    for i in range(len(df)-1):
        current = df.iloc[i]
        next = df.iloc[i + 1]
        duration = next['timestamp'] - current['timestamp']
        
        raw_app = current['application']
        if not isinstance(raw_app, str):
            continue
        if "Visual Studio Code" in raw_app:
            app = "VS Code"
        elif "Google Chrome" in raw_app:
            app = "Chrome"
        elif "Brave" in raw_app:
            app = "Brave"
        else:
            app = raw_app

        app_usage[app] = app_usage.get(app, pd.Timedelta(0)) + duration
        app_names = []
        app_durations = []
        for app, duration in app_usage.items():
            minutes = duration.total_seconds() / 60
            app_names.append(app)
            app_durations.append(minutes)
        plt.figure(figsize=(10, 5))
        bars = plt.bar(app_names, app_durations, color='skyblue')
        plt.title('Application Usage Over Time')
        plt.xlabel('Applications')
        plt.ylabel('Usage Duration (minutes)')
        plt.xticks(rotation=45, ha='right')
        for bar, value in zip(bars, app_durations):
            plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, f'{value:.1f}', ha='center', va='bottom')
            plt.tight_layout()
            plt.show()


    
if __name__ == "__main__":

    print_activity_summary()
    print_app_usage_summary()
    plot_app_usage()