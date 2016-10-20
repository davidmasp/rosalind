#!/usr/local/bin/python3

# imports
import sys


#clases
class Sequence(object):
	"""Class to store sequences Sequence"""
	def __init__(self,id,seq):
		self.id = id.lstrip(">")
		self.seq = "".join(seq).upper()
	def get_GC(self):
		nC = self.seq.count("C")
		nG = self.seq.count("G")

		total = len(self.seq)

		return((nC+nG)/total)
	def get_id(self):
		return(str(self.id))


#functions
def fasta_iterator(filename):
	fh = open(filename,"r")
	seq = []
	ident = "0"
	for i in fh:
		line = i.strip("\n")
		if line.startswith(">"):
			if (ident != "0"):
				yield Sequence(ident,seq)
			ident = line
			seq = []
		else:
			seq.append(line)
	yield Sequence(ident,seq)
	fh.close()




filename = sys.argv[1]



values = {}
for i in fasta_iterator(filename):
	values[i.get_id()] = i.get_GC()


r = sorted(values.items(), key=lambda x: x[1], reverse=True)[0]

sys.stdout.write("{}\n{}\n".format(r[0],r[1]*100))
		








