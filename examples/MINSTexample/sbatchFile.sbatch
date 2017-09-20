#! /bin/bash

# set a job name
#SBATCH --job-name=NN_BO
##############
# set output
#SBATCH --output=/home/jcollfont/tmp/mdcs-test_1.out
###########
# error dump
#SBATCH --error=/home/jcollfont/tmp/mdcs-test_1.err
###########
# number of tsasks
#SBATCH --exclusive
##############
# partition
###############
# num nodes
#SBATCH -N 1

python /home/jcollfont/Documents/Research/Spearmint/examples/MINSTexample/MINST_keras_remote.py '-dIn' 0.2 '-dHi' 0.2 '-mo' 0.0 '-wD' 0.0 '-wM' 10
