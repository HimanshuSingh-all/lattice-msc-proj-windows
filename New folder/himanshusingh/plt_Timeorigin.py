import glob
from PARSER_MSD import ensemble_sqavg,getnparray ,getrunparams, time_msd 
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 
width = 0.35
paramlen=6
Ns=100000
w=100
"""
    MSDS_=dict()
    WP=0
    NSTEPS=0
    D=list()
"""
MSDS_=[]
for i,dire in enumerate(sorted(glob.glob('simdata\\Simrun-1'))):
    names=glob.glob(f'{dire}\\*.txt')#COVERAGE-*-NSTEPS*-*
    #print(i,'\n',names)
    for fname in names:
        params=getrunparams(fname,paramlen)
        narray=getnparray(fname,params,paramlen)
        MSDS_[int(float(params['Coverage'].split()[0]))]=np.array(time_msd(narray,fname,paramlen))
        STEPNO=np.arange(w,Ns,w)   
        plt.plot(STEPNO,MSDS_,label=params['Coverage'].split()[0])
        #D.append(stats.linregress(STEPNO,MSDS_[int(float(params['Coverage'].split()[0]))]).slope/4.0)
#    run[i]=D
plt.legend()
plt.show()
#plt.plot(MSDS_[10],label=f"Coverage:{10}",marker='o',linestyle=None)
