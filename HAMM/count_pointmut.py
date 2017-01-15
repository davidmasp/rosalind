# script to count point mutations
import argparse
import sys

# args
parser = argparse.ArgumentParser(description='ounter of point mutations')
parser.add_argument('-f','--file', help='Plain sequence file', required=True)
parser.add_argument('-v','--verbose', help='verbose', action="store_true",
        default = False)
args = parser.parse_args()


if args.verbose:
    sys.stderr.write("""This script will count the point mutations present in 
    your sequences. They must be same length.""")
    sys.stderr.write("Reading the file {}".format(args.file))

fh = open(args.file,"r")

# getting the list of sequences
seq = []
seq.append(fh.readline())
seq.append(fh.readline())


fh.close()


if args.verbose:
    sys.stderr.write("Computing the point mutations.")

if len(seq[0])== len(seq[1]):
    i = 0
    count = 0
    while i < len(seq[0]):
        if seq[0][i] != seq[1][i]:
            count = count+1
        i = i +1
    sys.stdout.write("{}".format(count))
else:
    sys.stderr.write("The sequence don't have the sae lenght!")
