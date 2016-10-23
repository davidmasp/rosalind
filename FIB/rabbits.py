#!/usr/local/bin/python3

## imports
import sys
import argparse


parser = argparse.ArgumentParser(
     prog='fyboRabbits',
     formatter_class=argparse.RawDescriptionHelpFormatter,
     description='''\
         This is a rabbit generator for rosalind problem.
         ''')

parser.add_argument('-n', dest='n',
                    type = int,
                    help='Get the number of months')

parser.add_argument('-k', dest='k',
                    type = int,
                    help='Get the number of months')

parser.add_argument('-r', '--recursive',dest='r', action='store_true',
                    help='Tag to use the recursive approach')

#parser.add_argument('-dr', '--dynrec',dest='dr', action='store_true',
#                    help='Tag to use the dynamic recursive approach')

parser.add_argument('-b', '--bench',dest='b', action='store_true',
                    help='Tag to benchmark the available methods')


args = parser.parse_args()





## functions

def fiborabbits_recursive(n,k):
	if n==0:
		return 0
	if n==1:
		return 1
	else:
		return fiborabbits_recursive(n-1,k) + fiborabbits_recursive(n-2,k) * k



def fiborabits_dynamic_iterative(n,k):
	# step 1 : create the dict
	fib = {}
	fib[0] = 0
	fib[1] = 1
	#step 2 loop
	i = 2
	while i < n+1:
		fib[i] = fib[i-1] + fib[i-2] * k
		i = i + 1
	#step 3 get the value
	return fib[n]


if args.b:
	from timeit import Timer
	time_r = Timer("fiborabbits_recursive({0},{1})".format(args.n,args.k),
		"from __main__ import fiborabbits_recursive")
	time_dy = Timer("fiborabits_dynamic_iterative({0},{1})".format(args.n,args.k),
		"from __main__ import fiborabits_dynamic_iterative")
	sys.stdout.write("Recursive approach: {0}\nDynamic approach: {1}\n".format(time_r.timeit(number=100),
		time_dy.timeit(number=100)))
else:
	if args.r:
		res = fiborabbits_recursive(args.n,args.k)
	else:
		res = fiborabits_dynamic_iterative(args.n,args.k)
	sys.stdout.write("{}\n".format(res))

