from data import input

input_tuple = [int(item) for item in input.split("\n")]


def count_depth_increases_group(input):
    depth_increases  = 0
    for i, step in enumerate(input):
        # return when final group is reached
        if i + 3 == len(input):
            print(f'first group is {first_group}')
            print(f'second group is {second_group}')
            return depth_increases
        
        # set up groups
        first_group = sum(input[i:i+3])
        second_group = sum(input[i+1:i+4])
        
        
        if first_group < second_group:
            depth_increases += 1
        
            
def main():
    print(count_depth_increases_group(input_tuple))
    
if __name__ == "__main__":
    main()