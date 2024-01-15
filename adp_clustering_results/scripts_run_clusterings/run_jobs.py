import numpy as np
import os

num_runs = 4
num_weights = 4 # [uniform, bias, rbias, fbias]
col_indx_list = [0, 3, 4, -1]

# loop over runs
for i in range(num_runs):
    input_ = "r%d/"%(i+1)

    # loop over weights
    for j in range(num_weights):

        dir_name = "r%d/w%d/"%(i+1,j)
        line_ = "python template_clusterings.py %d %s %s"%(col_indx_list[j], input_, dir_name) 
        
        if os.path.isdir(dir_name):
            print(dir_name+" directory exists!\n")
        else:
            os.mkdir(dir_name)
            os.system("sbatch --job-name r%d_w%d -o "%(i+1,j)+dir_name+"r%d_w%d.log submit_sep_jobs.sh "%(i+1,j)+'"%s"'%line_)

