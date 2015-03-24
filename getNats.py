__author__ = 'adriana'

f = open("uniqPerfects_mut.txt", "r")
for line in f:
    if line.strip().split()[1][-2:] == "-1":
        print line.strip().split()[0]