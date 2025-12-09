#!/bin/bash
# Training script for GCP - runs in background with logging

DATASET=${1:-shoe}  # Default to shoe dataset
CONFIG="configs/${DATASET}.yml"
LOG_FILE="training_${DATASET}_$(date +%Y%m%d_%H%M%S).log"

echo "=== Starting SCPS-NIR Training ==="
echo "Dataset: $DATASET"
echo "Config: $CONFIG"
echo "Log file: $LOG_FILE"

# Activate conda environment
eval "$($HOME/miniconda3/bin/conda shell.bash hook)"
conda activate scps_nir

# Run training with nohup (continues after logout)
nohup python train.py --config $CONFIG > $LOG_FILE 2>&1 &

PID=$!
echo "Training started with PID: $PID"
echo "To monitor progress: tail -f $LOG_FILE"
echo "To stop training: kill $PID"
echo ""
echo "Process is running in background. Safe to disconnect."
