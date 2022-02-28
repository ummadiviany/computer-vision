from pydoc import plain
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from scipy.signal import convolve2d


def get_guassian_kernel(kernel_size, sigma):
    """
    Returns a guassian kernel with the given sigma.
    """
    guassian_filter = np.zeros((kernel_size,kernel_size))
    offset = int(np.floor(kernel_size/2))
    for x in range(-offset , offset+1):
        for y in range(-offset , offset+1):
            guassian_filter[x+offset,y+offset] = (1 / (2 * np.pi * sigma * sigma)) * np.exp(-(x**2 + y**2) / (2 * sigma  * sigma))

    return guassian_filter

def get_guassian_blur(image, guassian_filter):
    """
    Returns a blurred image using a guassian kernel.
    """
    gauss_blur_image = np.zeros(image.shape)
    R = image[:,:,0]
    G = image[:,:,1]
    B = image[:,:,2]
    for idx, channel in enumerate([R,G,B]):
        guassian_filter = guassian_filter / guassian_filter.sum()
        gauss_blur_image[:,:,idx] = convolve2d(channel, guassian_filter, mode='same')

    return gauss_blur_image

def get_difference_of_guassians(image, kernel_size, sigma_1, sigma_2):
    """
    Returns the difference of two guassians with the given sigmas.
    """
    guassian_filter_1 = get_guassian_kernel(kernel_size, sigma_1)
    guassian_blur_1 = get_guassian_blur(image, guassian_filter_1).astype(np.uint8)
    guassian_filter_2 = get_guassian_kernel(kernel_size, sigma_2)
    guassian_blur_2 = get_guassian_blur(image, guassian_filter_2).astype(np.uint8)
    
    return guassian_blur_1, guassian_blur_2, abs(guassian_blur_1 - guassian_blur_2)




if __name__ == '__main__':

    image = plt.imread('3images/Balls.tif')
    sigma1 = 1
    sigma2 = sigma1 * sqrt(2)
    kernel_size = int(np.ceil(6 * sigma2))

    print("sigma1: " + str(sigma1))
    print("sigma2: " + str(sigma2))
    print("kernel_size: " + str(kernel_size))

    guassian_blur_1, guassian_blur_2, dog = get_difference_of_guassians(image, kernel_size, sigma1, sigma2)

    # print("guassian_blur_1: " + str(guassian_blur_1))
    # print("Shape of guassian_blur_1: " + str(guassian_blur_1.shape))
    plt.figure(1)
    plt.subplot(2,2,1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.subplot(2,2,2)
    plt.imshow(guassian_blur_1)
    plt.title(f"Guassian Blur 1 with sigma : {sigma1}")
    plt.subplot(2,2,3)
    plt.imshow(guassian_blur_2)
    plt.title(f"Guassian Blur 2 with sigma : {sigma2:.2f}")
    plt.subplot(2,2,4)
    plt.imshow(dog)
    plt.title("Difference of Guassians")
    plt.show()

    # def plot_kernel(kernel_size, sigma):
    #     o1 = get_guassian_kernel(kernel_size, sigma)
    #     o1 = o1 / max(o1.flatten())
    #     o1 *= 255
    #     o1 = o1.astype(np.uint8)
    #     return o1

    # plt.figure(2)
    # plt.subplot(1,2,1)
    # plt.imshow(plot_kernel(kernel_size, sigma1),cmap='gray')
    # plt.title(f"Guassian Kernel with sigma : {sigma1}")
    # plt.subplot(1,2,2)
    # plt.imshow(plot_kernel(kernel_size, sigma2),cmap='gray')
    # plt.title(f"Guassian Kernel with sigma : {sigma2}")
    # plt.show()
