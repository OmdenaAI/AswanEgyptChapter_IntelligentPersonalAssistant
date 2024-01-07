def add_time_durations(time_str1, time_str2):
    # Function to convert time string to minutes
    def convert_to_minutes(time_str):
        value, unit = time_str.split()
        if unit == 'hours' or unit == 'hour':
            return int(value) * 60
        elif unit == 'minutes' or unit == 'minute':
            return int(value)
        else:
            raise ValueError(f"Unsupported time unit: {unit}")

    # Convert input time strings to minutes
    minutes1 = convert_to_minutes(time_str1)
    minutes2 = convert_to_minutes(time_str2)

    # Calculate the sum of minutes
    total_minutes = minutes1 + minutes2

    # Convert total minutes back to hours and minutes
    total_hours = total_minutes / 60

    # Format the result string
    result_str = f'{total_hours:.1f} hours'

    return result_str