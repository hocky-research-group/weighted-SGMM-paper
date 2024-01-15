#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:1
#SBATCH --mem=10GB
#SBATCH --time=24:00:00

input=$1

# run notebook
bash test-launch-papermill.sh $input
