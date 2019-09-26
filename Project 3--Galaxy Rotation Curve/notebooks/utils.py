import os
from astropy.io import fits
import numpy as np
from tqdm import tqdm

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

def smooth_nans_and_infs(data, window_buffer_size=1):
    '''
    Given an image, smooth over the nan and inf values with a square buffer window of window_buffer_size pixels. Should be odd.
    '''

    nrows, ncols = data.shape
    # Handle nans
    for nan_coords in np.argwhere(np.isnan(data)):
        print(nan_coords)
        x_nan, y_nan = nan_coords

        if 0 <= x_nan - window_buffer_size and x_nan + window_buffer_size <= nrows and 0 <= y_nan - window_buffer_size and y_nan + window_buffer_size <= ncols:
            nanmean = np.nanmean(data[x - window_buffer_size:x + window_buffer_size + 1, y - window_buffer_size:y + window_buffer_size + 1])
            data[x, y] = nanmean
        else:
            data[x, y] = np.nanmedian(data)

    # Handle infs
    data[np.isinf(data)] = np.median(data) # Lazy way for now

    assert not np.isnan(data).any(), "Not all nans removed."
    assert not np.isinf(data).any(), "Not all infs, removed."

    return data
