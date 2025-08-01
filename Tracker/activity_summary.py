import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def clean_app_name(raw_app):
    if not isinstance(raw_app, str):
        return "Unknown"
    elif "Visual Studio Code" in raw_app:
        return "VS Code"
    elif "Google Chrome" in raw_app:
        return "Chrome"
    elif "Brave" in raw_app:
        return "Brave"
    elif "Instagram" in raw_app:
        return "Instagram"
    else:
        return raw_app.strip()

def print_activity_summary():
    try:
        df = pd.read_csv("activity_log.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    except FileNotFoundError:
        print("No activity log found. Please run the tracker first.")
        return    
    except Exception as e:
        print(f"Error reading activity log: {e}")
        return

        total_active_time = pd.Timedelta(0)
        total_idle_time = pd.Timedelta(0)

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
    try:
        df = pd.read_csv("activity_log.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.dropna(subset=['application'])
    except FileNotFoundError:
        print("No activity log found. Please run the tracker first.")
        return
    except Exception as e:
        print(f"Error reading activity log: {e}")
        return

    app_usage = {}
    for i in range(len(df)-1):
        current = df.iloc[i]
        next = df.iloc[i + 1]
        duration = next['timestamp'] - current['timestamp']
        app = clean_app_name(current['application'])
        app_usage[app] = app_usage.get(app, pd.Timedelta(0)) + duration

    sorted_apps = sorted(app_usage.items(), key=lambda x: x[1], reverse=True)[:5]

    print("\n🖥️   Application usage summary:")
    for app, duration in sorted_apps:
        print(f"{app} | {duration}")

def plot_app_usage(file_path="activity_log.csv"):
    try:
        df = pd.read_csv(file_path)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.dropna(subset=['application'])
    except FileNotFoundError:
        print("No activity log found. Please run the tracker first.")
        return 
    except Exception as e:
        print(f"Error reading activity log: {e}")
        return

    app_usage = {}
    for i in range(len(df)-1):
        current = df.iloc[i]
        next = df.iloc[i + 1]
        duration = next['timestamp'] - current['timestamp']
        app = clean_app_name(current['application'])
        app_usage[app] = app_usage.get(app, pd.Timedelta(0)) + duration

    # Sort top 5 apps
    sorted_apps = sorted(app_usage.items(), key=lambda x: x[1], reverse=True)[:5]

    app_names = []
    app_durations = []
    for app, duration in sorted_apps:
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


def plot_hourly_productivity(file_path = "activity_log.csv"):
        try:
            df = pd.read_csv(file_path)
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            df = df[df['status'] == 'active']
            df['hour'] = df['timestamp'].dt.hour
        except FileNotFoundError:
            print("No activity log found. Please run the tracker first.")
            return
        except Exception as e:
            print(f"Error reading activity log: {e}")
            return
        #duration
        hourly_usage ={hour: pd.Timedelta(0) for hour in range(24)}
        for i in range(len(df)-1):
            current = df.iloc[i]
            next = df.iloc[i + 1]
            duration = next['timestamp'] - current['timestamp']
            hour = current['hour']
            hourly_usage[hour] += duration
        print("🕒 Hourly Active Durations:")
        for hour, duration in hourly_usage.items():
            print(f"{hour:02d}:00 → {duration}")
        # Plotting data

        hour_label = []
        minutes_label = []
        for hour in range(24):
            minutes = hourly_usage[hour].total_seconds() / 60
            hour_label.append(f"{hour:02d}:00")
            minutes_label.append(minutes)
        #plotting
        plt.figure(figsize=(12,6))
        plt.bar(hour_label, minutes_label, color='lightgreen')
        plt.title("Hourly Productivity")
        plt.xlabel("Hour")
        plt.ylabel("Active Minutes")
        plt.xticks(rotation=45)
        
        for bar, minutes, in zip(hour_label, minutes_label):
            plt.text(bar.get_x() + bar.get_width()/ 2, bar.get_height() + 1, f'{minutes:.1f}', ha='center', fontsize=8)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    print_activity_summary()
    print_app_usage_summary()
    plot_app_usage()
    plot_hourly_productivity()
