"""
Function to implement KLDA on a given dataset

Steps
1. Load the dataset
2. Calculate the Gram Matrix for the given dataset
3. Calculate the sw_inverse and sb for G
4. Obtain n largest eigen values, and corresponding eigen vectors
5. Transform the input data
"""
import mlpy
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def plot_eigs(ev, inds):
    """
    A Function to plot the eigen values in descending order
    """
    num_vals = len(ev)
    plt.scatter([i+1 for i in range(num_vals)], ev[inds], color='b')
    plt.savefig('../res_imgs/eig_A_gauss_sig2.png')
    plt.show()

def klda(X, y):
    """
    Function to reduce the dimensions of the given X values
    X : features
    y : labels
    """
    num_classes = len(np.unique(y))

    # Calculate the number of entries for each class
    _, n = np.unique(y, return_counts=True)
    for i in range(num_classes):
        print n[i],

    total_n = np.sum(n)
    # X is a N*m matrix
    N = X.shape[0]
    m = X.shape[1]

    # Obtain all the indices that contain each class separately
    class_indices = []
    for c in np.unique(y):
        class_indices.append(np.where(y==c))

    # Calculate the number of entries for each class
    _, nrs = np.unique(y, return_counts=True)

    # Inner product matrix is K
    # It is N*N matrix, i.e., (n1+n2+n3)*(n1+n2+n3)
    # K = X.dot(X.T)
    G = mlpy.kernel_gaussian(X, X, sigma=2.0)

    #G = np.matmul(X, X.T)

    c_list = []

    k = 0

    for i in range(num_classes):

        c_temp = G[:, k:k+n[i]]

        k += n[i]

        c_list.append(c_temp)

    #print c1.shape, c2.shape, c3.shape

    sb = np.zeros([total_n, total_n], np.float32)

    sw = np.zeros([total_n, total_n], np.float32)


    means = []

    for i in range(num_classes):
        means.append(np.reshape(np.sum(c_list[i], 1) / n[i], (total_n, 1)))

    mean_overall = np.zeros((total_n, 1), np.float32)

    for i in means:

        mean_overall += i

    mean_overall /= num_classes

    print '\n'

    print num_classes

    print np.sum(mean_overall)

    for i in range(num_classes):    
        sb += n[i] * np.matmul(means[i] - mean_overall, (means[i] - mean_overall).T)

    for i in range(num_classes):
        for j in range(n[i]):

            sw += np.matmul(c_list[i][:,j] - means[i], (c_list[i][:,j] - means[i]).T)

    
    print np.sum(sw)

    print np.sum(sb)

    
    sw_inv_sb = np.matmul(np.linalg.pinv(sw), sb)

    eig_vals, eig_vecs = np.linalg.eig(sw_inv_sb)

    indices = np.argsort(eig_vals)[::-1]
    plot_eigs(eig_vals, indices)

    to_red = 1

    indices = indices[:to_red]

    eig_vecs = eig_vecs[indices]

    w = np.reshape(eig_vecs[0], (total_n, 1))

    for i in range(1, to_red):

        w = np.concatenate((w, np.reshape((eig_vecs[i]), (total_n, 1))), axis=1)

    print w.shape

    return np.matmul(w.T, G)

def main():
    # Load the data
    data = np.loadtxt('../Flowmeters/Meter A')
    N, m = data.shape
    m -= 1
    X = data[:, :m]
    y = data[:, m]
    classes = np.unique(y)
    k = len(classes)
    print X.shape, y.shape
    print classes
    redX = klda(X, y).T.astype(np.float32)
    redData = np.concatenate((redX, np.reshape(y, (N, 1))), axis=1)
    np.savetxt('../reduced_data/A_1_gauss_e', redData)

if __name__ == '__main__':
    main()