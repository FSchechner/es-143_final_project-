
================================================================
Description
================================================================

This is a dataset to test implementations of Lambertian photometric
stereo.

RAW images were captured by an (approximately) orthographic camera in the
configuration depicted in image <capture_config.jpg>. Several images were 
acquired with different light directions, and the light source
was sufficiently distant to me modeled as a directional source. An additional
images was acquired with ambient lighting (<ref.JPG>) to facilitate the manual
identification of the center and radius for each sphere.

Light directions were estimated using each sphere, and the two estimates from
the two spheres were averaged to create a final estimate of the light direction 
for each frame.

To save storage space, the spheres and the object have been cropped and are 
stored as separate images. Pixel values in the Object images are linearly
proportional to image irradiance.

3D reconstructions can be compared to the one shown here:
vision.seas.harvard.edu/qsfs/stlview/?ZGT_cat

================================================================
Notation and conventions
================================================================

We use a right-handed coordinate system such that when an image is shown, x axis
points rightwards, y axis upwards and z axis outwards toward camera. The origin 
is therefore at the bottom-left corner of the image, and the coordinates are 
1-indexed (matlab convention) so the bottom-left pixel is (1,1). 

# To load the light directions using numpy:
# Load lighting directions
import numpy as np
import os

L = np.loadtxt(os.path.join(base_data_filepath, 'light_directions.txt'))

================================================================
Folder structure
================================================================

TopDirectory
+-- capture_config.jpg        # Example of configuration used for data capture
+-- Object                   
|   |-- Image_NN.png          # Object images, numbered
|
+-- LightProbe-{1,2}          
|   |-- Image_NN.JPG          # Light probe images, numbered
|   |-- ref.JPG               # Reference light probe image with ambient lighting
|   |-- circle_data.txt       # (xc,yc,r) circle center and radius of light probe's image
|   |-- light_directions.txt  # Estimated lighting directions from one light probe
|
+-- light_directions.txt      # Final lighting directions from both light probes.

================================================================
Credits
================================================================

This dataset is a subset of the following:

Source: PSBox
Author: Ying Xiong
Created: Jan 24, 2014
Release: Feb 13, 2014 (v0.3.1)
