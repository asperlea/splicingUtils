__author__ = 'adriana'

from itertools import islice
from collections import defaultdict
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
from math import isnan

def getCounts(countsFile):
    countsDict = defaultdict(int)
    allCountsDict = defaultdict(list)

    while True:
        next_2_lines = list(islice(countsFile, 2))
        if not next_2_lines:
            break

        sequence = next_2_lines[0].strip()
        counts = next_2_lines[1].strip("[]\n").split(", ")
        countsDict[sequence] = float(counts[-1])
        allCountsDict[sequence] = [float(counts[i]) for i in range(0, len(counts) - 1)]
    return countsDict, allCountsDict

def main():
    exons = open("mut_nat_common_exons.txt", "r")
    countsNatFile = open("countsPerbin_mut.txt", "r")
    countsMutFile = open("countsPerbin_nat.txt", "r")
    dataFile = open("nat_vs_mut_data.txt", "w")

    natCounts, allNat = getCounts(countsNatFile)
    mutCounts, allMut = getCounts(countsMutFile)

    ox = []
    oy = []
    histData = []
    countNAN = 0
    for line in exons:
        exon = line.strip()
        ox.append(natCounts[exon])
        oy.append(mutCounts[exon])

        (corr, pvalue) = pearsonr(allNat[exon], allMut[exon])
        if not isnan(corr):
            print corr
            histData.append(corr)
        else:
            countNAN += 1
        dataFile.write(exon + "," + str(ox[-1]) + "," + str(oy[-1]) + "\n")

    print "This many NAN: ", countNAN
    print len(histData)
    plt.hist(histData)
    plt.savefig("nat_vs_mut_hist.png")
    '''
    plt.scatter(ox, oy)
    plt.savefig("nat_vs_mut.png")
    '''
    dataFile.close()

main()