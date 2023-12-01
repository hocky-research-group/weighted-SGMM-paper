#!/bin/bash

source ./plumed_source_script.sh

# print the value of temp in energy units/ kt
plumed kt --temp 300 --units kcal/mol

# actual one
plumed sum_hills --hills run_ala2_metad_sigma0.3_height1.2_pace500.hills.dat --kt 0.596161 --min -pi,-pi --max pi,pi --bin 32,32 --outfile 2d_fe_phi_psi_sum_hill.txt --mintozero


# deposit FE vs. CV after addition every 5000 gaussian hills
#plumed sum_hills --hills ../HILLS --stride 10000 --outfile myfes_ --mintozero --kt 2.577483 
#plumed sum_hills --hills ../HILLS --stride 5000 --outfile myfes_ --mintozero --kt 2.577483


# generating histogram data
#plumed sum_hills --histo ../COLVAR --idw cleft_dist,dihedral --sigma 0.025,0.025 --kt 2.577483 --mintozero

