#!/bin/bash
#SBATCH -N 1
#SBATCH -p gpu-shared
#SBATCH --gres=gpu:p100:2
#SBATCH -t 2:00
#SBATCH --ntasks-per-node 14
module load singularity
singularity exec ../i-my-tensorflow-gpu-py3.simg python test_mnist.py
