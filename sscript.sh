#!/bin/bash
#SBATCH -J TestGPU_KERAS
#SBATCH -o TestGPU_KERAS.%J.stdout
#SBATCH -e TestGPU_KERAS.%J.stderr
#SBATCH --partition gpu
#SBATCH --qos gpu-award
#SBATCH --gres gpu:1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -t 04:00:00
#SBATCH -A gr19002-001

module load python/3.6.6
module load cuda/9.0

#activate the python environment that has tensorflow
source /gpfs/gpfs/project1/gr19002-001/faawork/faa_tf_keras/bin/activate

#ensure you go to the folder for execution of script
cd /gpfs/gpfs/project1/gr19002-001/faawork/testing-elf/
python test_mnist.py
