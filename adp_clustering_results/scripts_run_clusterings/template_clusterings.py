#!/usr/bin/env python
# coding: utf-8

# ## Import

# In[ ]:


import sys
import numpy as np
from shapeGMMTorch import scripts
import MDAnalysis as md
import torch
import pickle


# ## inputs

# In[ ]:


#! 0 means uniform, 3 is meta.bias, 4 is meta.rbias, -1 means use meta.fbias from colvar_reweight file
#col_indx = sys.argv[1]  # 0,3,4,-1
col_indx = int(sys.argv[1])  # 0,3,4,-1
data_path = sys.argv[2] # location from where to read traj, colvar, gro etc.
out_path = sys.argv[3]   # output path


# ## parameters

# In[ ]:


gro_file = "run_ala2_metad_sigma0.3_height1.2_pace500_bf10.gro"
traj_file = "run_ala2_metad_sigma0.3_height1.2_pace500_bf10_wrapped.trr"
colvar_file = "run_ala2_metad_sigma0.3_height1.2_pace500_bf10.colvars.dat"


# ## Load trajectory

# In[ ]:


bb_selection = "(name C and resid 1) or (name C CA N and resid 2) or (name N and resid 3)"

# load data
prmtopFileName =  data_path + gro_file
trajFile = data_path+traj_file

coord = md.Universe(prmtopFileName,trajFile)
sel_bb = coord.select_atoms(bb_selection)

trajData = np.empty((coord.trajectory.n_frames,sel_bb.n_atoms,3),dtype=float)
count = 0

for ts in coord.trajectory:
    trajData[count,:,:] = sel_bb.positions - sel_bb.center_of_geometry()
    count += 1


# ## load bias and calculate the weights

# In[ ]:


kt = 0.596161 # in kcal/mol @ 300K

# uniform case
if col_indx == 0:
    pass

# fbias case
elif col_indx == -1:
    
    bias = np.loadtxt(data_path+"colvar_reweight", usecols=3)
    bias -= bias.min()  # subtract the minimum only for fbias 
    
    weights = np.exp(bias/kt)
    weights /= np.sum(weights)

# bias or rbias case
else:

    bias = np.loadtxt(data_path+colvar_file, usecols=col_indx)
    
    weights = np.exp(bias/kt)
    weights /= np.sum(weights)


# ## run clusterings for different sizes

# In[ ]:


cluster_sizes = np.arange(2,7)

for size in cluster_sizes:
    
    # for uniform
    if col_indx == 0:
        wsgmm = scripts.sgmm_fit_with_attempts(trajData, size, 40, device=torch.device("cuda:0"), dtype=torch.float64)
    
    # for other cases
    else:
        wsgmm = scripts.sgmm_fit_with_attempts(trajData, size, 40, frame_weights=weights, device=torch.device("cuda:0"), dtype=torch.float64)
    
    with open(out_path+"wsgmm_%dstate_nattempts_40.pickle"%size, "wb") as fo:
        pickle.dump(wsgmm, fo)

