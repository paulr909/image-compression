from PIL import Image

image = Image.open('IMG_1141.jpg')
image.thumbnail((400, 400))
image.save('IMG_1141_400x400.jpg')

print(image.size)  # Output: (400, 400)
