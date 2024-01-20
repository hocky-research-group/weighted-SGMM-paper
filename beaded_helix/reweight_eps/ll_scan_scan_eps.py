#!/usr/bin/env python
# coding: utf-8

# ## Load Libraries

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import MDAnalysis as md
from shapeGMMTorch import torch_sgmm
from shapeGMMTorch import scripts
import torch
# ignore warnings
import warnings
warnings.filterwarnings('ignore')


# ## Read Trajectory

# In[ ]:


prmtopFileName = "../helix_template.pdb"
trajFileName = "../run_files/helix_folding_eps6.0.dcd"
coord = md.Universe(prmtopFileName,trajFileName)
print("Number of atoms in trajectory:", coord.atoms.n_atoms)
print("Number of frames in trajectory:", coord.trajectory.n_frames)
# make atom selection
atomSel = coord.select_atoms('all')
print("Number of atoms in selection:", atomSel.n_atoms)
# create traj data of selection
traj_data = np.empty((coord.trajectory.n_frames,atomSel.n_atoms,3),dtype=float)
#loop traj
for ts in coord.trajectory:
    traj_data[ts.frame,:] = atomSel.positions


# ## Scan epsilon

# In[ ]:


eps_range = np.array([1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18])
cluster_array = np.arange(1,7).astype(int)
dtype = torch.float64
device = torch.device("cuda:0")
for eps in eps_range:
    print("epsilon = ", eps)
    file_name = "eps" + str(eps) + "_frame_weights.dat"
    frame_weights = np.loadtxt(file_name)
    eps_train, eps_cv = scripts.cross_validate_cluster_scan(traj_data, 90000, frame_weights = frame_weights, covar_type="kronecker", cluster_array = cluster_array, n_training_sets=3, n_attempts = 10, dtype=dtype, device=device)
    train_file_name = "eps" + str(eps) + "frame_weights_ll_train_90k.dat"
    np.savetxt(train_file_name, eps_train)
    cv_file_name = "eps" + str(eps) + "frame_weights_ll_cv_10k.dat"
    np.savetxt(cv_file_name, eps_cv)

