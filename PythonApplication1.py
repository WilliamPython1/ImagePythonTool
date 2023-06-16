from turtle import *
from PIL import Image


t = Turtle()
t.hideturtle()


    
def get_most_prominent_color(image_path):

    image = Image.open(image_path)

    image = image.convert("RGB")

    width, height = image.size

    color_count = {}


    for x in range(width):
        for y in range(height):

            r, g, b = image.getpixel((x, y))

            color = (r, g, b)
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1


    #max is the mode of color_count, which is a list of all rgb of pixels.
    most_prominent_color = max(color_count, key=color_count.get)
    return most_prominent_color



most_prominent_color = get_most_prominent_color(image_path = r"C:\Users\willi\OneDrive\Pictures\Camera Roll\Hippo fauve art.jpg")
print("The most prominent color in the image is:", most_prominent_color)
t.screen.colormode(255)
bgcolor(most_prominent_color)
done()