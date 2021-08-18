# Spearman's rank correlation coefficient: Spearman correlation of 2 random variables
# is basically the pearson correlation between the rank of the 2 variables. As Pearson's
# works only with linear correlation, we use Spearmans for variables which are monotonic
# (whether linear or not);

# Imports
import numpy as np
from scipy.stats import rankdata
from covariance import covariance
from measure_of_dispersion import standard_deviation_using_numpy


def spearman_rank_correlation_using_numpy(x, y):
    """
    This function takes two lists, arrays, Series, dataframe and outputs spearman_rank_correlation value.
    Basically quantifying the linear relationship between x and y.
    :param x: Input a list, array, Series or a dataframe for x
    :param y: Input a list, array, Series or a dataframe for y
    return: correlation between x and y
    """
    try:
        x_rank = np.array(x).argsort().argsort() + 1
        y_rank = np.array(y).argsort().argsort() + 1
        if len(x_rank) == len(y_rank):
            diff = x_rank - y_rank
            d = 0
            for i in diff: d = d + i*i
            n = len(x_rank)
            residual = (6 * d)/(n * (n*n - 1))
            pearson_coef = 1 - residual
            return "Pearson correlation of", x, "and", y, "is:", pearson_coef
        else: return "Pearson correlation CANNOT be calculated for", x, "and", y

    except Exception as e:
        return e


def spearman_rank_correlation_using_numpy_cov(x, y):
    """
    This function takes two lists, arrays, Series, dataframe and outputs spearman_rank_correlation value.
    Basically quantifying the linear relationship between x and y.
    :param x: Input a list, array, Series or a dataframe for x
    :param y: Input a list, array, Series or a dataframe for y
    return: correlation between x and y
    """
    try:
        x_rank = np.array(x).argsort().argsort() + 1
        y_rank = np.array(y).argsort().argsort() + 1
        if len(x_rank) == len(y_rank):
            cov_rank = covariance(x_rank, y_rank)
            x_rank_std = standard_deviation_using_numpy(x_rank)
            y_rank_std = standard_deviation_using_numpy(y_rank)
            pearson_coef = cov_rank/(x_rank_std * y_rank_std)
            return "Pearson correlation of", x, "and", y, "is:", pearson_coef
        else: return "Pearson correlation CANNOT be calculated for", x, "and", y

    except Exception as e:
        return e


def spearman_rank_correlation_using_scipy(x, y):
    """
    This function takes two lists, arrays, Series, dataframe and outputs spearman_rank_correlation value.
    Basically quantifying the linear relationship between x and y.
    :param x: Input a list, array, Series or a dataframe for x
    :param y: Input a list, array, Series or a dataframe for y
    return: correlation between x and y
    """
    try:
        x_rank = rankdata(np.array(x))
        y_rank = rankdata(np.array(y))
        if len(x_rank) == len(y_rank):
            diff = x_rank - y_rank
            d = 0
            for i in diff: d = d + i*i
            n = len(x_rank)
            residual = (6 * d)/(n * (n*n - 1))
            pearson_coef = 1 - residual
            return "Pearson correlation of", x, "and", y, "is:", pearson_coef
        else:
            return "Pearson correlation CANNOT be calculated for", x, "and", y

    except Exception as e:
        return e


def spearman_rank_correlation_using_scipy_cov(x, y):
    """
    This function takes two lists, arrays, Series, dataframe and outputs spearman_rank_correlation value.
    Basically quantifying the linear relationship between x and y.
    :param x: Input a list, array, Series or a dataframe for x
    :param y: Input a list, array, Series or a dataframe for y
    return: correlation between x and y
    """
    try:
        x_rank = rankdata(np.array(x))
        y_rank = rankdata(np.array(y))
        if len(x_rank) == len(y_rank):
            cov_rank = covariance(x_rank, y_rank)
            x_rank_std = standard_deviation_using_numpy(x_rank)
            y_rank_std = standard_deviation_using_numpy(y_rank)
            pearson_coef = cov_rank/(x_rank_std * y_rank_std)
            return "Pearson correlation of", x, "and", y, "is:", pearson_coef
        else:
            return "Pearson correlation CANNOT be calculated for", x, "and", y

    except Exception as e:
        return e


x = [12, 131, 41, 41, 231, 41, 53, 36, 4, 75, 8, 7, 35, 93, 124, 23, 78, 92, 124, 12, 65, 77, 87, 91]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101, 11, 24, 6, 7, 23, 41, 45, 26, 72, 72, 89, 47, 82, 92]
print(spearman_rank_correlation_using_numpy(x, y))
print(spearman_rank_correlation_using_numpy_cov(x, y))
print(spearman_rank_correlation_using_scipy(x, y))
print(spearman_rank_correlation_using_scipy(x, y))
