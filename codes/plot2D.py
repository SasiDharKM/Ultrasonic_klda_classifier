import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def main():
    # Load the data
    data = np.loadtxt('../reduced_data/adi_2d_A')
    X, y = data[:, :2], data[:, 2]
    colors = ['r', 'b']
    classes, Ns = np.unique(y, return_counts=True)
    k = len(classes)

    s = 0
    for i in range(k):
        plt.scatter(X[s:s+Ns[i]][:, 0], X[s:s+Ns[i]][:, 1], color=colors[i])
        s += Ns[i]
    plt.savefig('../res_imgs/dat_A_line_2.png')
    plt.show()

if __name__ == '__main__':
    main()