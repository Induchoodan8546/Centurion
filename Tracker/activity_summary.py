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
if __name__ == "__main__":
    print("Activity summary:")
    print_activity_summary()