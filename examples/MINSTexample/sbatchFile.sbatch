#! /bin/bash

# set a job name
#SBATCH --job-name=NN_BO
##############
# set output
#SBATCH --output=/home/jcollfont/tmp/mdcs-test_$8.out
###########
# error dump
#SBATCH --error=/home/jcollfont/tmp/mdcs-test_$8.err
###########
# number of tsasks
#SBATCH --exclusive
##############
# partition
###############
# num nodes qwith 1 GPU and 32 cpu
#SBATCH -N 1
#SBATCH -p par-gpu
#SBATCH -n 32

python /home/jcollfont/Documents/Research/Spearmint/examples/MINSTexample/MINST_keras_remote.py -dIn $1 -dHi $2 -mo $3 -wD $4 -wM $5 -lr $6 -dr $7 -jobID $8
