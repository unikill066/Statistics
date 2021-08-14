def skewed(x):
    """
    This function finds out the skewness of the data and returns, if the data is positively, negatively or symmetrically distributed.
    :param x: Pass an array, list, series, dataframe for which skewness needs to be calculated
    :return: returns the direction towards which the data is skewed
    """
    try:
        # Imports
        import numpy, statistics, matplotlib.pyplot as plt

        mean = numpy.mean(x)
        median = numpy.median(x)
        mode = statistics.mode(x)
        print("\n", "Mean:", mean, "\n", "Median:", median, "\n", "Mode:", mode, "\n")

        y, counter = [], 0
        for i in x:
            counter = counter + 1
            y.append(counter)
        plt.plot(y, x)
        plt.title("Distribution of X")
        plt.xlabel('No. of Values in X')
        plt.ylabel('X')
        # plt.show()
        filename = "C:/Users" + "/" + str(numpy.random.randint(6576476)) + ".png"
        plt.savefig(filename)

        if mean > median > mode: return "Positively skewed data" # Eg. wealth distribution in the world
        elif mode > median > mean: return "Negatively skewed data" # Eg.Death rate (more deaths towards 80's)
        elif mean == mode == median: return "Symmetric Distribution" # Employee Salaries
        else: raise Exception("The skewness in the data cannot be predicted.")

    except Exception as e:
        return e

x = [10,11,12,14,15,16,16,12,19,31,51,18,92,10,76,29,64,52,81,27,98,43,36,71,77,89,45,65,37,11]
print(skewed(x))