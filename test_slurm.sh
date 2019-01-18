#!/bin/bash
#SBATCH -N 1
#SBATCH -p GPU-small
#SBATCH --gres=gpu:p100:2
#SBATCH -t 5:00
#SBATCH --ntasks-per-node 28
module load keras/2.2.0_tf1.7_py3_gpu
python test_mnist.py
