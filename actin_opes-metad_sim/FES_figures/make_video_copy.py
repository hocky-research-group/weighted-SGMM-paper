# Importing libraries
import numpy as np
import os
import cv2   # pip install opencv-python
import glob
import matplotlib.pyplot as plt


# function for sorting all the image files in a particular order
def sort_img_files(e):
    #key = int(e.split("_")[1].split("ns")[0])
    key = int(e.split("_")[1].split(".")[0][:-2:])
    return key

# Input parameters
fps = 4
each_frame_time = 1

"""
nbins_cleft_dist = 351 
nbins_dihedral = 350
dt = 0.002    # in ps

# function for sorting all the grid files in a particular order
def sort_files(e):
    key = int(e.split("/")[2].split(".")[2])
    return key

# loadinfg files 
files = sorted([f for f in glob.glob("../1/*grid*") if not f.split("/")[2].startswith('bck')], key=sort_files)
times = [int(f.split("/")[2].split(".")[2])*dt*1e-3 for f in files]

print(len(files))
print(times)

for i in range(len(files)):
    print(files[i])

entire_data_set = []
for i in range(len(files)):
    metad_bias = np.loadtxt(files[i], usecols=2, unpack=True, dtype=float)
    metad_bias = metad_bias.reshape((nbins_cleft_dist, nbins_dihedral), order='F').T
    entire_data_set.append(metad_bias)

    plt.figure()
    plt.xlabel("Cleft Width [angstroms]", fontsize=12)
    plt.ylabel("Dihedral [degrees]", fontsize=12)
    plt.ylim(-50,15)
    plt.xlim(17,32)
    plt.title('Time= '+str(round(times[i]))+"ns", fontsize=12)
    plt.imshow(metad_bias.max()-metad_bias, origin='lower', extent=(15,40,-180,180), aspect='auto', animated=True, cmap='gnuplot')
    cbar = plt.colorbar()
    cbar.set_label("FE (kcal/mol)", fontsize=12)
    plt.clim(0,20)
    plt.savefig("fes_"+str(round(times[i]))+"ns.png")
    print(i+1)

entire_data_set = np.array(entire_data_set)
print(entire_data_set.shape)
np.save('entire_metad_bias_set_copy.npy', entire_data_set)
"""

img_files = sorted(glob.glob("fig_*ns.png"), key=sort_img_files)
for i in range(len(img_files)):
    print(img_files[i])

frame_array= []

for i in range(len(img_files)):
    img = cv2.imread(img_files[i])
    height, width, layers = img.shape
    size = (width, height) 

    for t in range(each_frame_time):
        frame_array.append(img)

out = cv2.VideoWriter('fes_video_copy.avi', cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
#out = cv2.VideoWriter('fes_video_copy.avi', cv2.VideoWriter_fourcc(*'mp4v'), fps, (4,3))

for i in range(len(frame_array)):
    out.write(frame_array[i])
out.release()
























