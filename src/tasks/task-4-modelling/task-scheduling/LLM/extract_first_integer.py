import re

def extract_first_integer(input_string):
    # Using regular expression to find the first integer in the string
    match = re.search(r'\b\d+\b', input_string)

    # Check if a match is found
    if match:
        # Convert the matched string to an integer and return
        return int(match.group())
    else:
        # Return None if no integer is found in the string
        return None
