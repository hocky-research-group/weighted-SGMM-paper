import sys
import numpy as np
import MDAnalysis as md
import MDAnalysis.transformations as trans

frame_num = int(sys.argv[1])
rst_num = int(sys.argv[2])

prmtopFileName = "/scratch/projects/hockygroup/ss12902/posLDA_actin/cluster_opes_data_from_triasha/run_with_v1.6.1/run_with_1us_data/actin-gatpu_ionized_npt_20ns_every50ps-g5.1.4_5mus.tpr"

trr_file = "/scratch/projects/hockygroup/gmh4/projects/gmm_clustering/weighted_gmm/actin_clustering_generate_frames/prod_continue_310K/every5ps_trr/frame%d/%d/actin_gatpu-opes-restart_every5ns_%d_fulltrr_s%d_every5ps.run.500000.trr"%(frame_num, rst_num, frame_num, rst_num)

colvar_file = "/scratch/projects/hockygroup/gmh4/projects/gmm_clustering/weighted_gmm/actin_clustering_generate_frames/prod_continue_310K/every5ps_trr/frame%d/%d/COLVAR"%(frame_num, rst_num)

coord = md.Universe(prmtopFileName, trr_file)
protein = coord.select_atoms("resid 1 to 375")
alpha_carbons = coord.select_atoms("name CA")

# define the transformations (unwraping followed by placing the protein in center of the box)
transforms = [trans.unwrap(protein), trans.center_in_box(protein, center="geometry")]
# do it on-the-fly for all frames in one go
coord.trajectory.add_transformations(*transforms)

positions = coord.trajectory.timeseries(alpha_carbons)
positions -= positions.mean(axis=1, keepdims=True)
np.save("frame%d_%d_positions.npy"%(frame_num, rst_num), positions)

colvar = np.loadtxt(colvar_file, usecols=(1,2,3,4))[::5]
np.savetxt("frame%d_%d_colvar.txt"%(frame_num, rst_num), colvar)

