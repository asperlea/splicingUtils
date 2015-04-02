'''
Quick script for printing the distribution of natural background sequences in the bins of the mutant library.
'''

__author__ = 'adriana'

from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np

def main():
    heatmapData = open("backgroundsPerbin_mut.txt", "r")
    binNames = ["9", "10", "11", "12", "13", "14", "15", "16"]

    column_labels = binNames
    row_labels = []
    data = []
    for line in heatmapData:
        splitLine = line.strip().split()
        ID = splitLine[0]
        counts = [float(splitLine[i]) for i in range(1, len(splitLine))]
        row_labels.append(ID)
        data.append(counts)
    print row_labels
    data = np.array(data)
    #print data
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
    ax.set_xticklabels(column_labels)
    #ax.set_yticklabels(row_labels)
    plt.savefig("backgroundsPerBins.png")
main()
