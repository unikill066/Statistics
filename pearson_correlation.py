# Pearson Correlation is measure of linear correlation between 2 sets of data.
# Basically ratio of covariance to product of their standard deviations.
# Thus it i a normalized measurement of covariance. The limitation is that, pearson correlation
# ignores other types of relationships (or) correlations.

# Imports
import numpy as np
from measure_of_dispersion import *


def pearson_correlation(x, y):
        """
        This function takes two lists, arrays, Series, dataframe and outputs pearson_correlation value.
        Basically quantifying the linear relationship between x and y.
        :param x: Input a list, array, Series or a dataframe for x
        :param y: Input a list, array, Series or a dataframe for y
        return: linear correlation between x and y
        """
        try:
            x_mean = np.mean(x)
            y_mean = np.mean(y)
            cov_nu = 0
            for i, j in zip(x, y):
                temp = cov_nu
                cov_nu = (i - x_mean) * (j - y_mean)
                cov_nu = temp + cov_nu
            cov = cov_nu / (len(x))
            return cov/(standard_deviation_using_numpy(x) * standard_deviation_using_numpy(y))

        except Exception as e:
            return e


def determine_pearson_correlation(x, y):
    """
    This function takes two lists, arrays, Series, dataframe and outputs the correlation.
    Basically quantifying the relationship between x and y ==> Positive, Negative or No correlation
    :param x: Input a list, array, Series or a dataframe for x
    :param y: Input a list, array, Series or a dataframe for y
    return: linear correlation between x and y
    """
    try:
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        cov_nu = 0
        for i, j in zip(x, y):
            temp = cov_nu
            cov_nu = (i - x_mean) * (j - y_mean)
            cov_nu = temp + cov_nu
        cov = cov_nu / (len(x))
        pearson_cov = cov / (standard_deviation_using_numpy(x) * standard_deviation_using_numpy(y))
        if pearson_cov >= 0.75:
            return "High Positive Correlation"
        elif 0.75 > pearson_cov > 0:
            return "Positive Correlation"
        elif pearson_cov == 0:
            return "No Correlation"
        elif 0 > pearson_cov > -0.75:
            return "Negative Correlation"
        elif -0.75 > pearson_cov >= -1:
            return "High Negative Correlation"
        else:
            msg = "Correlation value cannot be determined for", x, "and", y
            raise Exception(msg)

    except Exception as e:
        return e


x = [12, 131, 41, 41, 231, 41, 53, 36, 4, 75, 8, 7, 35, 93, 124, 23, 78, 92, 124, 12, 65, 77, 87, 91]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101, 11, 24, 6, 7, 23, 41, 45, 26, 72, 72, 89, 47, 82, 92]
print("\nPearson Correlation of\n", x, "\nand\n", y, "\nis:", pearson_correlation(x, y))
print("\n", determine_pearson_correlation(x, y))