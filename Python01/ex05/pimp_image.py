from load_image import ft_load
from PIL import Image, ImageOps
import numpy
import array


def ft_invert(array) -> array:
    """Invert color of a picture"""
    res = numpy.copy(array)
    res = [[[255 - c for c in pixel] for pixel in row] for row in res]
    return res


def ft_red(array) -> array:
    """Reding the picture"""
    res = numpy.copy(array)
    res = [[[pix[0],0,0]for pix in row]for row in res]
    return res


def ft_green(array) -> array:
    """Greening the picture"""
    res = numpy.copy(array)
    res = [[[0, pix[1], 0] for pix in row] for row in res]
    return res


def ft_blue(array) -> array:
    """Blueing the picture"""
    res = numpy.copy(array)
    res = [[[0, 0, pix[2]] for pix in row] for row in res]
    return res


def ft_grey(array):
    """Image become grey"""
    grey = numpy.copy(array)
    grey = Image.fromarray(grey)
    grey = ImageOps.grayscale(grey)
    return numpy.array(grey)

def do_img(array, function, save_to):
    """Save the image"""
    new = function(array)
    new = numpy.array(new, dtype=numpy.uint8)
    new = Image.fromarray(new)
    new.save(save_to + ".jpeg")

def main():
    img = ft_load("landscape.jpg")
    do_img(img, ft_invert, "inverted")
    do_img(img, ft_blue, "blueing")
    do_img(img, ft_green, "greening")
    do_img(img, ft_red, "reding")
    do_img(img, ft_grey, "grey")
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()