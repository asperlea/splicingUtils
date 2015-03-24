__author__ = 'adriana'

import sys

def main():
    if len(sys.argv) < 2:
        print "Program requires path to directory containing file hg38.phyloP7way.wigFix"
        exit(0)
    dirname = sys.argv[1]
    if dirname[-1] != '/':
        dirname += '/'
    allChrs = open(dirname + "hg38.phyloP7way.wigFix", "r")
    # allChrs file has a bunch of lines that look like this that signal beginning of new chromosomes:
    # fixedStep chrom=chr12_GL877876v1_alt start=1 step=1
    # and we need to split them up by chrom name
    chrFile = None
    lastChrom = ""
    for line in allChrs:
        if line.find("fixedStep") != -1:
            data = line.split()
            chromosome = data[1].split('=')[1]
            start = data[2].split('=')[1]

            if (chromosome != lastChrom):
                if chrFile != None:
                    chrFile.close()
                print "Creating ", dirname + chromosome + ".phyloP7way.wigFix"
                chrFile = open(dirname + chromosome + ".phyloP7way.wigFix", "w")
            lastChrom = chromosome
        chrFile.write(line)

main()

