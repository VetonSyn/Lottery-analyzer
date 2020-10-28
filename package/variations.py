# ------------------ Default maximum lottery game numbers ------------------ #

# Warning: It is not possible to have both bonus numbers and an extra ball in your lottery game.

# Powerball USA
powerball_usa_lottery_title = "Powerball" # Default game title
powerball_usa_lottery_title_bonus = "bonus number" # Bonus number title
powerball_usa_lottery_title_extra_ball = "extra ball" # Extra ball title
powerball_usa_lottery_max_number_input = 5 # input the maximum of lottery game numbers (not incl. bonus number or extra balls)
powerball_usa_lottery_max_bonus_input =  1 # Bonus number
powerball_usa_lottery_extra_ball =  0 # Extra ball
powerball_usa_lottery_ticket_price = 2 # Price per ticket

# Euromillions
euromillions_title = "Euromillions"
euromillions_title_bonus = "stars"
euromillions_title_extra_ball = "extra ball"
euromillions_max_number_input = 5
euromillions_max_bonus_input = 2
euromillions_extra_ball = 0
euromillions_ticket_price = 2.5

# Default Lottery
default_lottery_title = "Default lottery"
default_lottery_title_bonus = "bonus number"
default_lottery_title_extra_ball = "extra ball"
default_lottery_max_number_input = 6
default_lottery_max_bonus_input = 0
default_lottery_extra_ball = 4
default_lottery_ticket_price = 1.25

# Joker
joker_title = "Joker"
joker_title_bonus = "star sign"
joker_title_extra_ball = "extra sign"
joker_max_number_input = 6
joker_max_bonus_input = 0
joker_extra_ball = 1
joker_ticket_price = 1.50

# currency sign EUR
currency_sign_eur = "€"

# currency sign USD
currency_sign_usd = "$"

# currency sign GBP
currency_sign_gbp = "£"

# currency sign, default is EUR
currency_sign = currency_sign_usd

# ------------------ Default maximum lottery game numbers ------------------ #

from colorama import Fore, Back, Style, init

init(convert=True, strip=False)

# This will store users numbers input
input_numbers_list =  []

# the total ticket price
total_ticket_price = 0

