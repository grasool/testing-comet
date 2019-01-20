#!/bin/bash
#SBATCH -N 1
#SBATCH -p gpu-shared
#SBATCH --gres=gpu:p100:2
#SBATCH -t 2:00
#SBATCH --ntasks-per-node 14
module load singularity
singularity exec /oasis/scratch/comet/mkandes/temp_project/singularity/images/keras-tensorflow-gpu.img python test_mnist.py
