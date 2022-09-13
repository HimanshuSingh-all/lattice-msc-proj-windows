import numpy as np
def time_msd(traj):
    #traj: a numpy iXD
    N=traj.shape[0]
    mea=list()
    for n in range(1,N):
        print(n)
        disp_sq_comp=(traj[n::,1:]-traj[:-n:,1:])*(traj[n::,1:]-traj[:-n:,1:])#
        print(disp_sq_comp,":\n",traj[n::,1:],":\n",traj[:-n:,1:])
        disp=np.sum(disp_sq_comp,axis=1)
        MSD=np.mean(disp)
        print(MSD)
        mea.append(MSD)
    return mea

fname="singleparticletraj.txt"

traj=np.loadtxt(fname)
msdvtlag=time_msd(traj)
print(traj)
import matplotlib.pyplot as plt
from scipy import stats
N=traj.shape[0]
y=np.arange(1,N)
res=stats.linregress(y,msdvtlag)
print("The Diffusion Constant is: ",res.slope/4.0)
plt.plot(y,msdvtlag,'r*',markersize=7)
plt.plot(y,res.slope*y+res.intercept,color='red',markersize=7,linestyle='dashed')
plt.xlabel(" Time Lag (psec) ")
plt.ylabel(" MSD (Angstrom sq.) ")
plt.title("MSD vs Time Lag for Single Particle")
plt.grid()
plt.show()