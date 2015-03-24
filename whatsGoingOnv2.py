__author__ = 'adriana'

import sys
from itertools import islice

def main():
    libraryFile = open(sys.argv[1], "r")
    while True:
        next_4_lines = list(islice(libraryFile, 4))
        if not next_4_lines:
            break
        header = next_4_lines[0].strip()
        sequence = next_4_lines[1].strip() + next_4_lines[2].strip() + next_4_lines[3].strip()
        print header.split()
        print sequence

main()