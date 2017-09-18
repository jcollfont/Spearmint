
import numpy as np

def main(job_id, params):
  x1 = params['x']
  x2 = params['y']

  f  = x1 + x2**2 + 0.5
  c1 = x1 - 0.5

  return {'f':f, 'c1':c1}


"""
Everything below this point is optional. It is used to specify
the true solution so that one can plot the error curve using
progress_curve.py in the visualizations/ directory.
"""
def true_val():
    return 0.5
def true_sol():
    return {'x' : 0, 'y' : 0}
true_func = main
