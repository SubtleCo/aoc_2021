def split_new_line_seperated_string(expected_type, input_string):
    input_list = [expected_type(item) for item in input_string.split("\n")]
    return input_list