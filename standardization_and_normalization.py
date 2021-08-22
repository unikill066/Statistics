# Imports
import numpy as np


def standardize(x):
    """
    This function takes a list, array, Series, dataframe and outputs a standardized list.
    :param x: Input a list, array, Series or a dataframe for x
    return: standardized list of x
    """
    try:
        _mean = np.mean(x)
        _std = np.mean(x)
        standardized_data = []
        for i in x:
            standardized_data.append((i - _mean) / _std)
        return standardized_data

    except Exception as e:
        return e


def standardize_using_sklearn(x):
    """
    This function takes a list, array, Series, dataframe and outputs a standardized list.
    :param x: Input a list, array, Series or a dataframe for x
    return: standardized list of x
    """
    try:
        from sklearn import preprocessing
        scaled_data = preprocessing.scale(x)
        return scaled_data

    except Exception as e:
        return e


def standardize_using_sklearn_standard_scaler(x):
    """
    This function takes a list, array, Series, dataframe and outputs a standardized list.
    :param x: Input a list, array, Series or a dataframe for x
    return: standardized list of x
    """
    try:
        from sklearn.preprocessing import StandardScaler
        # Initiating a StandardScaler object
        scale = StandardScaler()
        scaled_data = scale.fit_transform(x)
        return scaled_data

    except Exception as e:
        return e


def normalize(x):
    """
    This function takes a list, array, Series, dataframe and outputs a normalized list.
    :param x: Input a list, array, Series or a dataframe for x
    return: normalized list of x
    """
    try:
        _min = np.min(x)
        _max = np.max(x)
        normalized_data = []
        for i in x:
            normalized_data.append(x - _min/_max - _min)
        return normalized_data

    except Exception as e:
        return e


def normalize_using_sklearn(x):
    """
    This function takes a list, array, Series, dataframe and outputs a normalized list.
    :param x: Input a list, array, Series or a dataframe for x
    return: normalized list of x
    """
    try:
        from sklearn import preprocessing
        normalized_data = preprocessing.normalize(x)
        return normalized_data

    except Exception as e:
        return e


x = [12, 131, 41, 41, 231, 41, 53, 36, 4, 75, 8, 7, 35, 93, 124, 23, 78, 92, 124, 12, 65, 77, 87, 91]
print("-------------1--------------",standardize(x))
print("-------------2--------------",standardize_using_sklearn(x))

print("-------------1--------------",normalize(x))
print("-------------2--------------",normalize_using_sklearn(x))
