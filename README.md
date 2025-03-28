# LSB Steganography Tool

| ru [Русский](README.ru.md) | en [English](README.md) |

## Content

- [Installation](#installation)
- [Usage](#usage)
- [Images](#images)
- [Demonstration](#demonstration)

## Installation

1. Make sure you have Python version 3.7 or higher installed.

2. Clone the repository:

   ```shell
   git clone https://github.com/s4yw13/LSB
   ```

3. Install the required dependencies:

   ```shell
   pip install Pillow==9.5.0
   ```

## Usage

To hide a file in an image use:

```shell
python stego_tool.py hide image_path secret_path

positional arguments:
image_path   Path to the image file
secret_path  Path to the secret file

options:
-h, --help   show this help message and exit
```

To extract a secret file from an image and view its LSB bits:

```shell
python stego_tool.py extract image_path

positional arguments:
image_path   Path to the image file

options:
-h, --help   show this help message and exit
```

## Images

The images used in testing were added to `images`.

## Demonstration

The `demo` directory contains code illustrating the process of extracting the least significant bits of an image.
