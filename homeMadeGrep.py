'''
homeMadeGrep.py maps a set of DNA sequences from an input file to another input reference file. This essentially
a home made implementation of grep, adapted to the details of our analysis, but can be easily customized for other uses.
Usage: python homeMadeGrep.py <file1> <file2>
       <file1>: a file containing a list of DNA sequences, one per line
       <file2>: a file containing the reference chip; every line has the Ensembl ID of the sequence, followed by the sequence

This script assumes that the sequences in the file2 reference are contained between the GGCGCGCC and TTAATTAA primer
sites, and that the sequences in file1 contain the TTAATTAA primer as well.

Output:
The list of sequences in file1, and their corresponding Ensembl IDs.
'''

__author__ = 'adriana'

import os
import sys

def main():
    if len(sys.argv) < 3:
        print "Need input file to grep in and input file containing what to grep for"
        exit(1)
    words = open(sys.argv[1], "r")
    text = open(sys.argv[2], "r")

    # hash text
    textHash = {}
    for line in text:
        ID = line.split()[0]
        sequence = line.split()[1][15:-15].upper() #15:-15 slicing removes primers
        textHash[sequence] = ID
        
    for line in words:
        word = line.strip()
        pos = word.find("TTAATTAA")
        word = word[:pos] # only keep everything up to TTAATTAA
        if word in textHash:
            print word, textHash[word]

main()
