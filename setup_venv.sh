#!/bin/bash

# Setup script for Photometric Stereo Demo Data project
# This script creates a virtual environment and installs all dependencies

echo "=========================================="
echo "Photometric Stereo - Virtual Environment Setup"
echo "=========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "Python version:"
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
python3 -m venv venv_photometric

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv_photometric/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo ""
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv_photometric/bin/activate"
echo ""
echo "To run Jupyter Notebook:"
echo "  jupyter notebook PhotometricStereo_DemoData.ipynb"
echo ""
echo "To deactivate the virtual environment when done:"
echo "  deactivate"
echo ""
