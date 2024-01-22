import numpy as np
import os 

n_frames = 191
n_restarts = 4

count = 0
parent_dir = "/scratch/projects/hockygroup/ss12902/posLDA_actin/cluster_opes_data_from_triasha/run_with_v1.6.1/wrapped_trajs_for_actin"
for i in range(n_frames):
    #for j in range(n_restarts):
    for j in range(2, n_restarts):
        new_dir =  "frame%d/%d"%(i,j+1)
        path = os.path.join(parent_dir, new_dir)
        os.makedirs(path)
        os.system("cp get_calphas.py %s"%new_dir)
        os.system("cp submit_job.sbatch %s"%new_dir)
        os.chdir(path)
        os.system("sbatch --job-name f%d_r%d -o f%d_r%d.log submit_job.sbatch "%(i,j+1,i,j+1)+'"python get_calphas.py %d %d"'%(i,j+1))
        #os.system("python get_calphas.py %d %d"%(i, j+1))
        os.chdir(parent_dir)
        count += 1 
        print(count)
