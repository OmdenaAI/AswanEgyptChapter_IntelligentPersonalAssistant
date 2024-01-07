from datetime import datetime, timedelta

def find_date_by_day(day_string):
    # Get the current date
    current_date = datetime.now()

    # Find the current day of the week as an integer (Monday is 0 and Sunday is 6)
    current_day = current_date.weekday()

    # Define a mapping of day strings to their corresponding indices
    days_mapping = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    # Find the index of the specified day string
    day_index = days_mapping.get(day_string.lower())

    if day_index is not None:
        # Calculate the difference in days between the current day and the desired day
        days_difference = (day_index - current_day + 7) % 7

        # Calculate the date of the desired day
        desired_date = current_date + timedelta(days=days_difference)

        return str(desired_date.date())
    else:
        return None

