from PIL import Image

img = Image.open(r"C:\Users\ngw33\OneDrive\Desktop\ProfilePicturePhoto.jpg")

for x in range(img.height):
    for y in range(img.width):
        a,b,c = img.getpixel((x,y))

        a = 255 - a
        b = 255 - b
        c = 255 - c
        d = (a, b, c)
        img.putpixel((x,y),d)

img.show()
