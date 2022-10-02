from PIL import Image
import numpy as np


# img = Image.open(r"bahubali.jpg")
img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\ProfilePicturePhoto.jpg")
# img = Image.open(r"images.jpg")
r = 0
b = 0
g = 0
wid = min(img.height,img.width) # =
#                                   -from preventing the index out of bound error
hei = max(img.height,img.width) # =


# By Normalizing the present color in the image

# for x in range(hei):
#     for y in range(wid):
#         r1, g1, b1 = img.getpixel((x, y))
#         r += r1
#         b += b1
#         g += g1

# r /= (img.width * img.height)
# g /= (img.width * img.height)
# b /= (img.width * img.height)


# By threshold rgb values

for x in range(hei):
    for y in range(wid):
        r1, g1, b1 = img.getpixel((x, y))
        if r1 >= 105 and b1 >= 80 and g1 >= 70 and r1 <= 255 and b1 <= 255 and g1 <= 255:
            r1 = 255 - r1
            b1= 255 - b1
            g1 = 255 - g1
            d = (r1,g1,b1)
            img.putpixel((x,y),d)

# img = img.save("output_skin_detect.png") # for savving the image file

img.show()
