# The toy problem in http://arxiv.org/abs/1403.4890

import sys
import os
import numpy as np
sys.path.insert(0, '/Users/jaume/Documents/Research/Spearmint/examples/MINSTexample/')
import MINST_keras_remote as testEx


dataset = testEx.setTestandTrain()

def main(job_id, params):

    dropout_In = float(params['dropout_In'])
    dropout_Hi = float(params['dropout_Hi'])
    momentum = float(params['momentum'])
    weightDecay = float(params['weightDecay'])
    maxWeight = float(params['maxWeight'])
    learningRate = float(params['learningRate'])
    decayRate = float(params['decayRate'])


    output = testEx.run_MINST_example(dataset, 
                                      10**dropout_In, 10**dropout_Hi, 
                                      10**momentum, 10**weightDecay, 
                                      maxWeight, 10**learningRate, 
                                      10**decayRate)
    
    f  = np.array([-output['f'][1]])
    c1 = np.array([output['c']])

    return {'f': f, 'c1': c1}


# def main2(job_id, params):
#
#     momentum = params['momentum']
#
#
#     output = testEx.run_MINST_example(dataset,0.2,0.2,momentum[0], 0.0, 10.)
#     f  = np.array([-output['f'][1]])
#     c1 = np.array([output['c']])
#
#     return {'f': f, 'c1': c1}
