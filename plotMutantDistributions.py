__author__ = 'adriana'

import glob
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def main():
    heatmapData = open("mutantTypesPerBin_data.txt", "w")
    mutants = defaultdict(lambda : defaultdict(int))
    binNames = []
    binTranslate = {'9': "mut2", '10': "mut5", '11': "mut8", '12': "mut9", '13': "mut6", '14': "mut10", '15': "mut11", '16': "mut12", '18': "unsorted"}
    for fileName in glob.glob("mutantDistributions-alwaysNOTSpliced/*.txt"):
        file = open(fileName, "r")
        binName = binTranslate[fileName.split("-")[1].split("/")[1]]
        binNames.append(binName)

        for line in file:
            data = line.split()
            mutant = data[2].split("-")[1]
            freq = int(data[0])
            mutants[mutant][binName] += freq

    row_labels = mutants.keys()
    column_labels = binNames

    print row_labels
    print column_labels
    data = []
    for mutant in row_labels:
        data_line = []
        for bin in column_labels:
            data_line.append(mutants[mutant][bin])
        print mutant, data_line
        data.append(data_line)

    for line in data:
        for el in line[:-1]:
            heatmapData.write(str(el) + ",")
        heatmapData.write(str(el) + "\n")
    heatmapData.close()

    data = np.array(data)
    #print data
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
    plt.yticks(range(len(row_labels)))
    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels, fontsize=10)
    print row_labels
    plt.savefig("mutantsPerBins_backgroundsin11and12.png")
main()
