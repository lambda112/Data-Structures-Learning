def testing(test_string = None,string_array = None, data_array = None, test_data = None):
    """
    Prints string used for testing data stuctures.
    Can use an array to test multiple things at once.
    """

    # if using string and not array print standard test results
    if test_data is not None:
        print(f"{test_string}: {test_data}\n")

    # if using array to test multiple things at once
    elif data_array:

        # if string_array is empty or not same length as data_array raise exception
        if string_array is None or len(string_array) != len(data_array):
            raise Exception("Length of string array and data array not equal!")

        # loop through data_array and string_array producing string results
        for data,string in zip(data_array, string_array):
            print(f"{string}: {data}")

        # start new line for next test
        print(" ")

    # print no data if none was offered
    else:
        print("No data!")

