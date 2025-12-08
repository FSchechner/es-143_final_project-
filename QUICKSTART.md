# Quick Start Guide

## 🚀 Get Started in 4 Steps

### 1. Setup (First Time Only)

Open Terminal and run:

```bash
cd /Users/maiaposternack/Desktop/cs/es-143_final_project-
chmod +x setup_venv.sh
./setup_venv.sh
```

### 2. Register Jupyter Kernel (First Time Only)

```bash
source venv_photometric/bin/activate
python -m ipykernel install --user --name=venv_photometric --display-name "Python (Photometric Stereo)"
```

### 3. Run Jupyter Notebook

```bash
source venv_photometric/bin/activate
jupyter notebook
```

### 4. Select Kernel and Run

- Click on `PhotometricStereo_DemoData.ipynb` in the browser
- **IMPORTANT**: Go to **Kernel → Change Kernel → Python (Photometric Stereo)**
- Run cells with **Shift + Enter**

---

## 📋 Every Time You Work

```bash
# Navigate to project
cd /Users/maiaposternack/Desktop/cs/es-143_final_project-

# Activate environment
source venv_photometric/bin/activate

# Start Jupyter
jupyter notebook

# When done, deactivate
deactivate
```

---

## ✅ Verify Installation

After setup, check everything is installed:

```bash
source venv_photometric/bin/activate
python -c "import numpy, cv2, matplotlib, plotly, gdown; print('✓ All packages installed!')"
```

---

## 🆘 Common Issues

**"Permission denied"**
```bash
chmod +x setup_venv.sh
```

**"python3 not found"**
- Install Python from python.org

**Jupyter won't start**
```bash
python -m jupyter notebook
```

---

## 📁 What You'll Have

```
es-143_final_project-/
├── PhotometricStereo_DemoData.ipynb  ← Your main notebook
├── requirements.txt                   ← Dependencies
├── venv_photometric/                 ← Virtual environment
└── data/                             ← Your data
```

That's it! 🎉
