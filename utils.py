from scipy import ndimage, misc, spatial
import os.path

import matplotlib.pyplot as plt
import numpy as np


COLL_DATASET_SIZE = 500
COLL_ITEM_SHAPE = (28, 40, 3)

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        d = pickle.load(fo, encoding='bytes')
    return d


def load_cifar_dataset(path, label='automobile'):
    d = unpickle(os.path.join(path, 'batches.meta'))
    label_names = d[b'label_names']
      
    label_idx = -1
    for i, name in enumerate(label_names):
        if name.decode('ascii') == label:
            label_idx = i
            break

    assert label_idx != -1
    print("Label found: {}".format(label_idx))

    def extract_data(i):
        d = unpickle(os.path.join(path, 'data_batch_{}'.format(i)))
        data = np.reshape(d[b'data'], (10000,3,32,32))
        data = np.rollaxis(data, 1, 4)
        labels = d[b'labels']
        condition = np.equal(labels, label_idx)
        
        return data[condition]

    dataset = extract_data(1)
    for i in range(2, 6):
        dataset = np.vstack((dataset, extract_data(i)))
    return dataset 


def load_image_from_file(path):
    return misc.imread(path, mode='RGB')


def load_coll_dataset(path, ext='png'):
    # Preallocate the array for faster load
    size = COLL_DATASET_SIZE
    dataset = np.empty((size,) + COLL_ITEM_SHAPE, dtype=np.uint8)
    
    # Load images into array
    for i in range(1, size + 1):
        img_path = os.path.join(path, str(i) + '.' + ext)
        img = load_image_from_file(img_path)
        dataset[i - 1] = img

    return dataset


def generate_rect(side_lengths):
    # Generates rectangular mesh
    lx, ly = side_lengths
    X, Y = np.mgrid[0:lx, 0:ly]
    return X.ravel(), Y.ravel()

def generate_hex(side_lengths):
    # Generates hexagonal mesh
    region = generate_rect(side_lengths)
    lx, ly = side_lengths
    X, Y = region
    condition = ((X + Y >= lx / 2) * (X + Y <= ly + lx / 2)
            * (Y - X >= -lx / 2) * (Y - X <= ly - lx / 2))
    
    return X[condition], Y[condition]

def resize_image(image, size):
    return misc.imresize(image, size)

def calc_mean_color(image, region, offset=(0, 0)):
    # Calculates mean color of an image region with an offset
    sx, sy = offset
    X, Y = region

    pixels = image[X + sx, Y + sy]
    mean = np.mean(pixels, axis=0)
    return mean

def paint_region(canvas, image, region, offset):
    # Paints the canvas with the image at the region
    sx, sy = offset
    X, Y = region
    
    canvas[X + sx, Y + sy] = image[X, Y]
    return canvas

def save_result(result, path):
    misc.imsave(path, result)
