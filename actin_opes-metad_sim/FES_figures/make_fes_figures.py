import numpy as np
import matplotlib.pyplot as plt
import os

"""
# generate the FES
for i in range(21):
    time = (i+1)*50
    inp_file = "state_%dns"%time
    out_file = "fes_%dns"%time
    os.system("./make_fes_opes_state.sh %s %s"%(inp_file, out_file))
"""

ld1_grids = np.linspace(-41.0, 41.0, 100, endpoint=True)
dihedral_grids = np.linspace(-np.pi, np.pi, 100, endpoint=True)

# load the FEs and make plots
for i in range(21):
    time = (i+1)*50
    fes_i = np.loadtxt("fes_%dns"%time, usecols=2).reshape([100,100])/4.184  # conver to kcal/mol unit
    plt.figure(figsize=(4,3))
    plt.title("Time = %dns"%time)
    plt.ylim(-50.0,10.0)
    plt.xlabel("LD 1")
    plt.ylabel("Dihedral")
    plt.contourf(ld1_grids, dihedral_grids*180/3.14, fes_i, cmap="jet", levels=50, vmin=0.0, vmax=20.0)
    cbar = plt.colorbar()
    cbar.set_label("FE (kcal/mol)")
    plt.tight_layout()
    plt.savefig("fig_%dns.png"%time)
