'''
Created on Mar 22, 2016

@author: walter
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from simplex_sampler import *

if __name__ == '__main__':
    
    w = uniform_sampler(2, 100)
    #print w
    ws = ws_transform(w)
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111)
    for i in range(w.shape[0]):
        ax1.scatter(w[i,0], w[i,1], c='r', marker='o')
        
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(111)
    for i in range(ws.shape[0]):
        ax2.scatter(ws[i,0], ws[i,1], c='b', marker='o')        
    
    plt.show()