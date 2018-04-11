import numpy as np
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fname", help="file name containing data to be prepared", default="../Flowmeters/Meter A")
parser.add_argument("-s", "--sname", help="file name to write prepared data to", default="../Flowmeters/rA")
args = parser.parse_args()
X = np.loadtxt(args.fname)
np.savetxt(args.sname, X, delimiter=' ')
