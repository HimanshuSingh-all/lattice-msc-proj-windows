import glob
from PARSER_MSD import ensemble_sqavg,getnparray ,getrunparams, time_msd 
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 
width = 0.35
paramlen=7
equilibriation=50000
Ns=100000
wp=100
"""
    MSDS_=dict()
    WP=0
    NSTEPS=0
    D=list()
"""
MSDS_=dict()
for i,dire in enumerate(sorted(glob.glob('simdata\\Simrun-3'))):
    names=glob.glob(f'{dire}\\*.txt')#COVERAGE-*-NSTEPS*-*
    #print(i,'\n',names)
    for fname in names:
        params=getrunparams(fname,paramlen)
        narray=getnparray(fname,params,paramlen)
        MSDS_[int(float(params['Coverage'].split()[0]))]=np.array(time_msd(narray,fname,paramlen))
STEPNO=np.arange(equilibriation+wp,Ns//4+1*wp,wp)   
        #D.append(stats.linregress(STEPNO,MSDS_[int(float(params['Coverage'].split()[0]))]).slope/4.0)
#    run[i]=D
print("stepno:", STEPNO.shape)

for key,value in MSDS_.items():
    print(key)
    plt.plot(STEPNO,value,label=f'Coverage:{key}'.split()[0],linestyle='--')
plt.xlabel(r'Time Step $\to$')
plt.title('MSD(Time Origin) vs Time Step')
plt.ylabel(r'MSD $\to$')
plt.legend()
plt.grid()
plt.show()
plt.savefig('DvsCov.png',bbox_inches='tight')
#plt.plot(MSDS_[10],label=f"Coverage:{10}",marker='o',linestyle=None)
