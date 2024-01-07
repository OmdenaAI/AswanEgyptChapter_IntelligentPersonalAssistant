from datetime import datetime, timedelta

def convert_time_to_string(time_str):
    time_format = "%H:%M:%S"
    time_obj = datetime.strptime(time_str, time_format)

    if time_obj.hour == 0:
        minutes = time_obj.minute
        if minutes == 1:
            return f'{minutes} minute'
        else:
            return f'{minutes} minutes'
    else:
        hours = time_obj.hour
        if hours == 1:
            return f'{hours} hour'
        else:
            return f'{hours} hours'

