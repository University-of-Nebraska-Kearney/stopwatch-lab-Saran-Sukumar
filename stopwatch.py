# Import Library
import datetime

def time_in_seconds(hours, minutes, seconds):
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)

def format_time(elapsed_seconds):
    hours = int(elapsed_seconds // 3600)
    minutes = int((elapsed_seconds % 3600) // 60)
    seconds = elapsed_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:05.2f}"

# Get time for start
input("Press Enter to start the stopwatch.")
start_time = str(datetime.datetime.now().time()).split(":")
start_hour = start_time[0]
start_minute = start_time[1]
start_second = start_time[2]

# Get time for stop
input("Press Enter again to stop the stopwatch.")
stop_time = str(datetime.datetime.now().time()).split(":")
stop_hour = stop_time[0]
stop_minute = stop_time[1]
stop_second = stop_time[2]

# Calculate elapsed time in seconds
start_total_seconds = time_in_seconds(start_hour, start_minute, start_second)
stop_total_seconds = time_in_seconds(stop_hour, stop_minute, stop_second)
elapsed_time_seconds = stop_total_seconds - start_total_seconds

# Display the result
formatted_time = format_time(elapsed_time_seconds)
print(f"Elapsed time: {formatted_time}")



