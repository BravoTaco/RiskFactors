from StatesInformation import StateInformation

indicators = ["Heart Disease Death Rate", "Motor Vehicle Death Rate", "Teen Birth Rate", "Adult Smoking",
              "Adult Obesity"]


def string_contains_indicators(string):
    for indicator in indicators:
        if not (indicator in string):
            return False
    return True


def get_longest_indicator():
    longest_word_size = -1
    longest_word = ""
    for indicator in indicators:
        if len(indicator) > longest_word_size:
            longest_word_size = len(indicator)
            longest_word = indicator
    return longest_word


def filter_state_information(line_list):
    current_index = 0
    states_information = []
    should_add_state_information = False
    for string in line_list:
        if should_add_state_information:
            states_information.append(line_list[current_index])
        if string_contains_indicators(string):
            should_add_state_information = True
        current_index += 1
    return states_information


def create_state_information_from_string_array(string_array):
    return StateInformation(string_array[0], string_array[1], string_array[5], string_array[7], string_array[11],
                            string_array[13])


def initialize_states(states_information_strings):
    temp_states_information_objects = []
    for string in states_information_strings:
        split_string = string.split(',')
        if len(split_string) >= 13:
            temp_states_information_objects.append(create_state_information_from_string_array(split_string))
    return temp_states_information_objects


def fill_whitespace(amount):
    temp_whitespace = ""
    for x in range(0, amount, 1):
        temp_whitespace += " "
    return temp_whitespace


def fill_with_chars(char, amount):
    temp_chars = ""
    for x in range(0, amount, 1):
        temp_chars += char
    return temp_chars


def set_min_max_values(state_objects):
    min_max_heart_disease_death_rate = [state_objects[0], state_objects[0]]
    min_max_motor_vehicle_death_rate = [state_objects[0], state_objects[0]]
    min_max_teen_birth_rate = [state_objects[0], state_objects[0]]
    min_max_adult_smoking = [state_objects[0], state_objects[0]]
    min_max_adult_obesity = [state_objects[0], state_objects[0]]

    for state in state_objects:
        if min_max_heart_disease_death_rate[0].heart_disease_death_rate > state.heart_disease_death_rate:
            min_max_heart_disease_death_rate[0] = state
        if min_max_heart_disease_death_rate[1].heart_disease_death_rate < state.heart_disease_death_rate:
            min_max_heart_disease_death_rate[1] = state
        if min_max_motor_vehicle_death_rate[0].motor_vehicle_death_rate > state.motor_vehicle_death_rate:
            min_max_motor_vehicle_death_rate[0] = state
        if min_max_motor_vehicle_death_rate[1].motor_vehicle_death_rate < state.motor_vehicle_death_rate:
            min_max_motor_vehicle_death_rate[1] = state
        if min_max_teen_birth_rate[0].teen_birth_rate > state.teen_birth_rate:
            min_max_teen_birth_rate[0] = state
        if min_max_teen_birth_rate[1].teen_birth_rate < state.teen_birth_rate:
            min_max_teen_birth_rate[1] = state
        if min_max_adult_smoking[0].adult_smoking > state.adult_smoking:
            min_max_adult_smoking[0] = state
        if min_max_adult_smoking[1].adult_smoking < state.adult_smoking:
            min_max_adult_smoking[1] = state
        if min_max_adult_obesity[0].adult_obesity > state.adult_obesity:
            min_max_adult_obesity[0] = state
        if min_max_adult_obesity[1].adult_obesity < state.adult_obesity:
            min_max_adult_obesity[1] = state

    return [min_max_heart_disease_death_rate, min_max_motor_vehicle_death_rate,
            min_max_teen_birth_rate,
            min_max_adult_smoking, min_max_adult_obesity]
