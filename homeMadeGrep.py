__author__ = 'adriana'

import os
import sys
from itertools import islice

def main():
    if len(sys.argv) < 3:
        print "Need input file to grep in and input file containing what to grep for"
        exit(1)
    words = open(sys.argv[1], "r")
    text = open(sys.argv[2], "r")

    # hash text
    textHash = {}
    wtf = ""
    while True:
        next_4_lines = list(islice(text, 4))
        if not next_4_lines:
            break

        header = next_4_lines[0].split()
        ID = header[0]
        sequence = next_4_lines[1].strip().upper() + next_4_lines[2].strip().upper() + next_4_lines[3].strip().upper()
        textHash[sequence] = ID
        
    for line in words:
        word = line.strip()
        pos = word.find("TTAATTAA")
        word = word[:pos]

        if word in textHash:
            print word, textHash[word]

main()
