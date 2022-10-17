def time_msd(traj):
    #traj: a numpy iXD
    N=traj.shape[0]
    mea=list()
    for n in range(1,N):
        (traj[n::n,1:]-traj[:-n:n,1:])*(traj[n::n,1:]-traj[:-n:n,1:])
