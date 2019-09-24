import os
from astropy.io import fits
import numpy as np

def crawl_and_median(data_folder, extension):
    '''
    Two functions in one.
    '''

    img_list, headers_list = crawl_folder(os.path.join(data_folder, extension))
    master = median_img_list(img_list)

    return master, headers_list[0]

def crawl_folder(folder):
    '''
    Crawl a folder looking for .fits files. Return a list of their data and headers.
    '''

    images_list = []
    headers_list = []

    for filename in os.listdir(folder):
        filename = os.path.join(folder, filename)

        if filename.endswith(".fits"):

            assert os.path.isfile(filename), "This is not a file"

            # Extract the pixel values
            data, header = fits.getdata(filename, header=True)
            data = data.astype(float)

            images_list.append(data)
            headers_list.append(header)

    return images_list, headers_list

def median_img_list(img_list, axis=2):
    '''
    Given a list of ndarrays (of images), stack and median them into a single image.
    '''
    img_stacked = np.stack(img_list, axis=axis)
    return np.median(img_stacked, axis=axis)
