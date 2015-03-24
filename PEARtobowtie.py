__author__ = 'adriana'

import sys
from itertools import islice

def main():
    if len(sys.argv) < 3:
        print "Need input and output files"
        exit(1)
    inFile = open(sys.argv[1], "r") # fastq file
    outFile = open(sys.argv[2], "w")

    oligoLengths = []
    while True:
        next_4_lines = list(islice(inFile, 4))
        if not next_4_lines:
            break

        sequence = next_4_lines[1]
        quality = next_4_lines[3]

        pos = sequence.find("TTAATTAA")
        sequence = sequence[:pos]
        quality = quality[:pos]
        
        if len(sequence) >= 100:
            outFile.write(next_4_lines[0])
            outFile.write(sequence + "\n")
            outFile.write(next_4_lines[2])
            outFile.write(quality + "\n")
    
            oligoLengths.append(len(sequence))
    print "Average oligo length was: ", sum(oligoLengths) / float(len(oligoLengths))

    outFile.close()

main()
