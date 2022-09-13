import glob
from PARSER_MSD import ensemble_sqavg,getnparray ,getrunparams, time_msd 
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 




width = 0.35
paramlen=6
run=dict()
w=100
fname='Coverage-98-NSTEPS100000-August-18-2022.txt'#'Coverage-90.0-NSTEPS100000-June-16-2022.txt'#
filename=f'simdata\\{fname}'
MSDS_=dict()
WP=0
NSTEPS=0
D=list()
params=getrunparams(filename,paramlen)
narray=getnparray(filename,params,paramlen)
WP=int(params['WRITE-PERIODICITY'].split()[0])
NSTEPS=int(params['NSTEPS'].split()[0])
MSDS_[int(float(params['Coverage'].split()[0]))]=np.array(time_msd(narray,filename,paramlen))
STEPNO=np.arange(WP,NSTEPS,WP)
print(NSTEPS)   
plt.plot(MSDS_[98],label=f"Coverage:{98}",linestyle='-')
x=np.arange(w,NSTEPS,w)
plt.ylabel('MSD')
plt.xlabel('Steps')
plt.title('MSD vs Coverage')
plt.legend()
plt.grid()
plt.show()

plt.tight_layout()

#plt.savefig('DvCov.png',bbox_inches='tight')
