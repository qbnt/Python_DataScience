from PIL import Image
import numpy


def ft_load(path: str) -> numpy.array:
    try:
        img = Image.open(path)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        exit()
    img = img.convert("RGB")
    arr = numpy.array(img)

    return arr
