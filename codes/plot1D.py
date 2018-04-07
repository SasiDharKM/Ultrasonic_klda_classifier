import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def main():
    # Load the data
    data = np.loadtxt('../reduced_data/A_1_poly')
    X, y = data[:, 0], data[:, 1]
    colors = ['r', 'b']
    classes, Ns = np.unique(y, return_counts=True)
    k = len(classes)

    s = 0
    for i in range(k):
        # print X[s:s+Ns[i]].shape, len(range(1, Ns[i]+1))
        plt.scatter(range(s+1, s+Ns[i]+1), X[s:s+Ns[i]], color=colors[i])
        s += Ns[i]
    plt.savefig('../res_imgs/dat_A_poly_1.png')
    plt.show()

if __name__ == '__main__':
    main()