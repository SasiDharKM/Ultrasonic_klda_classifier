import numpy as np
import matplotlib.pyplot as plt
import mlpy
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as KLDA

def main():
    data = np.loadtxt('../Flowmeters/Meter B')
    print data.shape
    N, m = data.shape
    m -= 1
    X = data[:, :m]
    y = data[:, m]
    classes = np.unique(y)
    k = len(classes)
    print X.shape, y.shape
    print classes

    kld = KLDA(n_components=2)
    Xkl = kld.fit_transform(X, y)
    print Xkl.shape, y.shape

if __name__ == '__main__':
    main()
