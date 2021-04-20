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
    deviation_1 = pow(variance(first_list_of_values), 0.5)
    deviation_2 = pow(variance(second_list_of_values), 0.5)
    result = covariance(first_list_of_values, second_list_of_values)

    return result / (deviation_1 * deviation_2)
