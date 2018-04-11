import time
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fname", help="file name containing data to be classified", default="../Flowmeters/Meter A")
    args = parser.parse_args()
    t0 = time.time()
    is_A = False
    data = np.loadtxt(args.fname)
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
        clf = LogisticRegression(solver='sag', max_iter=20000, multi_class='multinomial', verbose=1, n_jobs=2, tol=1e-6)
    else:
        clf = LogisticRegression(solver='saga', max_iter=20000, verbose=1, n_jobs=2, tol=1e-6)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    scores = cross_val_score(clf, X_train, y_train, cv=5)
    print "Training Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2)
    print "The testing set score for the classification is ", score
    run_time = time.time() - t0
    print "The run time is ", run_time

if __name__ == '__main__':
    np.random.seed(29)
    main()