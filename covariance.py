def covariance(x, y):
    """
    This function takes two lists, arrays, Series, dataframe and outputs covariance value.
    Basically quantifying the relationship between x and y.
    :param x: Input a list, array, Series or a dataframe for x
    :param y: Input a list, array, Series or a dataframe for y
    return: joint variability between x and y (or) just covariance(x,y)
    """
    try:
        # Imports
        import numpy as np

        x_mean = np.mean(x)
        y_mean = np.mean(y)
        cov_nu = 0
        for i, j in zip(x, y):
            temp = cov_nu
            cov_nu = (i - x_mean) * (j - y_mean)
            cov_nu = temp + cov_nu
        return cov_nu/(len(x))

    except Exception as e:
        return e


def covariance_plotting(x, y):
    """
    covariance_plotting function returns the variance matrix and the spread of data using scatter plot.
    :param x: Input a list, array, Series or a dataframe for x
    :param y: Input a list, array, Series or a dataframe for y
    :return: covariance and scatter plot using seaborn
    """
    try:
        # Imports
        import matplotlib.pyplot as plt
        import seaborn as sns, numpy as np

        data = np.array([x, y]).T  # clubbing both the arrays
        covariance_matrix = np.cov(data, rowvar=False, bias=True)

        fig, ax = plt.subplots(nrows=1, ncols=2)
        fig.set_size_inches(12, 12)
        ax0 = plt.subplot(2, 2, 1)
        sns.heatmap(covariance_matrix, vmin=0)
        ax1 = plt.subplot(2, 2, 2)
        ax1.scatter(x, y, color='red', s=40)
        plt.show()

    except Exception as e:
        return e

    finally:
        import numpy, matplotlib.pyplot as plt
        filename = "C:/Users" + "/" + str(numpy.random.randint(65674737)) + ".png"
        plt.savefig(filename)


# x = [10, 20, 30, 40]
# y = [50, 60, 70, 80]
x = [12, 131, 41, 41, 231, 41, 53, 36, 4, 75, 8, 7, 35, 93, 124, 23, 78, 92, 124, 12, 65, 77, 87, 91]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 101, 11, 24, 6, 7, 23, 41, 45, 26, 72, 72, 89, 47, 82, 92]
print("\nCovariance of\n", x, "\nand\n", y, "\nis:", covariance(x, y))
covariance_plotting(x, y)

