# Measure of dispersion basically encompasses [ Range, Variance, and Std. Deviation ]

def range_function(x):
    """
    Range function returns the range of the given list, array, dataframe, series, etc.
    :param x: Pass a list, tuple, array, series, dataframe, etc.
    :return: Range of the given datatype
    """
    try:
        import numpy as np, pandas as pd
        minimum = np.min(x)
        maximum = np.max(x)
        return maximum-minimum

    except Exception as e:
        return e


def variance(x):
    """
    Variance function calculates and returns variance of the the given list, array, dataframe, series, etc.
    :param x: Pass a list, tuple, array, series, dataframe, etc.
    :return: variance of the given x
    """
    try:
        import numpy as np
        var = 0
        x_mean = np.mean(x)
        for i in x:
            variance_calc = (i - x_mean) * (i - x_mean)
            var = var + variance_calc
        return var/(len(x))

    except Exception as e:
        return e


def variance_using_numpy(x):
    """
    variance_using_numpy function takes an array, list, set, series and returns variance value of the given datatype.
    :param x: Pass an array, list, series, dataframe for which mean needs to be calculated
    :return: variance
    """
    try:
        import numpy
        return numpy.var(x)

    except Exception as e:
        return e


def variance_of_sample(x):
    """
    Variance function calculates and returns variance of the the given sample (list, array, dataframe, series, etc).
    :param x: Pass a list, tuple, array, series, dataframe, etc.
    :return: variance of the given sample
    """
    try:
        import numpy as np
        var = 0
        x_mean = np.mean(x)
        for i in x:
            variance_calc = (i - x_mean) * (i - x_mean)
            var = var + variance_calc
        return var/(len(x)-1)

    except Exception as e:
        return e


def mean(x):
    """
    mean function takes an array, list, set, series or dataframe and returns mean value of the given datatype.
    :param x: Pass an array, list, series, dataframe for which mean needs to be calculated
    :return: mean
    """
    try:
        import numpy as np
        sum = 0
        for i in x:
            if i is not np.nan: sum = sum + int(i)
        return sum/(len(x))

    except Exception as e:
        return e


def mean_using_numpy(x):
    """
    mean_using_numpy function takes an array, list, set, series and returns mean value of the given datatype.
    :param x: Pass an array, list, series, dataframe for which mean needs to be calculated
    :return: mean
    """
    try:
        import numpy
        return numpy.mean(x)

    except Exception as e:
        return e


def standard_deviation(x):
    """
    standard deviation function calculates and returns std deviation of the the given list, array, dataframe, series, etc.
    :param x: Pass a list, tuple, array, series, dataframe, etc.
    :return: Std deviation of the given x
    """
    try:
        import numpy as np
        return np.sqrt(variance(x))

    except Exception as e:
        return e


def standard_deviation_using_numpy(x):
    """
    standard deviation function returns std deviation of the the given list, array, dataframe, series, etc.
    :param x: Pass a list, tuple, array, series, dataframe, etc.
    :return: Std deviation of the given x
    """
    try:
        import numpy as np
        return np.std(x)

    except Exception as e:
        return e


# Plotting an Ideal Random Normal Distribution Curve based on mean and std. deviation
def plot_normal_dist_curve(x):
    """
    This function plots a rough random normal curve based on the mean and std. deviation of a given list, array, series, dataframe, etc.
    :param x: feed list, array, series, dataframe, etc.
    :return: returns a plot object and saves the image to disk
    """
    try:
        # Imports
        import numpy, matplotlib.pyplot as plt

        # Normal Distribution Function from scipy package --> pip install scipy
        from scipy.stats import norm

        x_mean = numpy.mean(x)
        std_deviation = standard_deviation_using_numpy(x)

        plt.plot(x, norm.pdf(x, x_mean, std_deviation))
        plt.show()

    except Exception as e:
        return e

    finally:
        import numpy, matplotlib.pyplot as plt
        filename = "C:/Users" + "/" + str(numpy.random.randint(6576476)) + ".png"
        plt.savefig(filename)


# density function
def probability_density_function(x):
    """
    This function returns pdf value by taking in values of x, as list, array, series, dataframe
    :param x: Input a list, array, series, dataframe
    :return: pdf value
    """
    try:
        import numpy
        x_mean = numpy.mean(x)
        std_deviation = numpy.std(x)
        nor = 1/(std_deviation * numpy.sqrt(2 * numpy.pi)) * numpy.exp(- (x - x_mean)**2 / (2 * std_deviation**2))
        return nor

    except Exception as e:
        return e


def plot_normal_dist_continuous_curve(x):
    """
    This function plots a rough random normal curve based on the mean and std. deviation of a given list, array, series, dataframe, etc.
    :param x: feed list, array, series, dataframe, etc.
    :return: returns a plot object and saves the image to disk
    """
    try:
        # Imports
        import numpy, matplotlib.pyplot as plt

        x_mean = numpy.mean(x)
        std_deviation = standard_deviation_using_numpy(x)

        # calling density function
        y = probability_density_function(x)

        # plotting bell curve
        plt.plot(x, y, color='orange', linestyle='dashed')
        plt.show()

    except Exception as e:
        return e

    finally:
        import numpy
        filename = "C:/Users" + "/" + str(numpy.random.randint(6576476)) + ".png"
        plt.savefig(filename)


def plot_normal_dist_scatter_curve(x):
    """
    This function plots a rough random normal curve based on the mean and std. deviation of a given list, array, series, dataframe, etc.
    :param x: feed list, array, series, dataframe, etc.
    :return: returns a plot object and saves the image to disk
    """
    try:
        # Imports
        import numpy, matplotlib.pyplot as plt

        x_mean = numpy.mean(x)
        std_deviation = standard_deviation_using_numpy(x)

        # calling density function
        y = probability_density_function(x)

        # plotting bell curve
        plt.scatter( x, y, marker='o', s=25, color='orange')
        plt.show()

    except Exception as e:
        return e

    finally:
        import numpy
        filename = "C:/Users" + "/" + str(numpy.random.randint(6576476)) + ".png"
        plt.savefig(filename)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Using the function mean_using_numpy:", mean_using_numpy(x))
print("Using the mean function            :", mean(x))
print("Using the variance function        :", variance(x))
print("Std. deviation using numpy         :", standard_deviation_using_numpy(x))
print("Std. deviation calculated          :", standard_deviation(x))

# plot_normal_dist_curve(x)
# plot_normal_dist_continuous_curve(x)


if __name__ == '__main__':
    pass