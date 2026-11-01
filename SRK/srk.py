import turtle
from PIL import Image

def draw_image(image_path, scale_width=200, pixel_size=5):

    img = Image.open(image_path)
    w_percent = (scale_width / float(img.size[0]))
    h_size = int(float(img.size[1]) * w_percent)
    img = img.resize((scale_width, h_size), Image.Resampling.LANCZOS)
    img = img.convert('RGB')
    width, height = img.size


    screen = turtle.Screen()
    screen.setup(width * pixel_size * 2, height * pixel_size * 2)
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.penup()
    pen.speed(5)
    pen.hideturtle()


    start_x = -width * pixel_size / 2
    start_y = height * pixel_size / 2

    print(f"Drawing {width}x{height} pixels with size {pixel_size}...")

    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            pen.color(r / 255, g / 255, b / 255)

            pen.goto(start_x + x * pixel_size, start_y - y * pixel_size)
            pen.dot(pixel_size)

        if y % 5 == 0:
            screen.update()

    screen.update()
    print("Drawing Complete!")
    turtle.done()


draw_image('srk.png', scale_width=200, pixel_size=4.5)
