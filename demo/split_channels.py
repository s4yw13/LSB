from PIL import Image


image = Image.open('images/image.png')

width, height = image.size


def get_lsb(value):
    return value & 1


def process_channel(channel_data, color):
    result_data = []
    for pixel in channel_data:
        binary_value = bin(pixel)[-1]
        value = int(binary_value) * 255
        result_data.append((value, value, value))

    result_img = Image.new('RGB', (width, height), color)
    result_img.putdata(result_data)
    return result_img


pixels = list(image.getdata())

r_channel = [pixel[0] for pixel in pixels]
g_channel = [pixel[1] for pixel in pixels]
b_channel = [pixel[2] for pixel in pixels]

new_r_img = process_channel(r_channel, (255, 0, 0))
new_g_img = process_channel(g_channel, (0, 255, 0))
new_b_img = process_channel(b_channel, (0, 0, 255))

new_r_img.save('demo/red_channel_output.png')
new_g_img.save('demo/green_channel_output.png')
new_b_img.save('demo/blue_channel_output.png')
