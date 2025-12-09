#!/bin/bash
# Setup script for Google Cloud GPU VM

echo "=== SCPS-NIR GCP Setup ==="

# Update system
echo "Updating system packages..."
sudo apt-get update
sudo apt-get install -y git wget

# Install Miniconda
echo "Installing Miniconda..."
if [ ! -d "$HOME/miniconda3" ]; then
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda3
    rm miniconda.sh
fi

# Initialize conda
echo "Initializing conda..."
eval "$($HOME/miniconda3/bin/conda shell.bash hook)"
conda init bash
source ~/.bashrc

# Create conda environment
echo "Creating conda environment..."
cd ~/es-143_final_project-/Neural_Network_implementation/SCPS-NIR-main
conda env create -f environment_gpu.yml -y

# Verify GPU
echo "Verifying GPU..."
nvidia-smi

echo ""
echo "=== Setup Complete! ==="
echo ""
echo "To activate the environment and start training:"
echo "  conda activate scps_nir"
echo "  cd ~/es-143_final_project-/Neural_Network_implementation/SCPS-NIR-main"
echo "  python train.py --config configs/shoe.yml"
