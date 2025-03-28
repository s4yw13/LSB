import argparse

from PIL import Image


def file_to_binary(input_file: str) -> str:
    """Convert a file to binary string."""
    with open(input_file, 'rb') as file:
        content = file.read()

    binary_data = ''.join(format(byte, '08b') for byte in content)

    return binary_data


def get_lsb(value: int) -> int:
    return value & 1


def set_lsb(value: int, bit: int) -> int:
    return (value & 254) | bit


def hide_data(image_path: str, secret_path: str) -> None:
    """Hide binary data in an image and save the result."""
    binary_data = file_to_binary(secret_path)

    image = Image.open(image_path)
    width, height = image.size

    lsb_data = [get_lsb(int(byte)) for byte in binary_data]

    if len(lsb_data) > width * height * 3:
        print('Error: Not enough pixels to hide the data.')
        return

    pixels = list(image.getdata())
    new_pixels = []

    data_index = 0

    for pixel in pixels:
        new_pixel = list(pixel)
        for i in range(3):
            if data_index < len(lsb_data):
                new_pixel[i] = set_lsb(new_pixel[i], lsb_data[data_index])
                data_index += 1
        new_pixels.append(tuple(new_pixel))

    new_image = Image.new('RGB', (width, height))
    new_image.putdata(new_pixels)
    new_image.save('stego_image.png')

    print('Data hidden successfully in stego_image.png')


def get_extracted_lsb_bits(filename: str) -> bytes:
    """Extract raw LSB bits from a file."""
    with open(filename, 'rb') as f:
        content = f.read()
        return content


def extract_data(image_path: str) -> None:
    """Extract hidden data from an image."""
    image = Image.open(image_path)

    pixels = list(image.getdata())
    binary_data = [str(get_lsb(color)) for pixel in pixels for color in pixel]

    binary_str = ''.join(binary_data)
    bytes_arr = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    bytes_data = bytes([int(byte, 2) for byte in bytes_arr])

    with open('raw_data', 'wb') as file:
        file.write(bytes_data)

    raw_data = get_extracted_lsb_bits('raw_data')

    start_signature = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
    end_signature = b'\xAE\x42\x60\x82'

    start_index = raw_data.find(start_signature)

    while start_index != -1:
        end_index = raw_data.find(end_signature, start_index + 1)
        if end_index == -1:
            break

        png_data = raw_data[start_index:end_index + len(end_signature)]
        with open(f'extracted_{start_index}.png', 'wb') as png_file:
            png_file.write(png_data)
            print(f'Extracted photo and saved as extracted_{start_index}.png.')

        start_index = raw_data.find(start_signature, end_index + 1)

    print('The extracted raw LSB bits are stored in the raw_data file.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='LSB-tool',
        description='Tool to hide and extract data using LSB steganography',
        epilog='✦ Thanks for using! ツ ✦',
    )
    subparsers = parser.add_subparsers(dest='mode', title='mode')

    # Sub-parser for the hide command
    hide_parser = subparsers.add_parser('hide', help='Hide data in an image')
    hide_parser.add_argument('image_path', type=str, help='Path to the image file')
    hide_parser.add_argument('secret_path', type=str, help='Path to the secret file')

    # Sub-parser for the extract command
    extract_parser = subparsers.add_parser('extract', help='Extract data from an image')
    extract_parser.add_argument('image_path', type=str, help='Path to the image file')

    args = parser.parse_args()

    if args.mode == 'hide':
        hide_data(args.image_path, args.secret_path)
    elif args.mode == 'extract':
        extract_data(args.image_path)
    else:
        print('Invalid mode. Use either "hide" or "extract".')
