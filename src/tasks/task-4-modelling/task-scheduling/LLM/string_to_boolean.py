def string_to_boolean(string_value):
    try:
        boolean_value = eval(string_value)
        if isinstance(boolean_value, bool):
            return boolean_value
        else:
            raise ValueError("Invalid boolean expression")
    except Exception as e:
        print(f"Error: {e}")
        return None