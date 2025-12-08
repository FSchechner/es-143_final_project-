# Photometric Stereo Demo Data - Setup Instructions

This project performs 3D reconstruction using photometric stereo techniques.

## Prerequisites

- Python 3.8 or higher
- macOS (instructions provided for Mac)

## Quick Setup

### Option 1: Automated Setup (Recommended)

1. Open Terminal and navigate to the project directory:
   ```bash
   cd /Users/maiaposternack/Desktop/cs/es-143_final_project-
   ```

2. Make the setup script executable:
   ```bash
   chmod +x setup_venv.sh
   ```

3. Run the setup script:
   ```bash
   ./setup_venv.sh
   ```

### Option 2: Manual Setup

1. Open Terminal and navigate to the project directory:
   ```bash
   cd /Users/maiaposternack/Desktop/cs/es-143_final_project-
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv_photometric
   ```

3. Activate the virtual environment:
   ```bash
   source venv_photometric/bin/activate
   ```

4. Upgrade pip:
   ```bash
   pip install --upgrade pip
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Notebook

1. Activate the virtual environment (if not already activated):
   ```bash
   source venv_photometric/bin/activate
   ```

2. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. In the browser window that opens, click on `PhotometricStereo_DemoData.ipynb`

4. Run the cells sequentially (Shift + Enter)

## Deactivating the Virtual Environment

When you're done working, deactivate the virtual environment:
```bash
deactivate
```

## Installed Packages

- **numpy**: Numerical computing
- **opencv-python**: Image processing and computer vision
- **matplotlib**: 2D plotting and visualization
- **plotly**: Interactive 3D visualizations
- **gdown**: Download files from Google Drive
- **jupyter**: Jupyter Notebook interface
- **ipykernel**: Jupyter kernel for Python
- **kaleido**: Static image export for Plotly

## Project Structure

```
es-143_final_project-/
├── PhotometricStereo_DemoData.ipynb    # Main notebook
├── PhotometricStereo_Bunny.ipynb       # Bunny dataset notebook
├── requirements.txt                     # Python dependencies
├── setup_venv.sh                       # Automated setup script
├── README_SETUP.md                     # This file
├── venv_photometric/                   # Virtual environment (created after setup)
└── data/                               # Data directory
    └── bunny/                          # Bunny dataset
        ├── frame_*.jpg                 # Image frames
        └── masks/                      # Mask files
            ├── object_mask.png
            ├── probe_mask.png
            └── color_mask.png
```

## Troubleshooting

### Issue: "python3: command not found"
**Solution**: Install Python 3 from [python.org](https://www.python.org/downloads/)

### Issue: "Permission denied" when running setup script
**Solution**: Make the script executable:
```bash
chmod +x setup_venv.sh
```

### Issue: Jupyter Notebook doesn't open
**Solution**: 
1. Make sure the virtual environment is activated
2. Try running: `python -m jupyter notebook`

### Issue: Import errors in notebook
**Solution**: 
1. Verify all packages are installed: `pip list`
2. Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

### Issue: Plotly figures not displaying
**Solution**: 
1. Make sure you're running in Jupyter Notebook (not JupyterLab)
2. Try restarting the kernel: Kernel → Restart

## Additional Notes

- The virtual environment folder `venv_photometric/` should not be committed to git
- Data files are downloaded automatically by the notebook when needed
- First run may take longer due to data downloads

## Contact

For issues or questions about this setup, please refer to the course materials or contact the instructor.
