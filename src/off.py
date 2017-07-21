'''
Toolbox for writing datasets to point clouds in
OFF file format.
'''
import numpy as np
import itertools


def asciiwriter(file):
    def write(string):
        print(string.encode('ascii'), file=file)
    return write


def write_off(dataset, output_file, n=None, write_header=True):
    '''
    Write the pointcloud described by `dataset` to the opened file
    `output_file`.  

    Arguments:
        dataset: iterable of numpy arrays.
        output_file: opened file to write to
        n: optional. if dataset is a generator, this should be its length
    '''
    # Figure out dimensions and stuff
    if not n:
        dataset = np.asarray(dataset)
        n = dataset.shape[0]
        d = dataset[0].size()
    else:
        peek = dataset.next()
        d = peek.size()
        dataset = itertools.chain([peek], dataset)
    
    write = asciiwriter(output_file)
    
    # Write first line
    if write_header:
        write('OFF %d 0 0' % n)

    # Write points
    for array in dataset:
        write(' '.join(array.flat()))
