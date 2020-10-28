# Lottery analyzer

# Import modules
from package.excel_reader import read_file
from package.variations import LotteryVariations
from package.check_equal_numbers import check_equal
from package.random_generator import RandomClass
from package.excel_writer import Writer
 
if __name__ == "__main__":

    read_file()
    LotteryVariations().user_choice()
    check_equal()
    RandomClass().random_numbers()
    Writer().window()
    