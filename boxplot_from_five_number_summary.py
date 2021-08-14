import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns


def five_number_summary_using_numpy(y):
    """
    five_number_summary function basically returns the min, [25, 50, 75] percentile, and max value from a list, array, series or dataframe - y
    :param y: input a list, array, series or a dataframe
    :return: min, [25, 50, 75] percentile, and max value
    """
    try:
        y_min, y_max = np.min(y), np.max(y)
        q1, q2, q3 = np.percentile(y, [25, 50, 75])
        return y_min, q1, q2, q3, y_max

    except Exception as e:
        return e


def box_plot(y):
    """
    Box_plot function plots a box plot for a given list, array, series or dataframe
    :param y: Input a list, array, series or dataframe
    :return: a fig boxplot object and saves the same to Disk/Drive and also returns normal
    """
    try:
        y_min, q1, q2, q3, y_max = five_number_summary_using_numpy(y)  # calling five number summary
        iqr = q3 - q1  # Inter quartile range
        lower_bound = q1 - 1.5 * iqr
        higher_bound = q3 + 1.5 * iqr
        _outliers = outliers(y, lower_bound, higher_bound)
        normal_values = lambda a: a > lower_bound or a < higher_bound
        _normal = list(filter(normal_values, y))

        # Plotting boxplot
        sns.boxplot(data=[y_min, q1, q2, q3, y_max], orient="h")
        plt.show()

        return _outliers, _normal

    except Exception as e:
        return e

    finally:
        filename = 'C:/Users/' + str(np.random.randint(23532345)) + ".png"
        plt.savefig(filename)


def outliers(y, lower_bound, higher_bound):
    """
    outliers method detects outliers based upon the given lower and higher bounds
    :param y: Input a list, array, series or dataframe
    :param lower_bound: q1 - 1.5 * iqr
    :param higher_bound: q3 + 1.5 * iqr
    :return: outliers
    """
    try:
        outlier_values = lambda a: a < lower_bound or a > higher_bound
        _outliers = list(filter(outlier_values, y))
        return _outliers

    except Exception as e:
        return e


y = [11, 13, 34, 65, 66, 67, 68, 69, 40, 61, 72, 43, 54, 25, 36, 57, 48, 60]
box_plot(y)
