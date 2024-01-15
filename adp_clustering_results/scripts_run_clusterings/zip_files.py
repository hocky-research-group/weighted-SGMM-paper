import numpy as np
import os 
num_runs = 4
num_weights = 4
pwd = os.getcwd()


## zip the pickled objects only 
"""
for i in range(num_runs):
    for j in range(num_weights):
        dir_name = "r%d/w%d/"%(i+1,j)
        os.chdir(dir_name)
        os.system("zip obj_files_r%d_w%d.zip *.pickle"%(i+1,j))
        os.chdir(pwd)
"""

init = "run_ala2_metad_sigma0.3_height1.2_pace500_bf10"
## zip the simulation files only
for i in range(num_runs):
    dir_name = "r%d/"%(i+1)
    os.chdir(dir_name)
    cmd_line = "zip sim_files_r%d.zip %s.colvars.dat %s.plumed.dat %s.cpt %s.gro %s.hills.dat %s_prev.cpt %s.log %s.edr plumed_reweight.dat colvar_reweight 2d_fe_phi_psi_sum_hill_bf10_nbins_100.txt constrcut_fes.sh adp.tpr"%(i+1, init, init, init, init, init, init, init, init)
    os.system(cmd_line)
    os.chdir(pwd)
