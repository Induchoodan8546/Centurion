import pandas as pd
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

    app_usage ={}
    for i in range(len(df)-1):
        current = df.iloc[i]
        next = df.iloc[i + 1]
        duration = next['timestamp'] - current['timestamp']
        # Clean app title
        raw_app = current['application']
        if "Visual Studio Code" in raw_app:
            app = "VS Code"
        elif "Google Chrome" in raw_app:
            app = "Chrome"
        elif "Brave" in raw_app:
            app = "Brave"
        else:
            app = raw_app


        if app not in app_usage:
            app_usage[app] = duration
        else:
            app_usage[app] += duration

    sorted_apps = sorted(app_usage.items(), key =lambda x: x[1], reverse=True)

    print("\n🖥️   Application usage summary:")
    for app, duration in sorted_apps:
        print(f"{app} | {duration}")

if __name__ == "__main__":

    print_activity_summary()
    print_app_usage_summary()