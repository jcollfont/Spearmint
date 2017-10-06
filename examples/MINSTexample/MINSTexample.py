# The toy problem in http://arxiv.org/abs/1403.4890

#import sys
#import os
#import numpy as np
#sys.path.insert(0, '/Users/jaume/Documents/Research/Spearmint/examples/MINSTexample/')
#import json
#import time
#
#
#
#def main(job_id, params):
#
#    dropout_In = float(params['dropout_In'])
#    dropout_Hi = float(params['dropout_Hi'])
#    momentum = float(params['momentum'])
#    weightDecay = float(params['weightDecay'])
#    maxWeight = float(params['maxWeight'])
#    learningRate = float(params['learningRate'])
#    decayRate = float(params['decayRate'])
#
#    # setup command
#    paramsSTR = " " + str(dropout_In) + " " + str(dropout_Hi) +  " " + str(momentum) + "  " + str(weightDecay) +  "  " + str(maxWeight) + "  " + str(learningRate)  + "  " + str(decayRate) + " " + str(job_id)
#                
#    command = "sbatch " + "/home/jcollfont/Documents/Research/Spearmint/examples/MINSTexample/sbatchFile.sbatch "
#
#    # Connect to server and send request
#    os.system("ssh -f jcollfont@discovery2.neu.edu " + command + paramsSTR)
#    
#    # wait until file exists
#    waiting = 1
#    while waiting:
#            waiting = os.system("scp jcollfont@discovery2.neu.edu:/home/jcollfont/output.json  ./")
#            time.sleep(10*60)
#            
#    os.system("ssh -f jcollfont@discovery2.neu.edu " + "rm /home/jcollfont/output.json")
#    
#    # read in results
#    f = open('./output.json','r')
#    outputSTR =  json.loads(f.readline())
#    f.close()
#    
#    
#    f  = np.array([-outputSTR['f'][1]])
#    c1 = np.array([outputSTR['c']])
#
#    return {'f': f, 'c1': c1}

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
                                      dropout_In, dropout_Hi, 
                                      momentum, 10**weightDecay, 
                                      maxWeight, 10**learningRate, 
                                      10**decayRate)
    
    f  = np.array([output['f']])
    c1 = np.array([output['c']])

    return {'f': f, 'c1': c1}
