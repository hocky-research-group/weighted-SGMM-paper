#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=3GB
#SBATCH --time=30:00

input=$1

# run notebook
bash /scratch/projects/hockygroup/ss12902/posLDA_actin/cluster_opes_data_from_triasha/run_with_v1.6.1/wrapped_trajs_for_actin/launch_container.sh $input

