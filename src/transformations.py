import numpy as np

def to_homogenous(coords):
    return np.array([coords[0], coords[1], coords[2], 1])