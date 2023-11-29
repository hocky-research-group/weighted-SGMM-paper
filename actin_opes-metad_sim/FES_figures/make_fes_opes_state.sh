#!/bin/bash 

inp_file=$1
out_file=$2
f_name=../FES_from_State.py


#-----++++few notes++++-------#
# --cv is not available here 
# --sigma not needed
# --der option not supported with periodic CVs

# command line
python $f_name --temp 310.0 --state $inp_file --min ' -41.0,-3.14' --max 41.0,3.14 --bin 99,100 --outfile $out_file

#python $f_name --kt 2.577483 --state state_copy.data --all_stored --outfile fe_hlda_state.dat --der 

