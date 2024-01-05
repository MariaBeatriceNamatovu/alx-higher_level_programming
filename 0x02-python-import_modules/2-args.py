#/usr/bin/python3
import sys

def print_arguments(arguments):
    num_arguments = len(arguments)

    # Print the number of arguments
    print(f"Number of argument{'s' if num_arguments != 1 else ''}: {num_arguments}", end='')

    # Print the list of arguments
    if num_arguments > 0:
        print(f":")
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")
    else:
        print(".")

if __name__ == "__main__":
    # Extract command line arguments excluding the script name
    arguments = sys.argv[1:]

    print_arguments(arguments)

