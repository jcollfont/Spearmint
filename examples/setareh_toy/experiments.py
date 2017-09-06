#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:38:41 2017

@author: jaume
"""


import numpy as np
import scipy as sp
import toy as bb_fcn

# load initial points
inputs = sp.io.loadmat('/Users/jaume/Documents/Research/Spearmint/examples/setareh_toy/InitialData.mat')

initialPts = inputs['X_in']
N = initialPts.shape[0]

params = {'x':0.0 , 'y':0.0}
for n in range(N):
    
    # assign values
    params['x'] = initialPts[n,0]
    params['y'] = initialPts[n,1]
    
    # sample
    evals = bb_fcn.main(1,params)
    
    # plot
    print( evals['f'])
#    print(["C1: " + evals['c1']])
#    print(["C2: " + evals['c2']])