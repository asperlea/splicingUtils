__author__ = 'adriana'

import sys
from collections import defaultdict

def parseMDtag(MDtag):
    print MDtag
    MDtag = MDtag.split(":")[2]
    num = 0
    diff = 0
    SNPS = []
    for ch in MDtag:
        if ch.isdigit():
            diff = diff * 10 + int(ch)
        else:
            SNPS.append((num + diff, ch))
            num += diff
            diff = 0
    return SNPS

def main():
    readsFile = open("uniqReadsCoverage/10-22079066-reads.txt", "r")
    alignmentFile = open("test_alignment_mut.txt", "r")
    numMaps = defaultdict(int)

    alignmentDict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: "")))


    print "Creating dictionary from alignment file . . ."
    for line in alignmentFile:
        if line[0] != '@':
            data = line.split()
            read = data[9]
            if data[2] != "*":
                if len(data) >= 19:
                    exon = data[2].split("-")[0]
                    mutant = data[2].split("-")[1]
                    MDZ = data[18]
                    if MDZ.find("MD:Z:"):
                        alignmentDict[read][exon][mutant] = MDZ
    print "Done."

    for line in readsFile:
        read = line.split()[1]
        count = int(line.split()[0])

        if count > 50 and len(read) == 170:
            print alignmentDict[read][exon]['1']
            exit(0)
            natSNPS = parseMDtag(alignmentDict[read][exon]['1'])

            if len(alignmentDict[read]) > 1:
                print "GARBAGE READ"
                continue

            mutsInfo = []
            for exon in alignmentDict[read]:
                for mutant in alignmentDict[read][exon]:
                    mutSNPS = parseMDtag(alignmentDict[read][exon][mutant])

                    for natSNP in natSNPS:
                        if natSNP not in mutSNPS:
                            mutsInfo.append(mutant)
                            break
            print read
            print mutsInfo

main()
