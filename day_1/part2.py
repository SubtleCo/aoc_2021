from data import input_string
import helpers

input_list = helpers.split_new_line_seperated_string(int, input_string)


def count_depth_increases_group(input):
    depth_increases  = 0
    for i, step in enumerate(input):
        # return when final group is reached
        if i + 3 == len(input):
            return depth_increases

        # set up groups
        first_group = sum(input[i:i+3])
        second_group = sum(input[i+1:i+4])

        if first_group < second_group:
            depth_increases += 1


def main():
    print(count_depth_increases_group(input_list))


if __name__ == "__main__":
    main()