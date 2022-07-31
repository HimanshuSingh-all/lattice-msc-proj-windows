
""" Firs 6 lines of the datafile:
Created:June-16-2022 
Coverage:20.0 
N:20 
NUM-IONS:80 
NSTEPS:100000 
WRITE-PERIODICITY:100 
"""




#Parser MSD
import collections
from scipy import stats
import matplotlib.pyplot as plt
import glob
import numpy as np
paramlen=6
def getrunparams(fname,paramlen):
    params=dict()    
    with open(fname) as fhand:
        for i,line in enumerate(fhand):
            if i>=paramlen:
                break
            params[line.split(':')[0]]=line.split(':')[1]
    return params

def getnparray(fname,params:dict,paramlen):
    ndarray=np.loadtxt(fname,skiprows=paramlen)
    return ndarray


def ensemble_sqavg(ndarray,fname,paramlen):
    msdpers=list()
    params=getrunparams(fname,paramlen)
    s=int(params['NUM-IONS'])
    NS=int(params['NSTEPS'])
    WP=int(params['WRITE-PERIODICITY'])
    #print(narray.shape[0]/s,":::")
    for i in range(int(NS/WP-1)): #int(NS/WP-1) 
        #print(int(NS/WP-1))
        #msdpers.append(np.mean( (ndarray[s*(1+i):(i+2)*s,0]-ndarray[s*i:s*(i+1),0])**2+(ndarray[s*(1+i):(i+2)*s,1]-ndarray[s*i:s*(i+1),1])**2))
        msdpers.append(np.mean( np.linalg.norm( (ndarray[s*(1+i):(i+2)*s]-ndarray[0:s])**2,axis=1 )))
    return msdpers


def time_msd(traj,fname,paramlen):
    #traj: a numpy iXD
    
    params=getrunparams(fname,paramlen)
    mea=list()
    s=int(params['NUM-IONS'])
    NS=int(params['NSTEPS'])
    WP=int(params['WRITE-PERIODICITY'])
    tau=NS/(4*WP)
    for n in range(1,N):
        disp_sq_comp=(traj[n*s::]-traj[:-n*s:s])*(traj[n*s::]-traj[:-n*s:s]) #traj[:-n:,1:] means that we slice till (lastelement-n)th element  
        print(disp_sq_comp,":\n",traj[n::,1:],":\n",traj[:-n:,1:])
        disp=np.sum(disp_sq_comp,axis=1) 
        
        MSD=np.mean(disp)
        print(MSD)
        mea.append(MSD)
    return mea