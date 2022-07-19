import numpy as np
from datetime import date
np.random.seed()

class ion:
    def __init__(self,i:int,pos:tuple):
        self.i=i        #assign an index to the ion
        self.pos=pos    #pos (y,x) of the ion in the space (which will be later mapped on the lattice)
        self.init=pos   #init position of ion in space 



class lat_2d:

    def __init__(self,N:int,coverage:float):
        if coverage>1:
            print("Coverage Cannot be greater than 1")
            raise ValueError
        self.N=N
        self.cov=coverage
        self.ions=list()        

    def get_lattice_2d(self):
        A=np.array([(i,j) for i in range(self.N) for j in range(self.N)])
        B=np.arange(0,self.N**2)
        ionc=list()                                                             #contains the intial position of all the occupying lattice ions
        choice=np.random.choice(B,int(self.cov*self.N*self.N),replace=False)
        lattice=np.zeros((self.N,self.N))
        for b in choice:
            lattice[ tuple(A[b]) ]=1 
            ionc.append(tuple(A[b]))    
        return (lattice, ionc)


    def init_lattice(self):
        self.lattice,self.ionpos=self.get_lattice_2d()
        for i,posn in enumerate(self.ionpos):
            self.ions.append(ion(i,posn))
            

    def mappostolat(self,s,i:int):
        """
        Args:
        s(2-D numpy vector): the random next step (coordination number 4)
        i(int): index of the ion lattice ion
        Returns:
        2-tuple of indices for the mapped position of ion onto the lattice if that step is taken
        """
        if s is None:
            s=np.array((0,0))
        nextstep=np.array(self.ions[i].pos)+s
        return tuple(nextstep%self.N)
        

    def oneionstep(self,i):
        
        MOVES=[(1,0),(0,1),(-1,0),(0,-1)]
        s=np.array(MOVES[np.random.choice([0,1,2,3])]) # s is an array but class.pos is a tuple, so we add them by converting pos into ndarray and then revert it back to tuple
       # print("U: ",s, i)
        
        #applying periodic boundary 
        #TODO:check if this implementation works
        
        latposn=self.mappostolat(s,i)

        if self.lattice[latposn]!=1: #if there is no ion in the step chosen
            self.lattice[self.mappostolat(None,i)]=0 #vacate teh current position in the lattice   
            self.ions[i].pos=tuple(np.array(self.ions[i].pos)+s) #update the ion position
            self.lattice[latposn]=1 #update the new filled position
        
        return None

    def onemcstep(self):
        if len(self.ions)!=0:
            [self.oneionstep(i) for i in range(len(self.ions))]
        else:
            self.init_lattice()
            self.onemcstep()
      
    def sqdisp(self):
        disp=np.zeros_like(self.ions)
        for i,io in enumerate(self.ions):
            disp[i]=np.linalg.norm((np.array(io.pos)-np.array(io.init)))**2
            #print("posn: ",(np.array(io.pos)-np.array(io.init)),":",np.linalg.norm((np.array(io.pos)-np.array(io.init))))
        return disp
write=0
N=20
NSTEPS=100000
WT=100
today=date.today()
coverage=[10.0,20.0,30.0,40.0,50.0,60.0,70.0,80.0,90.0]
for cov in coverage:
    day=today.strftime("%B-%d-%Y")
    fname=f"simdata\\Simrun-2\\Coverage-{cov}-NSTEPS{NSTEPS}-{day}.txt"
    with open(fname,'w+') as fhand: 
        mylat=lat_2d(N,cov/100)
        mylat.init_lattice()
        NIONS=len(mylat.ions)
        fhand.write(f"Created:{day} \n")
        fhand.write(f"Coverage:{cov} \n")
        fhand.write(f"N:{N} \n")
        fhand.write(f"NUM-IONS:{NIONS} \n")
        fhand.write(f"NSTEPS:{NSTEPS} \n")
        fhand.write(f"WRITE-PERIODICITY:{WT} \n")
        for i,step in enumerate(range(NSTEPS)):
            mylat.onemcstep()
            if i%WT==0:
                for io in mylat.ions:
                    fhand.write(f"{io.pos[0]}  {io.pos[1]} \n")


