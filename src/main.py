import sys
from .error import check_input
from.output import output


def main():
    check_input()
    output(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))


