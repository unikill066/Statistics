# A percentile is a comparison score between a particular score and the scores of the rest of a group.
# It shows the percentage of scores that a particular score surpassed.
# For example, if you score 75 points on a test, and are ranked in the 85 th percentile,
# it means that the score 75 is higher than 85% of the scores.

def five_number_summary(y):
    """
    five_number_summary function basically returns the min, [25, 50, 75] percentile, and max value from a list, array, series or dataframe - y
    :param y: input a list, array, series or a dataframe
    :return: min, [25, 50, 75] percentile, and max value
    """
    try:
        import numpy as np
        y_min = np.min(y)
        percentile_1 = round((25/100) * (len(y)))
        percentile_2 = round((50/100) * (len(y)))
        percentile_3 = round((75/100) * (len(y)))
        y_max = np.max(y)
        return y_min, sorted(y)[round(percentile_1)-1], sorted(y)[round(percentile_2)-1], sorted(y)[round(percentile_3)-1], y_max

    except Exception as e:
        return e


def percentile(x, y):
    """
    percentile function calculates the percentile value - x in a list, array, series or dataframe - y
    :param x: value - x (int, float)
    :param y: input a list, array, series or a dataframe
    :return: percentile value of x in the given list, series, array or dataframe - y
    """
    try:
        count = 0
        for i in y:
            if i > x: pass
            else: count = count + 1
        # percentile rank of x in y
        # percentile_value = no. of values below or equal to x / n  X 100
        return (count * 100)/len(y)

    except Exception as e:
        return e


def percentile_25(y):
    """
    percentile_25 function calculates the rank of 25% percentile value from a list, array, series or dataframe - y
    :param y: input a list, array, series or a dataframe
    :return: 25 percentile value of y - list, series, array or dataframe
    """
    try:
        percentile = 25
        # quaterpercentile_value = percentile * (n-1)/100
        percentile = (percentile/100) * (len(y))
        return round(percentile), sorted(y)[round(percentile)-1]

    except Exception as e:
        return e


def percentile_50(y):
    """
    percentile_50 function calculates the rank of 50% percentile value from a list, array, series or dataframe - y
    :param y: input a list, array, series or a dataframe
    :return: 50 percentile value of y - list, series, array or dataframe
    """
    try:
        percentile = 50
        percentile = (percentile/100) * (len(y))
        return round(percentile), sorted(y)[round(percentile)-1]

    except Exception as e:
        return e


def percentile_75(y):
    """
    percentile_75 function calculates the rank of 75% percentile value from a list, array, series or dataframe - y
    :param y: input a list, array, series or a dataframe
    :return: 75 percentile value of y - list, series, array or dataframe
    """
    try:
        percentile = 75
        percentile = (percentile / 100) * (len(y))
        return round(percentile), sorted(y)[round(percentile)-1]

    except Exception as e:
        return e


if __name__ == '__main__':
    pass


# y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
y = [11, 13, 34, 65, 66, 67, 68, 69, 40, 61, 72, 43, 54, 25, 36, 57, 48, 60]
x = 12
# print(percentile(x, y))
# print(percentile_75(y))
print("Five number summary for the given list -->", y,"is: \n", five_number_summary(y))
_min, _25, _50, _75, _max = five_number_summary(y)
print("min",_min)
print("25",_25)
print("50",_50)
print("75",_75)
print("max",_max)
