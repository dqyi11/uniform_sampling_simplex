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

def ws_transform(weight):
    
    ws_weight = np.zeros(weight.shape, np.float)
    
    num = weight.shape[0]
    dim = weight.shape[1]
    
    for i in range(num):
        w = np.zeros(dim)
        w_t = 0.0
        for j in range(dim):
            w[j] = 1.0 / weight[i,j]
            w_t += w[j]
        for j in range(dim):
            ws_weight[i,j] = w[j] / w_t
    
    return ws_weight
        

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