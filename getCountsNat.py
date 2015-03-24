__author__ = 'adriana'

import os
import sys
from collections import defaultdict

def main():
    if len(sys.argv) < 2:
        print "Need input file with unique contigs"
        exit(1)
    countsFile = open("countsPerbin.txt", "w")
    coverageFile = open("coveragePerbin.txt", "w")

    dirlist = ["1-22079057", "2-22079058", "3-22079059", "4-22079060",  "5-22079061", "6-22079062", "7-22079063", "8-22079064", "17-22079073"]
    binContigsDicts = []
    totalCounts = []
    for dirct in dirlist:
        print "dir = ", dirct
        total = 0
        binContigsFile = open(dirct + "/perfectSeqs.txt")
        binContigs = defaultdict(int)
        for line in binContigsFile:
            contig = line.strip()
            binContigs[contig] += 1
            total += 1
        binContigsDicts.append(binContigs)
        totalCounts.append(total)
    print totalCounts

    contigsFile = open(sys.argv[1], "r") # contigs file
    idx = 0
    for line in contigsFile:
        contig = line.strip()
        countsPerBin = []
        coveragePerBin = []
        idx += 1
        if idx % 100 == 0:
            print "Done with ", idx, " contigs."
        bidx = 0
        for i in range(len(binContigsDicts)):
            binDict = binContigsDicts[i]
            counts = binDict[contig]
            coveragePerBin.append(float(counts))
            countsPerBin.append(float(counts) / totalCounts[i])
        countsFile.write(contig+"\n")
        countsFile.write(str(countsPerBin) + "\n")
        coverageFile.write(contig+"\n")
        coverageFile.write(str(coveragePerBin) + "\n")
    countsFile.close()
    coverageFile.close()

main()
