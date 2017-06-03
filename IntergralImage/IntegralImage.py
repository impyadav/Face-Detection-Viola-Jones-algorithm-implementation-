import numpy as np
from PIL import Image
import time

start_time = time.time()

original_mat = np.array(Image.open('grey_test_image.jpg'), dtype=int)

integral_mat = np.zeros(original_mat.shape, dtype=int)


def point_sum(mat , x , y):
    sum  = 0
    a = x
    b = y
    for i in range(a+1):
        for j in range(b+1):
            sum  += mat[i,j]
    return sum


def summed_mat(mat):
    print '************Start calculating Integral Image *************'
    for k in range(mat.shape[0]):
        for l in range(mat.shape[1]):
            integral_mat[k,l] = point_sum(mat,  k, l)
    print '.........Done with Integral Image\n'
    return integral_mat


def get_area(integral_image, top_left, bottom_right):

    top_left = (top_left[0]-1, top_left[1]-1)
    bottom_right = (bottom_right[0], bottom_right[1])

    top_right = (top_left[0], bottom_right[1])
    bottom_left = (bottom_right[0], top_left[1])

    area = integral_image[top_left] - integral_image[top_right] - integral_image[bottom_left] + integral_image[bottom_right]
    return area

