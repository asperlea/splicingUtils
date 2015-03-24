__author__ = 'adriana'

import os
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print "Need input file with unique contigs"
        exit(1)
    countsFile = open("countsPerbin_mut.txt", "w")

    dirlist = ["9-22079065", "10-22079066", "11-22079067", "12-22079068", "13-22079069", "14-22079070", "15-22079071", "16-22079072", "18-22079074"]

    binContigsDicts = []
    totalCounts = []
    for dirct in dirlist:
        print "dir = ", dirct
        binContigsFile = open(dirct + "/hm_perfect_seqs.txt")
        binContigs = defaultdict(int)
        total = 0
        for line in binContigsFile:
            contig = line.strip()
            binContigs[contig] += 1
            total += 1
        totalCounts.append(total)
        binContigsDicts.append(binContigs)

    contigsFile = open(sys.argv[1], "r") # contigs file
    idx = 0
    nonzero = 0
    for line in contigsFile:
        nzero = 0
        contig = line.strip()
        countsPerBin = []
        idx += 1
        if idx % 100 == 0:
            print "Done with ", idx, " contigs."
        bidx = 0
        for i in range(len(binContigsDicts)):
            binDict = binContigsDicts[i]
            counts = binDict[contig]
            if i < len(binContigsDicts) - 1:
                nzero += (counts/float(totalCounts[i]) != 0)
            countsPerBin.append(counts / float(totalCounts[i]))

        nonzero += (nzero != 0)
        if nzero == 0:
            print contig
        countsFile.write(contig+"\n")
        countsFile.write(str(countsPerBin) + "\n")
    print "nonzero = ", nonzero
    countsFile.close()

main()
