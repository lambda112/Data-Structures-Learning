def testing(test_string, data_array = None, test_data = None):
    """
    Prints string used for testing data stuctures.
    Can use an array to test multiple things at once.
    """

    if test_data is not None:
        print(f"{test_string}: {test_data}\n")

    elif data_array:
        for data in data_array:
            print(f"{test_string}: {data}")

        print("\n")

    else:
        print("No data!")

