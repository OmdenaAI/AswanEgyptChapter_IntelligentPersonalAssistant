import re
import ast  # ast module is used to safely evaluate the extracted string as a literal

def extract_first_list(input_string):
    # Use regular expression to find the first list in the string
    match = re.search(r'\[.*?\]', input_string)

    if match:
        # Extract the matched substring
        list_string = match.group(0)

        # Safely evaluate the string as a literal list using ast module
        first_list = ast.literal_eval(list_string)

        return first_list
    else:
        return None
