#!/usr/bin/env python
from skimage import io
from skimage.data import camera
from skimage.filters import sobel

image = camera()

original_fname = "camera_original.jpg"
edge_fname = "camerage_edges.jpg"

io.imsave(original_fname, image)
print(f"Saved original to {original_fname}.")

edge_sobel = 1 - sobel(image)

io.imsave(edge_fname, (255 * edge_sobel).astype("uint8"))
print(f"Saved edges to {edge_fname}.")
