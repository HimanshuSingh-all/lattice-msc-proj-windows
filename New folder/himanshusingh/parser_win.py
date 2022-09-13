import glob
from PARSER_MSD import ensemble_sqavg,getnparray ,getrunparams, time_msd 
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats 
width = 0.35
paramlen=6
run=dict()
Ns=100000
w=100
for i,dire in enumerate(sorted(glob.glob('simdata\\Simrun-?'))):
    names=glob.glob(f'{dire}\\*.txt')#COVERAGE-*-NSTEPS*-*
    #print(i,'\n',names)
    MSDS_=dict()
    WP=0
    NSTEPS=0
    D=list()
    for fname in names:
        params=getrunparams(fname,paramlen)
        narray=getnparray(fname,params,paramlen)
        WP=int(params['WRITE-PERIODICITY'].split()[0])
        NSTEPS=int(params['NSTEPS'].split()[0])
        MSDS_[int(float(params['Coverage'].split()[0]))]=np.array(time_msd(narray,fname,paramlen))
        STEPNO=np.arange(WP,NSTEPS,WP)   
        D.append(stats.linregress(STEPNO,MSDS_[int(float(params['Coverage'].split()[0]))]).slope/4.0)
    run[i]=D
#plt.plot(MSDS_[10],label=f"Coverage:{10}",marker='o',linestyle=None)
#STEPNO=np.arange(WP,NSTEPS,WP)
#label=['10','20','30','40','50','60','70','80','90']
x=np.arange(w,Ns,w)
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Diffusivity')
ax.set_xlabel('Coverage')
ax.set_title('Diffusivity vs Coverage')
ax.set_xticks(x, label)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.savefig('DvCov.png',bbox_inches='tight')
plt.show()