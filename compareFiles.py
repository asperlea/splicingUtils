__author__ = 'adriana'

from itertools import islice

def main():
    firstFile = open("all_mutated_v2.fa", "r")
    secondFile = open("exons_tab_delim_all_seqs.txt", "r")
    thirdFile = open("exonlibrary.fasta", "r")

    firstSEQS = set()
    secondSEQS = set()
    thirdSEQS = set()
    while True:
        next_4_lines = list(islice(firstFile, 4))
        if not next_4_lines:
            break
        seq = next_4_lines[1].strip().upper() + next_4_lines[2].strip().upper() + next_4_lines[3].strip().upper()
        if len(seq) != 170:
            print "@@@@"
        firstSEQS.add(seq)


    while True:
        next_5_lines = list(islice(thirdFile, 5))
        if not next_5_lines:
            break
        seq = next_5_lines[1].strip().upper() + next_5_lines[2].strip().upper() + next_5_lines[3].strip().upper() + next_5_lines[4].strip().upper()
        seq = seq[15:-15]
        '''
        if len(seq) != 170:
            print "@@@@"
            print next_4_lines[0]
            print seq
        '''
        if next_5_lines[0].find("mut") != -1:
            thirdSEQS.add(seq)

    for line in secondFile:
        ID = line.split()[0]
        seq = line.split()[1][15:-15].upper()

        if len(seq) != 170:
            print "!!!!!", len(seq)
        if ID.find("mut") != -1:
            secondSEQS.add(seq)

    print len(firstSEQS), len(secondSEQS)
    print len(firstSEQS.intersection(secondSEQS))
    print firstSEQS == thirdSEQS
    print secondSEQS == thirdSEQS

main()
