# This is a Python script for sTaTs - looks like a palindrome also

def mean(x):
    """
    mean function takes an array, list, set, series or dataframe and returns mean value of the given datatype.
    :param x: Pass an array, list, series, dataframe for which mean needs to be calculated
    :return: mean
    """
    import numpy as np
    sum = 0
    for i in x:
        if i is not np.nan: sum = sum + int(i)
    return sum/(len(x))


def mean_using_numpy(x):
    """
    mean_using_numpy function takes an array, list, set, series and returns mean value of the given datatype.
    :param x: Pass an array, list, series, dataframe for which mean needs to be calculated
    :return: mean
    """
    import numpy
    return numpy.mean(x)


x = [1,2,3,4,5]
print("Using the funciton mean_using_numpy:", mean_using_numpy(x))
print("Using the mean function            :", mean(x))


if __name__ == '__main__':
    pass