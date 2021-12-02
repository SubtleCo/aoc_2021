from data import input

input_tuple = input.split("\n")

def count_depth_increases(input):
    depth_increases  = 0
    for i, step in enumerate(input):
        if i + 1 == len(input):
            return depth_increases
        if int(step) < int(input[i+1]):
            depth_increases += 1
            
def main():
    print(count_depth_increases(input_tuple))
    
if __name__ == "__main__":
    main()
    