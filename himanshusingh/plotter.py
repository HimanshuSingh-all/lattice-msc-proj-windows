import numpy as np 
import matplotlib.pyplot as plt
import glob
from scipy import stats
# Data2/msdvs-N{0}-cov{1:.2f}-mcsteps{2}.txt
N=20
mcsteps=[100,200,500,1000]
#mcsteps=[100,200,300,400,500,600,700,800,900,1000]
cover=np.arange(10,100)
cover=cover/100
d=dict() 

def msdvsteps(mcstep:int, cov):
    x=np.arange(0,mcstep+1)
    msdvs=np.loadtxt("Data2/msdvs-N{0}-cov{1:.2f}-mcsteps{2}.txt".format(N,cov,mcstep))

    plt.scatter(x,msdvs,label="Coverage: {}".format(cov),alpha=0.6)
    plt.xlabel("Steps")
    plt.ylabel("Mean Square Displacement")
    plt.title("MSD vs Steps")
    plt.legend()



def getdvs(mcsteps:list,cover):
    pass

def dvscov(mcstep:int, cover,name):
    x=np.arange(0,mcstep+1)
    mv=list()
    bv=list()
    for cov in cover:    
        msdvs=np.loadtxt("Data2/msdvs-N{0}-cov{1:.2f}-mcsteps{2}.txt".format(N,cov,mcstep))
        m=stats.linregress(x,msdvs)[0]
        b=stats.linregress(x,msdvs)[1]
        mv.append(m)
        bv.append(b)
    plt.figure(dpi=200,facecolor='white')
    ax=plt.axes()
    ax.set_facecolor("gainsboro")

    ax.scatter(cover,np.array(mv)/4,color='mediumblue',alpha=0.6)
    ax.grid(color='white', linestyle='-.')

    ax.set_xlabel(r"Coverage$\to$")
    ax.set_ylabel(r"Diffusivity(D) $\to$")

    ax.set_title("Diffusivity vs Coverage")
    plt.savefig("Plots/{}.png".format(name),bbox_inches='tight')
    return mv,bv
    """
    for steps in mcsteps:
        x=np.arange(0,steps+1)
        dvs=list()
        i=0
        for cov in cover:    
            msdvs=np.loadtxt("Data2/msdvs-N{0}-cov{1:.2f}-mcsteps{2}.txt".format(N,cov,steps))
            dvs.append(stats.linregress(x,msdvs)[0])   
        d[steps]=np.array(dvs)
    with plt.xkcd():
        for steps in mcsteps:
            plt.scatter(cover,d[steps],label="Max Steps: {}".format(steps),alpha=0.8)
        #plt.scatter(cover,d[steps],alpha=0.8)
        plt.title("Diffusivity vs Steps", fontsize = 25)
        plt.xlabel(r"Coverage$\to$")
        plt.ylabel(r"Diffusion Coefficient (D)$\to$")
        plt.legend(loc=1, prop={'size': 6})
        #plt.grid(color='black')
        plt.savefig("Plots/{}.png".format(name),bbox_inches='tight')
        plt.show()
        """
"""
cover=[0.2,0.5,0.7,0.9]
[msdvsteps(100,cov) for cov in cover]
plt.savefig("Plots/MSDvsMCS-100step.png",bbox_inches='tight')
"""
def fitplot(mv,bv,name,mcstep,step):
    x=np.arange(0,mcstep+1)
    plt.figure(dpi=200,facecolor='white')
    ax=plt.axes()
    for i in range(0,cover.shape[0],step):    
        msdvs=np.loadtxt("Data2/msdvs-N{0}-cov{1:.2f}-mcsteps{2}.txt".format(N,cover[i],mcstep))
        
        ax.set_facecolor("gainsboro")

        p=ax.scatter(x,msdvs,alpha=0.6,label='Coverage: {}'.format(cover[i]))
        ax.plot(x,mv[i]*x+bv[i])
        ax.grid(color='white', linestyle='-.')

        ax.set_xlabel(r"Step $\to$")
        ax.set_ylabel(r"MSD $\to$")

        ax.set_title("Diffusivity vs Coverage")
    plt.savefig("Plots/{}.png".format(name),bbox_inches='tight')
            
name="DvsCov(100steps)"
mv,bv=dvscov(100, cover,name)
plt.show()
print(mv)
name="MSDVSTEP-100STEPS_1"
fitplot(mv,bv,name,100,25)
plt.legend()
plt.show()



