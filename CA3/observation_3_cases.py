from pydoc import plain
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from scipy.signal import convolve2d
from dog_bandpass import get_guassian_kernel, get_guassian_blur, get_difference_of_guassians
import os


def dog_visualize(image):
    """
    Input : A RGB image
    Output: A RGB image with the difference of guassians with different sigmas.
    """
    # Case 1:
    # Small sigma 1
    # sigma1 << sigma2

    sigma1 = 1
    sigma2 = sigma1 * 2.5
    kernel_size = int(np.ceil(6 * sigma2))

    _, _, dog = get_difference_of_guassians(image, kernel_size, sigma1, sigma2)

    plt.figure(1)
    plt.subplot(2,2,1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.subplot(2,2,2)
    plt.imshow(dog)
    plt.title(f'Case 1: sigma_1: {sigma1} and sigma_2: {sigma2:.2f}, Window Size: {kernel_size}')


    # Case 2:
    # Large sigma 1 and Large sigma 2
    # sigma1 ~= sigam2

    sigma1 = 5
    sigma2 = sigma1 * 1.1
    kernel_size = int(np.ceil(6 * sigma2))

    _, _, dog = get_difference_of_guassians(image, kernel_size, sigma1, sigma2)

    plt.subplot(2,2,3)
    plt.imshow(dog)
    plt.title(f'Case 2: sigma_1: {sigma1} and sigma_2: {sigma2:.2f}, Window Size: {kernel_size}')

    # Case 3:
    # Small sigma 1 and Small sigma 2
    # sigma1 ~= sigam2

    sigma1 = 1
    sigma2 = sigma1 * 1.1
    kernel_size = int(np.ceil(6 * sigma2))

    _, _, dog = get_difference_of_guassians(image, kernel_size, sigma1, sigma2)

    plt.subplot(2,2,4)
    plt.imshow(dog)
    plt.title(f'Case 3: sigma_1: {sigma1} and sigma_2: {sigma2:.2f}, Window Size: {kernel_size}')
    plt.show()


for image in os.listdir('3images'):
    image_path = os.path.join('3images', image)
    image = plt.imread(image_path)
    dog_visualize(image)