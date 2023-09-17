import numpy as np

def euclidean(x, y):
    """
    FUNCTION:
    Compute euclidean distance between "x" and "y".
    
    PARAMETERS:
    x, y -> Numpy arrays of numbers of the same length.
    
    RETURNS:
    Euclidean distance between "x" and "y".
    """
    distance = np.nan
    for xi, yi in zip(x, y):
        if xi and yi:
            distance = np.nansum(distance) + np.sqrt((xi - yi)**2)
    
    if np.isnan(distance):
        return np.inf
    else:
        return distance
    
def cosine(x, y):
    """
    FUNCTION:
    Compute the cosine of the angle between "x" and "y".
    
    PARAMETERS:
    x, y -> Numpy arrays of numbers of the same length.
    
    RETURNS:
    Cosine of the angle between "x" and "y".
    """
    valid = list()
    valid_x = (np.isnan(x) == False)
    valid_y = (np.isnan(y) == False)
    length = len(x)
    for bool1, bool2, index in zip(valid_x, valid_y, range(length)):
        if (bool1 and bool2):
            valid.append(index)
    
    x_ = x[valid].reshape((1, len(x[valid])))
    y_ = y[valid].reshape((1, len(y[valid])))
    
    cosine = (np.dot(x_, y_.T).flatten()[0])/(euclidean(x_.flatten(), np.zeros(x_.shape[0])) * euclidean(y_.flatten(), np.zeros(y_.shape[0])))
    return cosine
