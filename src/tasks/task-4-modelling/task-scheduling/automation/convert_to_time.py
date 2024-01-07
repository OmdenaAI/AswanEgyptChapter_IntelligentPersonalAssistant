from datetime import datetime

def convert_to_time(time_str):
    # Define the format of the input time string
    time_format = "%I:%M %p"  # %I: Hour (12-hour clock), %M: Minute, %p: AM/PM

    try:
        # Parse the input time string to a datetime object
        time_object = datetime.strptime(time_str, time_format)

        # Extract the time part (hour and minute) from the datetime object
        #time_part = time_object.strftime("%I:%M %p")

        return time_object

    except ValueError as e:
        print(f"Error: {e}")
        return None