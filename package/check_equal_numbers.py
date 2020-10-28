from collections import defaultdict

# Empty dictionary to store equal numbers
list_equal = defaultdict(list)

def check_equal():
    from package.excel_reader import lottery_list
    from package.variations import input_numbers_list, max_range_number, range_lottery_game_numbers

    # Get the keys and values from the dictionary
    for key, value in lottery_list.items():

        # Checking for value up to max giving lottery numbers
        for i in value[:range_lottery_game_numbers]:
            if i in input_numbers_list[:range_lottery_game_numbers]:
                list_equal[key].append(i)

        # Checking bonus numbers
        for i in value[range_lottery_game_numbers:]:
            if i in input_numbers_list[range_lottery_game_numbers:]:
                list_equal[key].append(i)

        # Create empty tickets in equal dict. 
        if key not in list_equal:
            list_equal[key].append("There are no equal nummers.")
    
    # Testing
    # print("Checking equal numbers done.")