'''
Created on Mar 22, 2016

@author: walter
'''

import numpy as np

def uniform_sampler(dim, num):
    weights = np.zeros((num,dim), np.float)
    for i in range(num):
        x = np.zeros(dim)
        sum = 0.0
        for j in range(dim):
            x[j] = np.random.uniform(0.0,1.0)
            sum += x[j]
        for j in range(dim):
            weights[i,j] = x[j]/sum
    
    return weights

def sort_interval_sampler(dim, num):
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