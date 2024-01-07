from datetime import datetime, timedelta

def parse_time(initial_time, time_str):
    amount, unit = time_str.split()
    amount = float(amount)

    if unit.lower() in ['minute', 'minutes']:
        time_delta =  timedelta(minutes=amount)
    elif unit.lower() in ['hour', 'hours']:
        time_delta = timedelta(hours=amount)

   

    current_time = datetime.strptime(initial_time, "%I:%M %p")


    result_time = current_time + time_delta

    # Formatting the time in AM/PM format
    #input_time_formatted = current_time.strftime("%I:%M %p")
    result_time_formatted = result_time.strftime("%I:%M %p")
    
    return result_time_formatted