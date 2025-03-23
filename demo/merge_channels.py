from PIL import Image

red_img = Image.open("demo/red_channel_output.png")
green_img = Image.open("demo/green_channel_output.png")
blue_img = Image.open("demo/blue_channel_output.png")

width, height = red_img.size

final_img = Image.new('RGB', (width, height), (0, 0, 0))

for x in range(width):
    for y in range(height):
        r_pixel = red_img.getpixel((x, y))[0]
        g_pixel = green_img.getpixel((x, y))[0]
        b_pixel = blue_img.getpixel((x, y))[0]

        pixel_color = (r_pixel * 255, g_pixel * 255, b_pixel * 255)
        final_img.putpixel((x, y), pixel_color)

final_img.save("demo/merged_image.png")
