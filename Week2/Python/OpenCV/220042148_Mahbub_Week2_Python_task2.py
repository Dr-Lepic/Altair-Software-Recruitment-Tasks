import cv2
import numpy as np


def grayscale(image, base_name):
    # Grayscale filter
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(f"./Filtered_Images/{base_name}-grayscale.png", grayscale_image)


def blur(image, base_name):
    # Blur filter
    blur_image = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imwrite(f"./Filtered_Images/{base_name}-blur.png", blur_image)


def brightness(image, base_name):
    # Brightness adjustment filter
    brightness_image = cv2.convertScaleAbs(image, alpha=1.2, beta=50)
    cv2.imwrite(f"./Filtered_Images/{base_name}-brightness.png", brightness_image)


def invert(image, base_name):
    # Inversion filter
    inversion_image = cv2.bitwise_not(image)
    cv2.imwrite(f"./Filtered_Images/{base_name}-inversion.png", inversion_image)


def contrast(image, base_name):
    # Contrast adjustment filter
    contrast_image = cv2.convertScaleAbs(image, alpha=2.0, beta=0)
    cv2.imwrite(f"./Filtered_Images/{base_name}-contrast.png", contrast_image)


def noise(image, base_name):
    # Noise filter
    noise_image = image.copy()
    noise = np.random.normal(0, 25, noise_image.shape).astype(np.uint8)
    noise_image = cv2.add(noise_image, noise)
    cv2.imwrite(f"./Filtered_Images/{base_name}-noise.png", noise_image)


if __name__ == "__main__":
    image_path = input("Enter image path: ")

    # Load the original image
    image = cv2.imread(image_path)
    temp = image_path.split("/")[-1]
    base_name = temp.split('.')[0]

    # Filters
    grayscale(image, base_name)
    blur(image, base_name)
    brightness(image, base_name)
    invert(image, base_name)
    contrast(image, base_name)
    noise(image, base_name)

