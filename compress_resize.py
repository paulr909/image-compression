# run this in any directory with the max width parameter add -v for verbose
# image will be scaled in proportion to confine within the max width parameter
# this allows you to get images that are within a box dimension for online publishing
# (i.e. 400x400) without distorting the image

# get Pillow (fork of PIL) from pip before running --> pip install Pillow

# regarding timing: 42 seconds for 4938 so max 15 minutes for 100,000 images

import os
import sys
from PIL import Image


def compress_resize(file, max_dim, verbose=False):
    filepath = os.path.join(os.getcwd(), file)
    oldsize = os.stat(filepath).st_size
    picture = Image.open(filepath)
    dim = picture.size

    ratio = (max_dim / dim[0], max_dim / dim[1])

    picture.thumbnail((dim[0] * ratio, dim[1] * ratio), Image.ANTIALIAS)
    picture.save("Compressed_" + file, "JPEG", optimize=True, quality=65)

    newsize = os.stat(os.path.join(os.getcwd(), "Compressed_" + file)).st_size
    percent = (oldsize - newsize) / float(oldsize) * 100
    if verbose:
        print(
            "File compressed from {0} to {1} or {2}%".format(oldsize, newsize, percent)
        )
    return percent


def main():
    max_dimension = sys.argv[1]
    verbose = False
    if len(sys.argv) > 2:
        if sys.argv[2].lower() == "-v":
            verbose = True

    pwd = os.getcwd()
    tot = 0
    num = 0
    for file in os.listdir(pwd):
        if os.path.splitext(file)[1].lower() in (".jpg", ".jpeg"):
            num += 1
            tot += compress_resize(file, int(max_dimension), verbose)
    print("Average Compression: %d" % (float(tot) / num))
    print("Done")


if __name__ == "__main__":
    main()
