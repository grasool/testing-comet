#!/bin/bash
#SBATCH -N 1
#SBATCH -p gpu-shared
#SBATCH --gres= gpu:4
#SBATCH -t 2:00
#SBATCH --ntasks-per-node 24
module load singularity
singularity exec /oasis/scratch/comet/mkandes/temp_project/singularity/images/tensorflow-gpu.img python test_mnist.py
