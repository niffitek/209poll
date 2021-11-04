import sys


def check_input():
    if len(sys.argv) != 4:
        exit(84)
    try:
        if float(sys.argv[1]) < 0:
            exit(84)
        if float(sys.argv[2]) < 0:
            exit(84)
        if int(sys.argv[1]) <= int(sys.argv[2]):
            exit(84)
        if float(sys.argv[3]) > 100.0 or float(sys.argv[3]) < 0.0:
            exit(84)
    except ValueError:
        exit(84)
