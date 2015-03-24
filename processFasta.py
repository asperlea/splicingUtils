from collections import defaultdict
import sys

def main():
    muts = open(sys.argv[1], "r")
    ofile = open(sys.argv[2], "w")
    seenIDs = defaultdict(int)
    for line in muts:
        if line[0] == '>':
            data = line.split()
            seenIDs[data[0]] += 1
            newID = data[0] + "-" + str(seenIDs[data[0]])
            data[0] = newID
            ofile.write(" ".join(data) + "\n")
        else:
            ofile.write(line)
    ofile.close()

main()