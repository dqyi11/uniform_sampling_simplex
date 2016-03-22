'''
Created on Mar 22, 2016

@author: walter
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def simplex_sampler(dim, num):
    weights = np.zeros((num,dim), np.float)
    for i in range(num):
        x = []
        x.append(0.0)
        for k in range(dim-1):
            x.append(np.random.uniform(0.0,1.0))
        x.append(1.0)
        x.sort()
        for j in range(dim):
            weights[i, j] = x[j+1] - x[j] 
    
    return weights

if __name__ == '__main__':
    
    w = simplex_sampler(3, 1000)
    print w
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(w.shape[0]):
        ax.scatter(w[i,0], w[i,1], w[i,2], c='r', marker='o')
    
    plt.show()