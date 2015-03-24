__author__ = 'adriana'

import numpy as np
import pylab as P
from collections import defaultdict
from itertools import islice
from scipy.stats.stats import pearsonr

binList = ["nat2", "nat6", "nat5", "nat8", "nat9", "nat10", "nat11", "nat12"] #natural

f_j = [0.1142340965, 0.02279123093, 0.09818295522, 0.0403015669, 0.06507313345, 0.1603029566, 0.1568286836, 0.1927874092] #natural

'''
Example of line in countsPerbin_*.txt
AAAAAAAAAAACCCACCTTGAAAAGTCTCCCTCTTACTTTCTTTCAGGTTCCTTTTTTGCCAGGAGATTCAGACCTTGATCAGCTAACAAGAATATTTGAAACTTTGGGCACACCAACTGAGGAACAGTGGCCGGTAAGCCTTTATGCATTTTCTTTGAAATGTAATTAG
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 5.184046614947161e-06]
'''

def main():
    dataFile = open("countsPerbin_nat.txt", "r")
    natBehavior = open("natBehavior_mut.txt", "r")
    natBehaviorDict = {}
    for line in natBehavior:
        ID = line.strip().split(",")[0]
        behavior = [float(i) for i in line.strip().split(",")[1:]]
        natBehaviorDict[ID] = behavior
    data = []
    binTotals = defaultdict(int)
    numBins = 8
    a_ID_mut = defaultdict(lambda: defaultdict(list))
    mutset = set()

    while True:
        next_2_lines = list(islice(dataFile, 2))
        if not next_2_lines:
            break
        '''
        n2l_cvg = list(islice(coverageFile, 2))
        if not n2l_cvg:
            break
        '''

        ID = next_2_lines[0].strip().split(" ")[1]
        counts = next_2_lines[1].strip("[]\n").split(", ")

        a_i = []
        total_in_all_bins = 0
        for j in range(numBins):
            total_in_all_bins += (float(counts[j]) * (f_j[j]))
        if total_in_all_bins != 0:
            for j in range(numBins):
                a_i.append(float(counts[j]) * f_j[j] / total_in_all_bins)

            if ID in natBehaviorDict:
                natBin = "other"
                if a_i[0] > 0.9 or a_i[1] > 0.9:
                    natBin = "double negatives"
                elif a_i[2] > 0.9 or a_i[3] > 0.9 or a_i[4] > 0.9:
                    natBin = "double positives"
                elif a_i[5] > 0.9 or a_i[6] > 0.9 or a_i[7] > 0.9:
                    natBin = "positive/negative"
                mutBin = "other"
                if natBehaviorDict[ID][0] > 0.9 or natBehaviorDict[ID][1] > 0.9:
                    mutBin = "double negatives"
                elif natBehaviorDict[ID][2] > 0.9 or natBehaviorDict[ID][3] > 0.9 or natBehaviorDict[ID][4] > 0.9:
                    mutBin = "double positives"
                elif natBehaviorDict[ID][5] > 0.9 or natBehaviorDict[ID][6] > 0.9 or natBehaviorDict[ID][7] > 0.9:
                    mutBin = "positive/negative"

                #print "ID = ", ID
                #print "natural library: ", natBin
                #print "mutant library: ", mutBin
                if natBin != mutBin:
                    print ID, natBin, mutBin

                #print "correlation: ", pearsonr(a_i, natBehaviorDict[ID])[0]

main()