import sys


if len(sys.argv) == 1:
    exit()
assert len(sys.argv) == 2, "more than one argument is provided"
assert sys.argv[1].lstrip('-').isdigit(), "argument is not an integer"

number = int(sys.argv[1])
if number % 2 == 0:
    print("I'm Even.")
elif number:
    print("I'm Odd")