class LotteryVariations:
    
    def __init__(self,  powerball_usa_game=1, euromillions_game=2, default_lotto_game=3, joker_game=4):
        # Lottery games variations

        # powerball usa lottery game
        self.pball_usa = powerball_usa_game
        # Default lottery game
        self.dl_game = default_lotto_game
        # Euromillions
        self.e_game = euromillions_game
        # Joker
        self.j_game = joker_game
        # User game choice
        self.game_choice = None
        # Text game started
        self.game_started = None

    def user_choice(self):

        """ Let the user choice to input a number that is equal to the lottery game number. """

        while True:
            try:
                # Print pattern lottery games
                self.print_games()

                # Asking for input number
                user_input_choice = int(input("\nChoose lottery game between number " + str(self.pball_usa) + " - " + str(self.j_game) + ": " ))

                # Check if the entered number is equal to the one of the lottery games
                # Check for powerball usa game
                if  user_input_choice == self.pball_usa:
                    # Set game choice to game title
                    self.game_choice = powerball_usa_lottery_title
                    # Print text (x) game has started
                    self.game_started = "\n{} lottery game has started.".format(self.game_choice)
                    # Start asking for lottery numbers
                    self.user_input(powerball_usa_lottery_max_number_input, powerball_usa_lottery_max_bonus_input, powerball_usa_lottery_extra_ball)
                    self.calculate_total(powerball_usa_lottery_ticket_price)
                    break

                # Check for euromillions game
                elif user_input_choice == self.e_game:
                    # Set game choice to game title
                    self.game_choice = euromillions_title
                    # Print text (x) game has started
                    self.game_started = "\n{} lottery game has started.".format(self.game_choice)
                    # Start asking for lottery numbers
                    self.user_input(euromillions_max_number_input, euromillions_max_bonus_input, euromillions_extra_ball)
                    self.calculate_total(euromillions_ticket_price)
                    break

                # Check for default lottery game
                elif user_input_choice == self.dl_game:
                    # Set game choice to game title
                    self.game_choice = default_lottery_title
                    # Print text (x) game has started
                    self.game_started = "\n{} has started.".format(self.game_choice)
                    # Start asking for lottery numbers
                    self.user_input(default_lottery_max_number_input, default_lottery_max_bonus_input, default_lottery_extra_ball)
                    self.calculate_total(default_lottery_ticket_price)
                    break

                    # Check for joker game
                elif user_input_choice == self.j_game:
                    # Set game choice to game title
                    self.game_choice = joker_title
                    # Print text (x) game has started
                    self.game_started =  "\n{} lottery game has started.".format(self.game_choice)
                    # Start asking for lottery numbers
                    self.user_input(joker_max_number_input, joker_max_bonus_input, joker_extra_ball)
                    self.calculate_total(joker_ticket_price)
                    break
                
                # If the input isn't equal with any lottery game number, a warning will giving
                elif user_input_choice >= (self.dl_game + self.e_game) or user_input_choice <= 0:
                    print(Fore.RED + "\nThere is no game for " + str(user_input_choice) + ". Choose again!" + Fore.RESET)

            # Exception for type error
            except (ValueError, TypeError):
                print(Fore.RED + "\nInvalid input!" + Fore.RESET)

    def user_input(self, lottery_game_numbers, lottery_bonus_numbers=0, extra_number=0):

        """ Function will be asking for user to give numbers, included the bonus number. """

        # Check if list of tickets numbers contain the same length as chosen game
        from package.excel_reader import lottery_list

        global range_lottery_game_numbers
        range_lottery_game_numbers = lottery_game_numbers

        # Max bonus for xlsx file "bonus" column
        global max_bonus_range
        max_bonus_range = lottery_bonus_numbers

        global max_extra_number
        max_extra_number = extra_number

        # The total lottery numbers with the bonus number(s)
        global max_range_number
        if lottery_bonus_numbers > 0:
            max_range_number = lottery_game_numbers + lottery_bonus_numbers
        elif extra_number > 0:
            max_range_number = lottery_game_numbers
            # max_range_number = lottery_game_numbers + extra_number
        else:
            max_range_number = lottery_game_numbers
        
        # The maximum lottery numbers
        global max_numbers_input

        # The correct game name will be printed in the xlsx file
        global user_game
        user_game = self.game_choice

        # Get the total dict values length
        lottery_length = len(max(lottery_list.values(), key=len))

        # If the game has lottery bonus numbers and an extra ball.
        if lottery_bonus_numbers > 0 and extra_number > 0:
            print("It is not possible to have both bonus numbers and an extra ball in your lottery game.\nPlease check your inputs.")
            raise SystemExit(0)

        # If the lottery length has more than 4 values (not ticket name incl.)
        elif lottery_length > 3:
            # Check of the lottery length is equal to lottery game numbers
            if lottery_length == max_range_number:
                print(Fore.BLUE + self.game_started + Fore.RESET)

            else:
                # Give error if not equal
                print("\nIncorrect input of numbers.\nPlease check your Excel file or choose another game which valid with your length of given numbers.")
                raise SystemExit(0)
        else:
            # Give error when there are less than 4 numbers in the list
            print("Unfortunately, the program will not work because you have have less than 4 numbers.\nPlease check your Excel file.")
            raise SystemExit(0)


        while True:
            try:
                """
                If the user tell the system that he have just 7 numbers, and he has a ticket that required 6 numbers + 1 bonus number then the 
                script will not work. We need to create function that the user can't use that amount of numbers, we need to multiply them 
                to allow us to work the random functionally.
                Let's be honest, there is no lottery game in the world that only needs 7 numbers but this is just for fixing the script. :)
                """

                # Asking for user for input the maximum of lottery game numbers
                max_numbers_input = int(input("What is the maximum allowed number?, example {}: ".format((Fore.GREEN + "50" + Fore.RESET))))

                # If the total of lottery game numbers & bonus numbers are less than the input ( = multiply by 2) then the program will not work
                max_numbers_input_total = (lottery_game_numbers + lottery_bonus_numbers) * 2

                # if the numbers input is less than the total (lottery game)
                if max_numbers_input < max_numbers_input_total:
                    print("Unfortunately, the program will not work because you cannot have less than {} numbers.".format((Fore.RED + str(max_numbers_input_total) + Fore.RESET)))
                else:
                    break 

            except ValueError:
                print (Fore.RED + "The input is invalid, try again!" + Fore.RESET)

        # Checking bonus numbers
        if lottery_bonus_numbers > 0:
            while True:
                try: 
                    # Asking for user for input the maximum of lottery game numbers
                    max_numbers_bonus_input = int(input("What is the maximum allowed bonus number? "))
                    if max_numbers_bonus_input > max_numbers_input:
                        print("Unfortunately, the program will not work because you cannot have more than {} numbers.".format((Fore.RED + str(max_numbers_input) + Fore.RESET)))
                    elif max_numbers_bonus_input < 5:
                        print("Unfortunately, the maximum allowed bonus number cannot be less than {}.".format((Fore.RED + str(5) + Fore.RESET)))
                    else:
                        break
                    
                except ValueError:
                    print (Fore.RED + "The input is invalid, try again!" + Fore.RESET)

        # Default numbers text
        text_numbers = Fore.GREEN + "1 - " + str(max_numbers_input) + ": " + Fore.RESET + " "

        if lottery_bonus_numbers > 0:
            # Bonus numbers text
            text_numbers_bonus = Fore.GREEN + "1 - " + str(max_numbers_bonus_input) + ": " + Fore.RESET + " "
        
        # Create empty list for bonus numbers
        bonus_numbers = []

        # Extra ball
        global max_range_number_extra_ball
        max_range_number_extra_ball = 0 # default value

        global extra_ball_list
        extra_ball_list = []

        if extra_number > 0:

            # Change variable to get an extra input for the extra ball
            max_range_number = lottery_game_numbers + extra_number
            max_range_number_extra_ball = extra_number

        for __ in range(0, max_range_number):
            while True:
                try:
                    # Check if the list (input_numbers_list) has more than lottery_game_numbers numbers
                    # If yes, then it's a bonus number
                    if lottery_bonus_numbers > 0:

                        # Check the length of number list
                        if input_numbers_list[lottery_game_numbers - 1:]:

                            while True:
                                # If true, text "bonus" will showing up
                                user_input_number = int(input("Enter your bonus number between {}".format(text_numbers_bonus)))

                                # Check if the input is greater than max input bonus numbers
                                if user_input_number > max_numbers_bonus_input:
                                    print(Fore.RED + "Your given number is too high!" + Fore.RESET)
                                else:
                                    break
                        else:
                            # When the length of the list has not yet reached the bonus numbers
                            user_input_number = int(input("Give a number between {}".format(text_numbers)))
                    else:
                        # If there are no game input bonus numbers, only text "Give a number between x-x" will show up
                        user_input_number = int(input("Give a number between {}".format(text_numbers)))

                    while True:

                        # Check if the entered number is equal or greater than 1
                        # Because you can't input zero in the lottery ticket, right?
                        if user_input_number >= 1:
                            
                            # Break while loop if user input is less than max_numbers_input
                            if user_input_number <= max_numbers_input:
                                break
                        
                            # Check if the input is greater than max input (normal) numbers
                            elif user_input_number > max_numbers_input:
                                print(Fore.RED + "Your given number is too high!" + Fore.RESET)

                                # Check if game has bonus
                                if lottery_bonus_numbers > 0:

                                    # Check the length of number list
                                    if input_numbers_list[lottery_game_numbers - 1:]:
                                        while True:
                                            # If true, text "bonus" will showing up
                                            user_input_number = int(input("Enter your bonus number between {}".format(text_numbers_bonus)))

                                            # Check if the input is greater than max input bonus numbers
                                            if user_input_number > max_numbers_bonus_input:
                                                print(Fore.RED + "Your given number is too high!" + Fore.RESET)
                                            else:
                                                break
                                    else:
                                        # When the length of the list has not yet reached the bonus numbers
                                        user_input_number = int(input("Give a number between {}".format(text_numbers)))
                                else:
                                    # If there are no game input bonus numbers, only text "Give a number between x-x" will show up
                                    user_input_number = int(input("Give a number between {}".format(text_numbers)))
                                
                        else:
                            # Asking to input again a number if 0 is entered
                            print(Fore.RED + "You cannot enter number 0, try again." + Fore.RESET)
                            # Check if game has bonus
                            if lottery_bonus_numbers > 0:

                                # Check the length of number list
                                if input_numbers_list[lottery_game_numbers - 1:]:
                                    while True:

                                        # If true, text "bonus" will showing up
                                        user_input_number = int(input("Enter your bonus number between {}".format(text_numbers_bonus)))

                                        # Check if the input is greater than max input bonus numbers
                                        if user_input_number > max_numbers_bonus_input:
                                            print(Fore.RED + "Your given number is too high!" + Fore.RESET)
                                        else:
                                            break
                                else:

                                    # When the length of the list has not yet reached the bonus numbers
                                    user_input_number = int(input("Give a number between {}".format(text_numbers)))
                            else:

                                # If there are no game input bonus numbers, only text "Give a number between x-x" will show up
                                user_input_number = int(input("Give a number between {}".format(text_numbers)))


                    # The bonus number has the option of having the same number as the normal numbers.
                    # But there is no way to have the same bonus numbers.
                    # We fix this problem be adding an extra list, special for bonus number.

                    # Check the length of number list
                    if input_numbers_list[lottery_game_numbers - 1:]:

                        # Check if game has bonus    
                        if lottery_bonus_numbers > 0:
                            
                            # Checking for multiple numbers
                            # A bonus number to input, can have the same number as the normal one
                            if user_input_number not in bonus_numbers:
                                bonus_numbers.append(user_input_number)
                                input_numbers_list.append(user_input_number)
                                break
                            else:
                                # if there are double bonus numbers than an error will be given
                                print("You already entered " + Fore.RED  + str(user_input_number) + Fore.RESET + ", try another bonus number.")
                        
                        # Check if game extra number
                        elif extra_number > 0:

                            # Checking for multiple numbers
                            # An extra bonus number cannot be the same as normal number   
                            if user_input_number not in input_numbers_list:
                                extra_ball_list.append(user_input_number)
                                input_numbers_list.append(user_input_number)
                                break

                            else:
                                # if there are double normal numbers than an error will be given
                                print("You already entered " + Fore.RED  + str(user_input_number) + Fore.RESET + ", try another number.")
                    
                    # Append input number into list
                    elif user_input_number not in input_numbers_list:
                        input_numbers_list.append(user_input_number)
                        break

                    else:
                        # If there are double normal numbers then an error will be given
                        print("You already entered " + Fore.RED  + str(user_input_number) + Fore.RESET + ", try another number.")

                except ValueError:
                    print(Fore.RED + "The input is invalid, try again!" + Fore.RESET)
        
        # Print the numbers out
        if lottery_bonus_numbers > 0:
            print("\nThe", self.game_choice, "numbers are:" + Fore.GREEN, *input_numbers_list[:lottery_game_numbers], Fore.RESET, 
            "\nYour bonus numbers are:" + Fore.GREEN, *input_numbers_list[lottery_game_numbers:], Fore.RESET, sep=" ")
        elif extra_number > 0:
            print("\nThe", self.game_choice,"numbers are:", Fore.GREEN, *input_numbers_list[:lottery_game_numbers], Fore.RESET, 
            "\nExtra ball:" + Fore.GREEN, *input_numbers_list[lottery_game_numbers:], Fore.RESET, sep=" ")
        else:
            print("\nThe", self.game_choice, "numbers are:" + Fore.GREEN, *input_numbers_list[:lottery_game_numbers], Fore.RESET, sep=" ")

    def calculate_total(self, ticket_price=0):

        # Calculate the total price of all the tickets
        from package.excel_reader import ticket_count

        # Calculate tickets
        global total
        total = ticket_count * ticket_price

    def print_games(self):
        
        # Correct values text (bonus or extra ball)
        if powerball_usa_lottery_max_bonus_input > 0:
            pball_usa_bonus_title = powerball_usa_lottery_title_bonus
            pball_usa_bonus_value = powerball_usa_lottery_max_bonus_input
        else:
            pball_usa_bonus_title = powerball_usa_lottery_title_extra_ball
            pball_usa_bonus_value = powerball_usa_lottery_extra_ball

        if euromillions_max_bonus_input > 0:
            e_game_bonus_title = euromillions_title_bonus
            e_game_bonus_value = euromillions_max_bonus_input
        else:
            e_game_bonus_title = euromillions_title_extra_ball
            e_game_bonus_value = euromillions_extra_ball

        if default_lottery_max_bonus_input > 0:
            dl_game_bonus_title = default_lottery_title_bonus
            dl_game_bonus_value = default_lottery_max_bonus_input
        else:
            dl_game_bonus_title = default_lottery_title_extra_ball
            dl_game_bonus_value = default_lottery_extra_ball

        if joker_max_bonus_input > 0:
            j_game_bonus_title = joker_title_bonus
            j_game_bonus_value = joker_max_bonus_input
        else:
            j_game_bonus_title = joker_title_extra_ball
            j_game_bonus_value = joker_extra_ball

        # Text powerball usa lottery    
        powerball_usa_lottery_game_label = (powerball_usa_lottery_title + " " + str(powerball_usa_lottery_max_number_input) + 
        " numbers + " + str(pball_usa_bonus_value) + " " + str(pball_usa_bonus_title) + ": " + str(self.pball_usa))
        
        # Text Euromillions
        euromillions_game_label = (euromillions_title + " " + str(euromillions_max_number_input) + 
        " numbers + " + str(e_game_bonus_value) + " " + str(e_game_bonus_title) + ": " + str(self.e_game))

        # Text default lottery    
        default_lottery_game_label = (default_lottery_title + " " + str(default_lottery_max_number_input) + 
        " numbers + " + str(dl_game_bonus_value) + " " + str(dl_game_bonus_title) + ": " + str(self.dl_game))
        
        # Text joker
        joker_game_label = (joker_title + " " + str(joker_max_number_input) + 
        " numbers + " + str(j_game_bonus_value) + " " + str(j_game_bonus_title) + ": " + str(self.j_game))

        # We need to get the longest word length in order to make the output of the border correctly to work
        powerball_usa_lottery_title_length = len(powerball_usa_lottery_game_label) # Powerball usa game
        euromillions_title_length = len(euromillions_game_label) # Euromillions game
        default_lottery_title_length = len(default_lottery_game_label) # Default lottery game
        joker_title_length = len(joker_game_label) # Joker game

        # Shorter variables
        pball_long = powerball_usa_lottery_title_length # Powerball USA game
        e_long = euromillions_title_length # Euromillions game
        dl_long = default_lottery_title_length # Default lottery game
        j_long = joker_title_length # joker game

        # If powerball usa word length is greater than other lottery games
        if pball_long > e_long and pball_long > j_long and pball_long > dl_long: 
            border_length = pball_long

        # If euromillions word length is greater than other lottery games
        elif e_long > dl_long and e_long > j_long and e_long > pball_long:
            border_length = e_long

        # If default lottery game word length is greater than other lottery games
        elif dl_long > e_long and dl_long > j_long and dl_long > pball_long:
            border_length = dl_long

        # If joker word length is greater than other lottery games
        elif j_long > dl_long and j_long > e_long and j_long > pball_long:
            border_length = j_long
        else:
            # Set default length 
            border_length = 15

        border = "-"
        line = border * border_length

        # Pattern lines
        print()
        print(line)
        print(powerball_usa_lottery_game_label)
        print(line)
        print(euromillions_game_label)
        print(line)
        print(default_lottery_game_label)
        print(line)
        print(joker_game_label)
        print(line)