# The toy problem in http://arxiv.org/abs/1403.4890
import numpy as np

def main(job_id, params):
  x1 = params['x']
  x2 = params['y']
  
  f = np.sin(x1) + x2
  c1 = np.sin(x1)*np.sin(x2) + 0.95
  
  c1 = -c1
  
  return {'f':f, 'c1':c1}


#"""
#Everything below this point is optional. It is used to specify
#the true solution so that one can plot the error curve using 
#progress_curve.py in the visualizations/ directory.
#"""
#def true_val():
#    return 0
#def true_sol():
#    return {'x' : 0, 'y' : 0}
#true_func = main    
