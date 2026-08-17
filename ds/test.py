class Testing():
    def __init__(self):
        pass

    def display_results(test_string = None,string_array = None, data_array = None, test_data = None):
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

    def display_changes(old_values: list = None, new_values:list = None, var_values: list = None):

        old_values = old_values or []
        new_values = new_values or []
        var_values = var_values or [] 

        if len(old_values) != len(new_values):
            raise ValueError("Old values and new values list sizes do not match.")

        count = 0
        print("----OLD VALUES----")
        for idx, old_val_list in enumerate(old_values):
            print(f"Group {idx + 1} ---------------------")
           
            for old_val in old_val_list:
                name = var_values[count] if count < len(var_values) else "Variable"
                print(f"{name}: {old_val}")
                count += 1

            print(" ")

        count = 0
        print("----NEW VALUES----")
        for idx, new_val_list in enumerate(new_values):
            print(f"Group {idx + 1} ---------------------")

            for new_val in new_val_list:
                name = var_values[count] if count < len(var_values) else "Variable"
                print(f"{name}: {new_val}")
                count += 1

            print(" ")