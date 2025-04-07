import load_image
import matplotlib.pyplot as plt


def main():
    img = load_image.ft_load("animal.jpg")
    height, width, _ = img.shape
    cx, cy = width // 2, height // 2
    zoom_size = 200

    print(f"The shape of image is: {img.shape}")
    print(img[0])
    print(img[-1])

    zoomed = img[cy - zoom_size:cy + zoom_size, cx - zoom_size:cx + zoom_size]

    print(f"\nNew shape after slicing: {zoomed.shape}")
    print(zoomed[0])
    print(zoomed[-1])
    plt.imshow(zoomed)
    plt.title("Zoomed Image")
    plt.axis("on")
    plt.show()


if __name__ == "__main__":
    main()
