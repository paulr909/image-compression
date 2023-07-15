import os

from PIL import Image


def main():
    images = [file for file in os.listdir() if file.endswith(("jpeg", "jpg", "png"))]
    for image in images:
        img = Image.open(image)
        # Try 600, 600 for smaller set of images
        img.thumbnail((800, 800))
        img.save("resized-" + image, optimize=True, quality=80)


if __name__ == "__main__":
    main()
