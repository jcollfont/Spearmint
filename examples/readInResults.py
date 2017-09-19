
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import os

###Settings for toy experiment
path = '/Users/jaume/Documents/Research/Spearmint/results/toy_all/output_repeat_'

numRepeats = 60
numFiles = 130
funcEvals = ['\'c2\'','\'c1\'','\'f\'']
#funcEvals = ['\'c1\'','\'f\'']

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
    
    print 'Repeat: ' + str(rep)
    
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
            
            text = f.readline()
            locked = text.find('Completed successfully')
            while  (locked < 0) & (text != ''):
                text = f.readline()
                locked = text.find('Completed successfully')
#                print text
#                print locked
#                
#            print text
            if text != '':
                s = text 
                for fcn in funcEvals:
                    
                    if s.find(fcn) >=0:
                        s = s[s.find(fcn):]
#                        print 'String is: ' + s
                        
                        if (fcn == funcEvals[0]):
                            c2value[rep,fileIx] = float(s[s.find('[')+1:s.find(']')])
                        elif (fcn == funcEvals[1]):
                            c1value[rep,fileIx] = float(s[s.find('[')+1:s.find(']')])
                        elif (fcn == funcEvals[2]):
                            fvalue[rep,fileIx] = float(s[s.find('[')+1:s.find(']')])
                        
                fileIx = fileIx+1
        
                #    print '\n'
            
            f.close()
            
fvalue = fvalue[:,:100]
c1value = c1value[:,:100]
c2value = c2value[:,:100]
    
for rep in range(numRepeats):
    
    validSol = (c1value[rep,:]>=0)&(c2value[rep,:]>=0)
    
    print 'Minimum: ' + str( np.min(fvalue[rep,validSol]) )
    
    plt.plot(fvalue[rep,validSol], label= 'f' + str(rep))
    #plt.plot(c1value, label='c1')
    #plt.plot(c2value, label='c2')
    plt.legend();

scipy.io.savemat('/Users/jaume//Desktop/toyExample.mat', mdict={'fval': fvalue, 'c1': c1value, 'c2': c2value})



#
#for rep in range(numRepeats):
#    
#    validSol = (c1value[rep,:]>=0)
#    
#    print 'Minimum: ' + str( np.min(fvalue[rep,validSol]) )
#    
#    plt.plot(fvalue[rep,validSol], label= 'f' + str(rep))
#    #plt.plot(c1value, label='c1')
#    #plt.plot(c2value, label='c2')
#    plt.legend();
#
#scipy.io.savemat('/Users/jaume//Desktop/simpleExample2.mat', mdict={'fval': fvalue, 'c1': c1value})

