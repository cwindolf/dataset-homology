import os
import urllib
import gzip
import struct
import numpy as np


MNIST_TRAIN_IMG = 'http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz'
MNIST_TRAIN_LAB = 'http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz'


def _download_mnist():
    '''
    Don't call this, `mnist` will do it for you if you haven't done it yet.
    '''
    if not os.path.isdir('data'):
        os.mkdir('data')

    urllib.request.urlretrieve(MNIST_TRAIN_IMG, 'data/.tmp.gz')
    with gzip.open('data/.tmp.gz', 'rb') as image_data:
        image_data.read(16)
        images = np.empty((60000, 784), dtype=np.float32)
        for i in range(60000):
            bytes = image_data.read(784)
            image = np.asarray(struct.unpack('784B', bytes), dtype=np.float32)
            images[i] = image
    os.remove('data/.tmp.gz')
    urllib.request.urlretrieve(MNIST_TRAIN_LAB, 'data/.tmp.gz')
    with gzip.open('data/.tmp.gz', 'rb') as label_data:
        label_data.read(8)
        labels = np.empty((10000,), dtype=np.int)
        for i in range(10000):
            byte = label_data.read(1)
            labels[i] = struct.unpack('1B', byte)[0]
    os.remove('data/.tmp.gz')
    np.savez_compressed('data/mnist.npz', i=images, l=labels)


def mnist(label):
    '''
    Make a generator yielding all of the images in the
    MNIST dataset with label `label`.
    '''
    if not os.path.isdir('data') or not os.path.isfile('data/mnist.npz'):
        _download_mnist()
    dat = np.load('data/mnist.npz')
    images, labels = dat['i'], dat['l']
    for (i, l) in zip(images, labels):
        if l == label:
            yield i
