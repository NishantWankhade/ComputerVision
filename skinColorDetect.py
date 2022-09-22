from PIL import Image
import numpy as np


# img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\bahubali.jpg")
# img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\ProfilePicturePhoto.jpg")
img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\Screenshot (178).png")
a = np.asarray(img)
print(a)
height,width,rgb = a.shape
for x in range(height):
    for y in range(width):
            a,b,c = rgb
            if((a >= 127 and b >= 67 and c >= 41) and  (a <= 254 and b <= 202 and c <= 182) ):
                a = 255 - a
                b = 255 - b
                c = 255 - c

b = Image.fromarray(a)
b.show()

                

img.show()