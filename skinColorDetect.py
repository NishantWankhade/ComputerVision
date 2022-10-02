from PIL import Image
import numpy as np


# img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\bahubali.jpg")
img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\ProfilePicturePhoto.jpg")
# img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\Screenshot (178).png")

for x in range(img.height):
    for y in range(img.width):
            a,b,c =img.getpixel((x,y))
            if(a == 232 and b == 190 and c == 172):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 141 and b == 85 and c == 36):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 198 and b == 134 and c == 66):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 224 and b == 172 and c == 105):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 241 and b == 194 and c == 125):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 45 and b == 34 and c == 30):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 60 and b == 46 and c == 40):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 75 and b == 57 and c == 50):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 90 and b == 69 and c == 60):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 105 and b == 80 and c == 70):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 120 and b == 92 and c == 80):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 135 and b == 103 and c == 90):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 150 and b == 114 and c == 100):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 165 and b == 126 and c == 110):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 180 and b == 138 and c == 120):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 195 and b == 149 and c == 130):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 210 and b == 161 and c == 140):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 225 and b == 170 and c == 150):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 240 and b == 184 and c == 160):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 255 and b == 195 and c == 170):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            elif (a == 255 and b == 206 and c == 180):
                a = 255 - a
                b = 255 - b
                c = 255 - c
            d = (a,b,c)
            img.putpixel((x,y),d)
                

img.show()