__author__ = 'adriana'

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from itertools import islice

binList = ["mut2", "mut6", "mut5", "mut8", "mut9", "mut10", "mut11", "mut12"] # mutant

f_j = [0.1460297264, 0.09276502227, 0.1159755557, 0.05147186398, 0.03581824841, 0.1537023114, 0.09926165828, 0.09509764232] # mutant

'''
Example of lines in countsPerbin_mut.txt
AAAAATTAGTGTGTAATCTCATTCTTAACCCTGTCTCTGTGCAGTCTTGGAAGTGGATCCTTGCACCGGTCATTCTTTATATCTGTGAAAGGATCCTCCGGTTTTACCGCTCCCAGCAGAAGGTTGTGATTACCAAGGTAAAGAATATGCACTTTCCTCTTGCTGTGATA >ENSE00001607924-cnsrv_1nt
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.434622576663538e-05]
'''

def main():
    dataFile = open("countsPerbin_mut.txt", "r")
    natFile = open("natBehavior_mut.txt", "w")
    numBins = 8
    a_ID_mut = defaultdict(lambda: defaultdict(list))
    mutset = set()
    nonat = 0
    while True:
        next_2_lines = list(islice(dataFile, 2))
        if not next_2_lines:
            break

        ID = next_2_lines[0].strip().split(" ")[1].split("-")[0]
        mut = next_2_lines[0].strip().split(" ")[1].split("-")[1]
        counts = next_2_lines[1].strip("[]\n").split(", ")

        a_i = []
        total_in_all_bins = 0
        for j in range(numBins):
            total_in_all_bins += (float(counts[j]) * (f_j[j]))
        if total_in_all_bins != 0:
            for j in range(numBins):
                a_i.append(float(counts[j]) * f_j[j] / total_in_all_bins)
        a_ID_mut[ID][mut] = a_i
        if mut != "nat":
            mutset.add(mut)

    # One file and one heatmap for each Ensembl ID
    for ID in a_ID_mut.keys():
        print "ID = ", ID

        #background should be at the top
        if a_ID_mut[ID]["nat"] != []:
            dir = ""
            if (a_ID_mut[ID]["nat"][0] > 0.9) or (a_ID_mut[ID]["nat"][1] > 0.9):
                dir = "26bins"
            elif (a_ID_mut[ID]["nat"][2] > 0.9) or (a_ID_mut[ID]["nat"][3] > 0.9) or (a_ID_mut[ID]["nat"][4] > 0.9):
                dir = "589bins"
            elif (a_ID_mut[ID]["nat"][5]) > 0.9 or (a_ID_mut[ID]["nat"][6] > 0.9) or (a_ID_mut[ID]["nat"][7] > 0.9):
                dir = "101112bins"
            else:
                dir = "other"

            matrix = open("mutantHeatMaps-sorted/" + dir + "/" + ID + ".txt", "w")
            data = []
            rowlabels = []
            matrix.write("nat")
            natFile.write(ID)
            for el in a_ID_mut[ID]["nat"]:
                matrix.write("," + str(el))
                natFile.write("," + str(el))
            matrix.write("\n")
            natFile.write("\n")
            data.append(a_ID_mut[ID]["nat"])
            rowlabels = ["nat"]

            # rest of the mutants
            for mut in sorted(mutset):
                if mut in a_ID_mut[ID]:
                    matrix.write(mut)
                    for el in a_ID_mut[ID][mut]:
                        matrix.write("," + str(el))
                    matrix.write("\n")
                    data.append(a_ID_mut[ID][mut])
                    rowlabels.append(mut)

            matrix.close()
            data = np.array(data)
            fig, ax = plt.subplots()
            heatmap = ax.pcolor(data, cmap=plt.cm.Blues)
            plt.yticks(range(len(rowlabels)))
            ax.set_xticklabels(binList)
            ax.set_yticklabels(rowlabels, fontsize=10)
            plt.savefig("mutantHeatMaps-sorted/" + dir + "/" + ID + ".png")
            plt.close()
        else:
            print "Had no nat."
            nonat += 1

    print nonat, " no naturals."

main()