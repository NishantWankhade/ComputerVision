from PIL import Image

img = Image.open(r"ProfilePicturePhoto.jpg")

for h in range(img.height):
    for w in range(img.width):
        a,b,c = img.getpixel((w,h))

        a = 255 - a
        b = 255 - b
        c = 255 - c
        d = (a, b, c)
        img.putpixel((w,h),d)

img.show()
