import cv2 as cv
import numpy as np
import os
import glob

def parse_txt(filename):
    """Parse text file with space-separated float values"""
    out_list = []
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        for x in lines:
            lxyz = np.array([float(v) for v in x.strip().split()], dtype=np.float32)
            out_list.append(lxyz)
    return np.stack(out_list, axis=0).astype(np.float32)

def load_cat(path, cfg=None):
    """
    Load Cat dataset (or similar structure)

    Expected structure:
    path/
    ├── Object/Image_*.png        # Object images
    ├── light_directions.txt      # Light directions (4×N format)
    └── mask.png                  # Binary mask
    """

    # Load images from Object/ subfolder
    img_pattern = os.path.join(path, 'Object', '*.png')
    img_files = sorted(glob.glob(img_pattern))
    if not img_files:
        raise FileNotFoundError(f"No images found in {path}/Object/")

    images = []
    for img_file in img_files:
        # Read as RGB and normalize to [0, 1]
        img = cv.imread(img_file)[:, :, ::-1].astype(np.float32) / 255.
        images.append(img)
    images = np.stack(images, axis=0)
    print(f"Loaded {len(images)} images from {path}/Object/")

    # Load mask
    mask_file = os.path.join(path, 'mask.png')
    mask = cv.imread(mask_file, 0).astype(np.float32) / 255.
    print(f"Loaded mask from {mask_file}")

    # Load light directions (4×N or 3×N format from Cat dataset)
    light_dir_file = os.path.join(path, 'light_directions.txt')
    light_dir = parse_txt(light_dir_file)

    # Convert from (3 or 4)×N to N×3
    if light_dir.shape[0] in [3, 4]:
        light_dir = light_dir[:3, :].T  # Take first 3 rows, transpose
        print(f"Converted light directions from {light_dir.T.shape[0]}×{light_dir.shape[0]} to {light_dir.shape}")

    # Apply coordinate system transformation (y and z axis flip)
    light_dir[..., 1:] = -light_dir[..., 1:]

    # Set light intensities to ones (not provided in Cat dataset)
    light_int = np.ones((len(images), 3), dtype=np.float32)
    print(f"Using default light intensities")

    # No ground truth normals
    gt_normal = np.zeros((images.shape[1], images.shape[2], 3), dtype=np.float32)

    # Verify
    assert len(images) == len(light_dir), \
        f"Mismatch: {len(images)} images vs {len(light_dir)} light directions"

    print(f"Dataset loaded successfully:")
    print(f"  Images: {images.shape}")
    print(f"  Mask: {mask.shape}")
    print(f"  Light directions: {light_dir.shape}")
    print(f"  Light intensities: {light_int.shape}")

    return {
        'images': images,
        'mask': mask,
        'light_direction': light_dir,
        'light_intensity': light_int,
        'gt_normal': gt_normal
    }
