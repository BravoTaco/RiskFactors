import StringUtilities as String_Util


def retrieve_file_contents(file_path):
    try:
        with open(file_path, 'r') as f:
            file_information = f.read()
            f.close()
            return file_information
    except IOError:
        return False


def construct_column(indicator, min_value_string, min_value, max_value_string, max_value):
    first_colon_index = len(String_Util.get_longest_indicator() * 2)
    second_colon_index = first_colon_index * 2
    temp_chars = []
    for x in range(0, first_colon_index + second_colon_index):
        if x != first_colon_index and x != second_colon_index:
            temp_chars.append(" ")
        elif x == first_colon_index:
            temp_chars.append(":")
        elif x == second_colon_index:
            temp_chars.append(":")
    temp_chars.append('\n')
    string = ""
    current_index = 0
    for char in indicator:
        temp_chars[current_index] = char
        current_index += 1
    current_index = first_colon_index + 2
    for char in min_value_string:
        temp_chars[current_index] = char
        current_index += 1
    current_index = second_colon_index - 2
    for char in min_value[::-1]:
        temp_chars[current_index] = char
        current_index -= 1
    current_index = second_colon_index + 2
    for char in max_value_string:
        temp_chars[current_index] = char
        current_index += 1
    current_index = len(temp_chars) - 2
    for char in max_value[::-1]:
        temp_chars[current_index] = char
        current_index -= 1
    for char in temp_chars:
        string += char
    return string


def construct_divider():
    first_colon_index = len(String_Util.get_longest_indicator() * 2)
    second_colon_index = first_colon_index * 2
    temp_chars = []
    for x in range(0, first_colon_index + second_colon_index):
        temp_chars.append('-')
    temp_chars.append('\n')
    string = ""
    for char in temp_chars:
        string += char
    return string


def construct_columns(min_max_values):
    output_data = construct_column(indicator="Indicator", max_value_string="Max", max_value=" ",
                                   min_value_string="Min", min_value=" ")
    output_data += construct_divider()

    for x in range(0, len(String_Util.indicators), 1):
        min_value_state_name = min_max_values[x][0].state_name
        min_value = str(min_max_values[x][0].information[x])
        max_value_state_name = min_max_values[x][1].state_name
        max_value = str(min_max_values[x][1].information[x])
        indicator = String_Util.indicators[x]
        output_data += construct_column(indicator=indicator, max_value_string=max_value_state_name,
                                        max_value=max_value, min_value_string=min_value_state_name,
                                        min_value=min_value)
    return output_data


def save_file(file_path, data):
    try:
        with open(file_path, 'w') as f:
            f.write(data)
            f.close()
            return True
    except IOError:
        return False
