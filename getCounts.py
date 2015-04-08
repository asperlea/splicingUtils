__author__ = 'adriana'

'''
getCounts takes three inputs:
<mut/nat>: specifying whether the analysis is for the mutant or natural library
<file1>: the name of the file containing the perfectly mapped reads in each bin directory
<file2>: the name of the file containing all the exons in the library
and outputs a file that contains each exon in the library on a line, followed by a list of how many counts of that
exons appear in each bin, normalized by the total number of reads in that bin.
These counts are listed in the order of the bins in the dirlist dictionary. Look at the mCherry run on basespace
for more details about bin names.
'''

import os
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 4:
        print '''Usage: python getCountsMut.py <mut/nat> <file1> <file2>
                 <file1>: name of file in each bin directory containing the perfectly mapped reads
                 <file2>: name of file containing all exons in the library'''
        exit(1)
    else:
        type = sys.argv[1]
        seqsFilename = sys.argv[2]
        allSeqs = sys.argv[3]
    countsFile = open("countsPerbin" + type + ".txt", "w")

    # bin directory names
    dirlist = {'mut': ["9-22079065", "10-22079066", "11-22079067", "12-22079068", "13-22079069", "14-22079070", "15-22079071", "16-22079072", "18-22079074"],
               'nat': ["1-22079057", "2-22079058", "3-22079059", "4-22079060",  "5-22079061", "6-22079062", "7-22079063", "8-22079064", "17-22079073"]}

    # For every bin, create a hash counting how many of each read are in the bin
    binContigsDicts = []
    totalCounts = []
    for dirct in dirlist[type]:
        print "dir = ", dirct
        binContigsFile = open(dirct + "/" + seqsFilename)
        binContigs = defaultdict(int)
        total = 0
        for line in binContigsFile:
            contig = line.strip().split()[0]
            binContigs[contig] += 1
            total += 1
        totalCounts.append(total)
        binContigsDicts.append(binContigs)

    # For each exon and each bin, calculate the normalized count of that exon in that bin
    contigsFile = open(allSeqs, "r") # all exons file
    idx = 0
    for line in contigsFile:
        contig = line.strip()
        countsPerBin = []
        idx += 1
        if idx % 100 == 0:
            print "Done with ", idx, " contigs."
        bidx = 0
        for i in range(len(binContigsDicts)):
            binDict = binContigsDicts[i]
            counts = binDict[contig]
            countsPerBin.append(counts / float(totalCounts[i]))

        countsFile.write(contig+"\n")
        countsFile.write(str(countsPerBin) + "\n")
    countsFile.close()

main()
