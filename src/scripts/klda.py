"""
Function to implement KLDA on a given dataset

Steps
1. Load the dataset
2. Calculate the Gram Matrix for the given dataset
3. Calculate the sw_inverse and sb for G
4. Obtain n largest eigen values, and corresponding eigen vectors
5. Transform the input data
"""
import numpy as np
import matplotlib.pyplot as plt
import mlpy
import argparse

plt.style.use('ggplot')

def plot_eigs(ev, inds, img_f):
    """
    A Function to plot the eigen values in descending order
    """
    num_vals = len(ev)
    plt.scatter([i+1 for i in range(num_vals)], ev[inds], color='b')
    plt.savefig(img_f)
    plt.show()

def klda(X, y, img_f):
    """
    Function to reduce the data and give the reduced transformation matrix
    X - The original dimensional data
    y - The labels
    @returns the dimnsionally reduced data
    """
    k = len(np.unique(y))

    # Calculate the number of entries for each class
    _, Ns = np.unique(y, return_counts=True)
    N, m = X.shape

    # Obtain all the indices that contain each class separately
    class_indices = []
    for c in np.unique(y):
        class_indices.append(np.where(y==c))

    # Calculate the Gram matrix after the Kernel Trick
    G = mlpy.kernel_gaussian(X, X, sigma=2.0)
    # print G.shape

    # Separate the k classes into k different matrices
    # Each entry in the c_list is N*nk
    c_list = []
    te = 0
    for i in range(k):
        c_temp = G[:, te:te+Ns[i]]
        te += Ns[i]
        c_list.append(c_temp)

    # Initialize the between class scatter matrix and the within class scatter matrix
    sb = np.zeros([N, N], np.float32)
    sw = np.zeros([N, N], np.float32)

    # Calculate the mean of each class
    # Each mean vector is N*1
    means = []
    for i in range(k):
        ci = np.sum(c_list[i], 1) / Ns[i]
        ci = np.reshape(ci, (N, 1))
        means.append(ci)
    
    # Calculate the mean of means
    # The mean of means is also a N*1 vector
    mean_overall = np.zeros((N, 1), np.float32)
    for meani in means:
        mean_overall +=  meani
    mean_overall /= k

    # Calculate sb
    for i in range(k):
        sb += Ns[i] * np.matmul((means[i] - mean_overall), (means[i] - mean_overall).T)
    
    # Calculate sw
    for j in range(k):
        for i in range(Ns[j]):
            sw += np.matmul((c_list[j][:, i] - means[j]), (c_list[j][:, i] - means[j]).T)

    # Calculate the eigen values and sorted eigen vectors of sw_inv_sb
    sw_inv_sb = np.matmul(np.linalg.pinv(sw), sb)
    eig_vals, eig_vecs = np.linalg.eig(sw_inv_sb)
    indices = np.argsort(eig_vals)[::-1]
    plot_eigs(eig_vals, indices, img_f)

    # Reduce the data
    # Choose the dimension to reduce to after analyzing the plot of eigen values
    to_red = 1
    indices = indices[:to_red]
    eig_vecs = eig_vecs[indices]
    W = np.reshape(eig_vecs[0], (N, 1))
    for i in range(1, to_red):
        W = np.concatenate((W, np.reshape(eig_vecs[i], (N,1))), axis=1)
    # print W.shape
    return np.matmul(W.T, G)

def main():
    """
    The main method
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--fname", help="file name containing data", default="../Flowmeters/Meter A")
    parser.add_argument("-s", "--sname", help="file name to save reduced data to", default="../reduced_data/A_1_gauss")
    parser.add_argument("-i", "--iname", help="file name to save image to", default="../res_imgs/def.png")
    args = parser.parse_args()
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
    redX = klda(X, y, args.iname).astype(np.float32)
    redData = np.concatenate((redX.T, np.reshape(y, (N, 1))), axis=1)
    np.savetxt(args.sname, redData)

if __name__ == '__main__':
    main()
