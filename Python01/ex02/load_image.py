from PIL import Image
import numpy


def ft_load(path: str) -> numpy.array:
    """Load an image from a file into a 2D array of pixels."""
    try:
        img = Image.open(path)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        exit()
    img = img.convert("RGB")
    arr = numpy.array(img)
    print(f"The shape of image is: {arr.shape}")

    return arr
