from collections import defaultdict
import random

# Create an empty dictionary for new random numbers
random_numbers = defaultdict(list)

# Generate new numbers
specified_number = 2

class RandomClass():
    def __init__(self, random_min_number=1):
        self.min_n = random_min_number

    def random_numbers(self):
        from package.excel_reader import lottery_list
        from package.variations import max_numbers_input
        from package.check_equal_numbers import list_equal

        # Get the max value length of the lotto list
        max_length_lottery_list = len(max(lottery_list.values(), key=len))

        # Random numbers if there are more than 3 equals number in one list
        for key, value in list_equal.items():
            # Create counter loop for random
            random_count = 0
            # Generate new numbers if there are more than 2 values
            if value[specified_number:]:
                while random_count < max_length_lottery_list:
                    # Random new number
                    i = random.randint(self.min_n, max_numbers_input)
                    # Check for not duplicate numbers
                    # Generate new tickets
                    if not i in value and i not in random_numbers[key]:
                        random_numbers[key].append(i)
                        random_count += 1
                    else:
                        if i not in random_numbers[key]:
                            random_numbers[key].append(i)
                            random_count += 1
            else:
                if key not in random_numbers:
                    random_numbers[key].append("You have not enough equal numbers.")
        
        # testing
        # print("Checking random function done.")
