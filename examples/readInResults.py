
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import os

###Settings for toy experiment
path = '/Users/jaume/Documents/Research/Spearmint/examples/toy/output_repeat_'

numRepeats = 30
numFiles = 110
funcEvals = ['\'c2\'','\'c1\'','\'f\'']

###Settings for simpleExp2
#path = '/Users/jaume/Documents/Research/Spearmint/examples/simpleExp2/output_repeat_'
#
#numRepeats = 100
#numFiles = 100
#funcEvals = ['\'c1\'','\'f\'']

fvalue = -1*np.ones([numRepeats,numFiles])
c1value = -1*np.ones([numRepeats,numFiles])
c2value = -1*np.ones([numRepeats,numFiles])

for rep in range(numRepeats):
    
    fileIx = 0
    for nn in range(numFiles):
    
        if nn < 9:
            fileName = '0000000'+ str(nn+1) +'.out'
        elif (nn < 99)&(nn >= 9):
            fileName = '000000'+ str(nn+1) +'.out'
        else:
            fileName = '00000'+ str(nn+1) + '.out'
        
#        print 'Loading file: ' + fileName
        fname = path + str(rep) + '/' + fileName
        
        if os.path.isfile(fname):
            f = open( fname ,'r')
            
            if f.readline().find('Job launching') >= 0:
                text = []
                for ii in range(10):
                    text.append(f.readline())
            #        print text[ii]
                    
#                print text[4]
                
                s = text[4]
                
                for fcn in funcEvals:
                    s = s[s.find(fcn):]
            #        print 'String is: ' + s
                    
                    if fcn == funcEvals[0]:
                        c2value[rep,fileIx] = float(s[s.find('[')+1:s.find(']')])
                    elif fcn == funcEvals[1]:
                        c1value[rep,fileIx] = float(s[s.find('[')+1:s.find(']')])
                    elif fcn == funcEvals[2]:
                        fvalue[rep,fileIx] = float(s[s.find('[')+1:s.find(']')])
                        
                fileIx = fileIx+1
    
            #    print '\n'
            
            f.close()
            
fvalue = fvalue[:,:(fileIx-1)]
c1value = c1value[:,:fileIx-1]
c2value = c2value[:,:fileIx-1]
    
for rep in range(numRepeats):
    
    validSol = (c1value[rep,:]>=0)&(c2value[rep,:]>=0)
    
    print 'Minimum: ' + str( np.min(fvalue[rep,validSol]) )
    
    plt.plot(fvalue[rep,validSol], label= 'f' + str(rep))
    #plt.plot(c1value, label='c1')
    #plt.plot(c2value, label='c2')
    plt.legend();

scipy.io.savemat('/Users/jaume//Desktop/toyExample.mat', mdict={'fval': fvalue, 'c1': c1value, 'c2': c2value})

