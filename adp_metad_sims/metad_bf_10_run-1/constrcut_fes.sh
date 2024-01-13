#!/bin/bash
source ./plumed_source_script.sh

# command
plumed sum_hills --hills run_ala2_metad_sigma0.3_height1.2_pace500_bf10.hills.dat --kt 0.596161 --min -pi,-pi --max pi,pi --bin 100,100 --outfile 2d_fe_phi_psi_sum_hill_bf10_nbins_100.txt --mintozero


