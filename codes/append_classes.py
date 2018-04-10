import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def main():
    # Load the data
    data = np.loadtxt('../reduced_data/adi_A_5')
    N, m = data.shape
    Ns = [35, 52]
    y = []
    for i in range(1, len(Ns)+1):
        # print i
        for j in range(Ns[i-1]):
            y.append(i)
    y = np.array(y)
    data = np.concatenate((data, np.reshape(y, (N, 1))), axis=1)
    print data.shape, y.shape

if __name__ == '__main__':
    main()