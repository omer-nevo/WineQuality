def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values) / 2)  # round to int required because division always produces float

    # Median value depends on length on list
    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index - 1]) / 2
    else:
        # Now we need only 1 index for exact value
        result = sorted_list[center_index]
    return result


def mean(list_of_values):
    return sum(list_of_values) / len(list_of_values)


def variance(list_of_values):
    average = mean(list_of_values)
    squared_sum = sum([(x - average) ** 2 for x in list_of_values])
    return squared_sum / (len(list_of_values) - 1)


def covariance(first_list_of_values, second_list_of_values):
    result, mean_1, mean_2 = 0, mean(first_list_of_values), mean(second_list_of_values)
    for value1, value2 in zip(first_list_of_values, second_list_of_values):
        cov1 = value1 - mean_1
        cov2 = value2 - mean_2
        result += (cov1 * cov2)

    return result / (len(first_list_of_values) - 1)


def correlation(first_list_of_values, second_list_of_values):
    """
    the deviation is the square root of the variance
    :param first_list_of_values: a list of numbers
    :param second_list_of_values: a list of numbers
    :return: the correlation between two features, a number(range = [-1,1])
    """
    deviation_1 = pow(variance(first_list_of_values), 0.5)
    deviation_2 = pow(variance(second_list_of_values), 0.5)
    result = covariance(first_list_of_values, second_list_of_values)

    return result / (deviation_1 * deviation_2)


def check_correlation(data):
    """
     finds the weakest and strongest correlation relations between the csv features
    :param data: a dictionary from the cvs file, 12 keys
    :return: weakest and strongest pairs of feathers, and a dictionary with the pairs names
    """
    weak, strong, temp = 1, 0, 0  # initial arguments for the weak\strong check
    correlation_dictionary = {'weak': ["null", "null"], 'strong': ["null", "null"]}

    for index, first_key in enumerate(list(data.keys())[:-2], start=1):
        for second_key in list(data.keys())[index:-1]:
            temp = correlation(data[first_key], data[second_key])
            if temp > strong:
                strong = temp
                correlation_dictionary['strong'][0] = first_key
                correlation_dictionary['strong'][1] = second_key
            if abs(temp) < abs(weak):
                weak = temp
                correlation_dictionary['weak'][0] = first_key
                correlation_dictionary['weak'][1] = second_key
    # swap the features in alphabetic order
    for key in correlation_dictionary:
        if correlation_dictionary[key][0] > correlation_dictionary[key][1]:
            correlation_dictionary[key][0], correlation_dictionary[key][1] = \
                correlation_dictionary[key][1], correlation_dictionary[key][0]

    return weak, strong, correlation_dictionary
