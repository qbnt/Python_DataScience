import load_image
import matplotlib.pyplot as plt
import numpy


def main():
    img = load_image.ft_load("animal.jpg")
    height, width, _ = img.shape
    cx, cy = width // 2, height // 2
    zoom_size = 200
    zoomed = img[cy - zoom_size:cy + zoom_size, cx - zoom_size:cx + zoom_size]

    print(f"The shape of image is: {zoomed.shape}")
    print(zoomed[0])
    print(zoomed[-1])

    rotated = [
        [
            [zoomed[y][x][c] for c in range(3)]
            for y in range(len(zoomed))
        ]
        for x in range(len(zoomed[0]))
    ]
    rotated = numpy.array(rotated)

    print(f"\nNew shape after slicing: {rotated.shape}")
    print(rotated[0])
    print(rotated[-1])
    plt.imshow(rotated)
    plt.title("Rotated Image")
    plt.axis("on")
    plt.show()


if __name__ == "__main__":
    main()
