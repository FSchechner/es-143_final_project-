# Photometric Stereo - Bunny Reconstruction Setup Guide

## Your Data Structure ✓

```
data/bunny/
├── frame_0001.jpg
├── frame_0003.jpg
├── frame_0005.jpg
├── ... (22 frames total)
└── masks/
    ├── object_mask.png    # Bunny segmentation
    ├── probe_mask.png     # Light probe sphere
    └── color_mask.png     # White balance sheet
```

## Required Imports

```python
import os
from pathlib import Path
import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import ndimage
import glob
```

## Install Missing Packages (if needed)

```bash
.venv/bin/pip install scipy plotly
```

## Key Functions You Need

### 1. Load Images
```python
def load_images_from_folder(image_folder):
    """Load all JPG frames from folder, sorted by frame number."""
    image_files = sorted(glob.glob(os.path.join(image_folder, 'frame_*.jpg')))
    images = []
    for img_path in image_files:
        img = cv2.imread(img_path)
        images.append(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    return np.array(images)
```

### 2. Load Masks
```python
def load_mask(mask_folder, mask_name):
    """Load binary mask (white=object, black=background)."""
    mask_path = os.path.join(mask_folder, mask_name)
    mask_img = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
    mask = (mask_img > 127).astype(np.uint8)
    return mask
```

### 3. Light Direction Calibration
```python
def find_brightest_point(image, center, radius, mask_inner_ratio=0.8):
    """Find brightest point on sphere (specular highlight)."""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cx, cy = center
    H, W = gray.shape
    Y, X = np.ogrid[:H, :W]
    mask = (X - cx) ** 2 + (Y - cy) ** 2 <= (radius * mask_inner_ratio) ** 2
    masked = gray * mask
    coords = np.argwhere(masked == masked.max())
    y_bright, x_bright = coords.mean(axis=0).astype(int)
    return (x_bright, y_bright)

def compute_light_direction_from_sphere(x_bright, y_bright, cx, cy, radius):
    """Calculate 3D light direction from brightest point on sphere."""
    x_star, y_star = x_bright - cx, y_bright - cy
    z_squared = radius**2 - x_star**2 - y_star**2
    z_star = np.sqrt(max(z_squared, 0))
    light_dir = np.array([x_star, y_star, z_star])
    return light_dir / np.linalg.norm(light_dir)
```

### 4. Surface Normal Estimation
```python
def estimate_normals_and_albedo(images, light_directions, mask):
    """Estimate surface normals using photometric stereo."""
    # Solve: I = L @ g, where g = albedo * normal
    # Using least squares: g = (L^T L)^-1 L^T I
    # Returns: normals (H x W x 3), albedo (H x W x 3)
```

### 5. Depth Integration
```python
def frankot_chellappa(normals, mask):
    """Integrate surface normals to depth using Frankot-Chellappa."""
    # Converts normals to depth map using Fourier integration
    # Returns: depth (H x W)
```

## Pipeline Overview

1. **Load Data** → Images + 3 masks (object, probe, color)
2. **Calibrate Lights** → Find sphere center, detect brightest points, compute light directions
3. **Estimate Normals** → Solve photometric stereo equation for each pixel
4. **Integrate Depth** → Convert normals to depth map using Frankot-Chellappa
5. **Visualize** → Create 3D point cloud with texture

## Running the Notebook

```bash
.venv/bin/jupyter notebook PhotometricStereo_Bunny.ipynb
```

## What Each Mask Does

- **object_mask.png**: Isolates bunny from background (used for reconstruction)
- **probe_mask.png**: Identifies light probe sphere (used for light calibration)
- **color_mask.png**: Marks white balance sheet (used for intensity normalization - optional)

## Expected Output

- Surface normal map (RGB visualization)
- Albedo map (reflectance/texture)
- Depth map (height field)
- Interactive 3D point cloud

## Troubleshooting

### If brightness is too high:
- Check saturation analysis from preprocess_data.ipynb
- If >5% pixels saturated, consider gamma correction or exposure adjustment

### If light directions look wrong:
- Verify probe_mask correctly identifies the sphere
- Check that brightest point detection works (visualize in notebook)

### If reconstruction looks noisy:
- Need more images with varied light directions
- Check that bunny doesn't move between frames
- Ensure masks are accurate

## Key Assumptions

✓ **Fixed camera** - Bunny doesn't move between frames  
✓ **Lambertian surface** - Diffuse reflection (good for stuffed animals)  
✓ **Distant lights** - Light direction consistent across object  
✓ **Multiple lights** - At least 3 different directions (you have 22!)  

## Next Steps

1. Run `PhotometricStereo_Bunny.ipynb` cell by cell
2. Check light direction visualization
3. Verify normal map looks reasonable
4. Explore 3D reconstruction
5. Optional: Add white balance normalization using color_mask
