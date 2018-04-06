import time
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def main():
    t0 = time.time()
    is_A = False
    data = np.loadtxt('../Flowmeters/Meter D')
    print data.shape
    N, m = data.shape
    m -= 1
    X = data[:, :m]
    y = data[:, m]
    classes = np.unique(y)
    k = len(classes)
    print X.shape, y.shape
    print classes

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=36)
    print X_train.shape, y_train.shape
    print X_test.shape, y_test.shape

    if not is_A:
        clf = LogisticRegression(solver='sag', max_iter=10000, multi_class='multinomial', verbose=1)
    else:
        clf = LogisticRegression(solver='saga', max_iter=10000, verbose=1)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print "The score is ", score
    run_time = time.time() - t0
    print "The run time is ", run_time

if __name__ == '__main__':
    print __doc__
    main()