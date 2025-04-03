import numpy


def slice_me(family: list, start: int, end: int) -> list:
    arr = numpy.array(family)

    print(f"My shape is : {arr.shape}")
    res = arr[start:end]
    print(f"My new shape is : {res.shape}")

    return res.tolist()
