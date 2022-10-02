from PIL import Image
import numpy as np


img = Image.open(r"bahubali.jpg")
# img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\ProfilePicturePhoto.jpg")
# img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\Screenshot (178).png")
r = 0
b = 0
g = 0
for x in range(img.width):
    for y in range(img.height):
        r1, g1, b1 = img.getpixel((x, y))
        r += r1
        b += b1
        g += g1

r /= (img.width * img.height)
g /= (img.width * img.height)
b /= (img.width * img.height)

for x in range(img.width):
    for y in range(img.height):
        r1, g1, b1 = img.getpixel((x, y))
        if r1 >= r and b1 >= b and g1 >= g:
            r1 = 255 - r1
            b1= 255 - b1
            g1 = 255 - g1
            d = (r1,g1,b1)
            img.putpixel((x,y),d)

img.show()
