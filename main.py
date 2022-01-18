from PIL import Image
import numpy as np
from random import randrange
pixels = [[(randrange(0,255), randrange(0,255), randrange(0,255)) for c in range(800)] for r in range(800)]
# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new.png')
