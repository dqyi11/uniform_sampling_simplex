'''
Created on Mar 22, 2016

@author: walter
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from simplex_sampler import *

if __name__ == '__main__':
    
    w = sort_interval_sampler(3, 100)
    print w
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(w.shape[0]):
        ax.scatter(w[i,0], w[i,1], w[i,2], c='r', marker='o')
    
    plt.show()