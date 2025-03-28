# Стеганографический инструмент LSB

| en [English](README.md) | ru [Русский](README.ru.md) |

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Изображения](#изображения)
- [Демонстрация](#демонстрация)

## Установка

1. Убедитесь, что у вас установлен Python версии 3.7 или выше.

2. Клонируйте репозиторий:

   ```shell
   git clone https://github.com/s4yw13/LSB
   ```

3. Установите необходимые зависимости:

   ```shell
   pip install Pillow==9.5.0
   ```

## Использование

Чтобы скрыть файл в изображении используйте:

```shell
python stego_tool.py hide image_path secret_path

positional arguments:
image_path   Path to the image file
secret_path  Path to the secret file

options:
-h, --help   show this help message and exit
```

Для извлечения секретного файла из изображения и просмотра его LSB битов:

```shell
python stego_tool.py extract image_path

positional arguments:
image_path   Path to the image file

options:
-h, --help   show this help message and exit
```

## Изображения

Использованные при тестировании изображения были добавлены в images.

## Демонстрация

В директории demo расположен код, иллюстрирующий процесс получения младших битов изображения.
