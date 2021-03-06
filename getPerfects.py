'''
Quick script to get perfect matches from a bowtie2 alignment. Iterates through every line and picks sequences with
a "170M" CIGAR string and a "MD:Z:170" tag.
Usage: python getPerfects.py <file1>
       <file1> : bowtie2 alignment file
'''

import sys

def main():
    if len(sys.argv) < 3:
        print "Need input alignment sam file and file to output perfects into."
        exit(1)

    infile = open(sys.argv[1], "r")
    ofile = open(sys.argv[2], "w")
    for line in infile:
        if line[0] != "@":
            data = line.split()
            if data[1] == "0":
                if data[5] == "170M" and data[17] == "MD:Z:170":
                    ofile.write(data[9] + "\n")

    ofile.close()

main()

