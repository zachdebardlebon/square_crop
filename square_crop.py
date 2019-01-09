import sys
from PIL import Image, ImageOps

filename = sys.argv[1]

image = Image.open(filename)
side_length = min(image.size)
cropped = ImageOps.fit(image, (side_length, side_length))

new_filename = filename.split('.')[0] + "_cropped.png"
cropped.save(new_filename)
