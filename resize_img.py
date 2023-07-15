import PIL
from PIL import Image


def main():
    fixed_height = 400
    image = Image.open("20210126_143006.jpg")
    height_percent = fixed_height / float(image.size[1])
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)
    image.save("resized-img.jpg")


if __name__ == "__main__":
    main()
