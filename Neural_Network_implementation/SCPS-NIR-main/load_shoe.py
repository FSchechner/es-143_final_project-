import cv2 as cv
import numpy as np
import os
import glob

def generate_hemisphere_lights(num_lights):
    """
    Generate light directions in a hemisphere pattern.
    This provides a reasonable initialization for SCPS-NIR to refine.
    """
    light_dirs = []

    # Create a spiral pattern on hemisphere
    golden_ratio = (1 + np.sqrt(5)) / 2
    for i in range(num_lights):
        # Fibonacci sphere distribution
        theta = 2 * np.pi * i / golden_ratio
        phi = np.arccos(1 - 2 * (i + 0.5) / num_lights)

        # Convert spherical to Cartesian (hemisphere only, phi limited)
        # Ensure z component is positive (lights from above/around, not below)
        phi = min(phi, np.pi / 2)  # Limit to upper hemisphere

        x = np.sin(phi) * np.cos(theta)
        y = np.sin(phi) * np.sin(theta)
        z = np.cos(phi)

        light_dirs.append([x, y, z])

    light_dirs = np.array(light_dirs, dtype=np.float32)

    # Normalize
    norms = np.linalg.norm(light_dirs, axis=1, keepdims=True)
    light_dirs = light_dirs / norms

    return light_dirs

def load_shoe(path, cfg=None):
    """
    Load shoe dataset from video frames

    Expected structure:
    path/
    ├── frame_0000.jpg, frame_0001.jpg, ...
    └── masks/
        └── object_mask.png
    """

    # Load images
    img_pattern = os.path.join(path, 'frame_*.jpg')
    img_files = sorted(glob.glob(img_pattern))
    if not img_files:
        raise FileNotFoundError(f"No frame images found in {path}")

    images = []
    for img_file in img_files:
        # Read as RGB and normalize to [0, 1]
        img = cv.imread(img_file)[:, :, ::-1].astype(np.float32) / 255.
        images.append(img)
    images = np.stack(images, axis=0)
    print(f"Loaded {len(images)} images from {path}")

    # Load mask
    mask_file = os.path.join(path, 'masks', 'object_mask.png')
    if not os.path.exists(mask_file):
        raise FileNotFoundError(f"Mask not found: {mask_file}")
    mask = cv.imread(mask_file, 0).astype(np.float32) / 255.
    print(f"Loaded mask from {mask_file}")

    # Initialize light directions in hemisphere pattern
    # SCPS-NIR will refine these during training
    num_images = len(images)
    light_dir = generate_hemisphere_lights(num_images)
    print(f"Initialized {num_images} light directions in hemisphere pattern")

    # Apply coordinate system transformation to match SCPS-NIR convention
    # (y and z axis flip)
    light_dir[..., 1:] = -light_dir[..., 1:]

    # Set light intensities to ones (SCPS-NIR will estimate actual values)
    light_int = np.ones((num_images, 3), dtype=np.float32)
    print(f"Using default light intensities")

    # No ground truth normals
    gt_normal = np.zeros((images.shape[1], images.shape[2], 3), dtype=np.float32)

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
