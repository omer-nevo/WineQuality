from statistics import mean, median, variance, correlation
import csv


def load_data(path):
    """
    Loads data from given csv
    :param path: path to csv file
    :return: returns data as dict {name_of_feature: list_of_values}
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        read_header = None
        data = {}
        index_to_column_name = {}
        for row in reader:
            if not read_header:
                # we are at first row with names of columns
                for i, column_name in enumerate(row):  # enumerate generates index together with value
                    data[column_name] = []  # initializing as empty list
                    index_to_column_name[i] = column_name
                read_header = True
            else:
                # need to append values to data lists. We don't know column name, only index.
                for i, value in enumerate(row):
                    current_column_name = index_to_column_name[i]  # reproducing column name
                    data[current_column_name].append(float(value))
    return data


def run_analysis():
    file_path = './winequality.csv'
    data = load_data(file_path)
    low_correlation, high_correlation, linear_names = check_correlation(data)

    print('Number of features:', len(data))
    for feature_name, list_of_values in sorted(data.items()):
        print('"{}". Mean: {:3.2f}, Median: {:3.2f}, Std: {:3.4f}'.format(
            feature_name, mean(list_of_values), median(list_of_values), variance(list_of_values) ** 0.5))

    print('The strongest linear relationship is between: "{}","{}". '
          'The value is: {:3.4f}'.format(linear_names['max'][0], linear_names['max'][1], high_correlation))

    print('The weakest linear relationship is between: "{}","{}". '
          'The value is: {:3.4f}'.format(linear_names['min'][0], linear_names['min'][1],
                                         low_correlation))


def check_correlation(data):
    minimum, maximum, temp = 2, -2, 0
    correlation_dict = {'min': ["null", "null"], 'max': ["null", "null"]}
    for index, key in enumerate(list(data.keys())[:-2], start=1):
        for second_key in list(data.keys())[index:-1]:
            temp = correlation(data[key], data[second_key])
            if temp > maximum:
                maximum = temp
                correlation_dict['max'][0] = key
                correlation_dict['max'][1] = second_key

            if temp < minimum:
                minimum = temp
                correlation_dict['min'][0] = key
                correlation_dict['min'][1] = second_key

    return minimum, maximum, correlation_dict


if __name__ == '__main__':
    run_analysis()
