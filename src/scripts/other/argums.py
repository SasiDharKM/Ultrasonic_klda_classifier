"""
A script to obtain command line arguments and work on them
"""
import argparse
parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number",
                    type=int)
parser.add_argument("-v", "--verbosity", help="increase output verbosity", type=int, choices=[0, 1, 2])
args = parser.parse_args()
# print args.echo
answer = args.square**2
if args.verbosity == 2:
    print "the square of {} equals {}".format(args.square, answer)
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print answer