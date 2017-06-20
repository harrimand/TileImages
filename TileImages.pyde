
rowcount = 3   # number of image rows
colcount = 4   # number of image columns
kerning = 20    # Spacing around each image
#Example loading image that was created using the Flag program.
img = loadImage("C:\Users\Darrell\Documents\Processing3\Projects\Flag\FLAG_image.png")

def settings():
    size(colcount * (img.width + kerning) + kerning, rowcount * (img.height + kerning) + kerning) 

def setup():
    background(0, 96, 0)

def draw():
    for y in range(kerning, rowcount * img.height + kerning, img.height + kerning):
        for x in range(kerning, colcount * img.width + kerning, img.width + kerning):
            image(img, x, y)
    noLoop()