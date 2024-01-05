import sys

def add_arguments(arguments):
    return sum(int(arg) for arg in arguments)

if _name_ == "_main_":
    # Extract command line arguments excluding the script name
    arguments = sys.argv[1:]
    
    # Check if there are any arguments
    if arguments:
        result = add_arguments(arguments)
        print(result)
    else:
        print("No arguments provided.")
