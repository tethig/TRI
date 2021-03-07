#!/usr/bin/env python3

__author__ = "Ben Dickins"
__version__ = "1.0.0"

import re, sys
from itertools import product

if __name__ == "__main__":

    # ask the user for input
    motif_length = int(input("Specify motif length: homo- (1), di- (2), tri- [default=3], tetra- (4)...: ") or 3)
    min_reps = int(input("Minimum number of repeats [default=3]: ") or 3)
    default_name = sys.argv[1].split(".f")[0]
    extension = '.{}mer.{}min.bed'.format(motif_length, min_reps)
    output_name = str(input("Please write name of output file [default={}] ({} will be appended): ".format(default_name, extension))) or default_name

    # the bases
    bases = ['A', 'C', 'G', 'T']

    # helper function for repeat detection
    # acknowledgement: https://stackoverflow.com/a/29489919
    def principal_period(s):
        i = (s+s).find(s, 1, -1)
        return None if i == -1 else s[:i]

    # create repeats from Cartesian product of motif_length number of replicates of the bases
    # deploy helper function to remove motifs with internal repeats
    try:
        motifs = [''.join(x) for x in product(bases, repeat=motif_length) if not principal_period(''.join(x))]
    except:
        print('Error in motif creation. Did you respond to questions properly?')
        sys.exit()

    # read the FASTA file into a variable (seq)
    with open(sys.argv[1], 'r') as fasta:
        all_lines = fasta.readlines()
        sequences, chrom = {}, ''
        for line in all_lines:
            line = line.rstrip()
            if line.startswith('>'):
                chrom = line[1:]
                sequences[chrom] = ''
            else:
                sequences[chrom] += line

    # analyse for repeats
    with open(output_name + extension, 'w') as outfile:
        # loop through each sequence
        for chrom, seq in sequences.items():
            # loop through each motif
            for unit in motifs:
                regex = re.compile("({}){{{},}}".format(unit, min_reps), re.IGNORECASE)
                discovery = [(m.start(), m.end(), unit, int(len(m.group())/motif_length)) for m in re.finditer(regex, seq)] #is list comprehension
                for tup in discovery:
                    print(chrom, "\t", "\t".join([str(t) for t in tup]), "\t+", file=outfile)