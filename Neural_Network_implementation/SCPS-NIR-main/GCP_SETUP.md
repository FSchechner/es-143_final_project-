# Running SCPS-NIR on Google Cloud GPU

## Step 1: Create GPU VM

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to **Compute Engine** > **VM Instances**
3. Click **Create Instance**

**Configuration:**
- **Name**: `scps-nir-training`
- **Region**: Choose one with GPU availability (e.g., `us-central1`)
- **Machine type**: `n1-standard-4` (4 vCPUs, 15 GB RAM)
- **GPU**: Click "Add GPU"
  - Type: `NVIDIA T4` (cheapest, ~$0.35/hour)
  - Number: 1
- **Boot disk**:
  - OS: `Ubuntu 20.04 LTS`
  - Size: `50 GB`
- **Firewall**: Check "Allow HTTP/HTTPS traffic"

**Cost estimate**: ~$0.50/hour total

## Step 2: Connect to VM

```bash
# From Google Cloud Console, click "SSH" button
# Or use gcloud CLI:
gcloud compute ssh scps-nir-training --zone=us-central1-a
```

## Step 3: Clone Repository

```bash
cd ~
git clone https://github.com/FSchechner/es-143_final_project-.git
cd es-143_final_project-/Neural_Network_implementation/SCPS-NIR-main
```

## Step 4: Run Setup Script

```bash
chmod +x setup_gcp.sh
./setup_gcp.sh
```

This will:
- Install Miniconda
- Create conda environment with GPU support
- Verify NVIDIA GPU is detected

## Step 5: Start Training

```bash
# Make training script executable
chmod +x train_gpu.sh

# Train on shoe dataset (runs in background)
./train_gpu.sh shoe

# Or train on cat dataset
./train_gpu.sh cat
```

## Step 6: Monitor Training

```bash
# View live training log
tail -f training_shoe_*.log

# Check GPU usage
nvidia-smi

# View TensorBoard
tensorboard --logdir runs/shoe/ --bind_all
# Then visit: http://[VM_EXTERNAL_IP]:6006
```

## Step 7: Download Results

When training completes:

```bash
# From your local machine
gcloud compute scp --recurse scps-nir-training:~/es-143_final_project-/Neural_Network_implementation/SCPS-NIR-main/runs/shoe ./results_shoe
```

Or download directly from the VM using SFTP.

## Step 8: Stop VM (Important!)

**Don't forget to stop the VM when done to avoid charges!**

```bash
# From Google Cloud Console: Click "Stop" on the VM
# Or use gcloud:
gcloud compute instances stop scps-nir-training --zone=us-central1-a
```

## Estimated Training Time

- **On CPU (Mac)**: ~24 hours for 2000 epochs
- **On GPU (T4)**: ~2-4 hours for 2000 epochs
- **On GPU (V100)**: ~1-2 hours for 2000 epochs

## Cost Estimate

- **T4 GPU**: ~$0.35/hour
- **VM (n1-standard-4)**: ~$0.15/hour
- **Total**: ~$0.50/hour

**Example**: 3 hours of training = $1.50

## Troubleshooting

**GPU not detected:**
```bash
nvidia-smi
# If this fails, GPU drivers aren't installed
# Reinstall with: sudo apt-get install nvidia-driver-525
```

**Out of memory:**
- Reduce batch_size in config file
- Or upgrade to larger GPU (V100)

**Training interrupted:**
```bash
# Resume from checkpoint
python train.py --config configs/shoe.yml --resume runs/shoe/checkpoint_500.pth
```
