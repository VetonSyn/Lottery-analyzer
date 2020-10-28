# ---------- Change names and functions ---------- #

# Note (!)
# You must save your file as a xlsx format otherwise the file will not work
excel_file_name = "new tickets.xlsx"

# Template styles
# "default"
# "green"
my_template = "default"

# ---------- Change names and functions ---------- #

# Import modules
import xlsxwriter
from package.excel_reader import lottery_list
from package.variations import input_numbers_list
from package.random_generator import random_numbers, specified_number
from package.check_equal_numbers import list_equal

# Output data
class Writer(object):
    
    workbook = xlsxwriter.Workbook(excel_file_name)
    worksheet = workbook.add_worksheet()

    # user choice which style he wants
    template = None

    # Standard variables
    title_cell_ticket = 1 # Count tickets default is 1 (starting from Ticket 1)
    row_count = 12  # Count rows (starting from row "13")

    def __init__(self):

        self.workbook
        self.worksheet
        self.template

        # Column formats
        # Get the right column length

        # Ticket column title
        self.ticket_column = 1

        # Get the max value length of the lottery list, included ticket column
        self.max_length_lottery_list = len(max(lottery_list.values(), key=len)) + self.ticket_column

        # +1 for total column
        self.total_column = self.max_length_lottery_list + 1 

        # Bonus column
        self.bonus_column = None

        # column for random
        self.random_column = self.ticket_column + self.total_column + self.max_length_lottery_list

        # header column
        self.total_header_column = self.random_column

    def window(self):

        # Change styles
        self.template = my_template

        if self.template == "default" or "green":
            Templates(self.template).check_templates()
        else:
            print("Template", self.template, "not found.")
            raise SystemExit(0)

        # column "A" will be skipped!
        self.worksheet.set_column(0, 0, 4)

        # Change height of row "12"
        self.worksheet.set_row(11, 30)

        # Change height for each row, starting from row "13"
        row = 12
        for __ in lottery_list.keys():
            self.worksheet.set_row(row, 30)
            row += 1

        # Set sheet to landscape mode
        self.worksheet.set_landscape()

        # Hide sheet
        self.worksheet.hide_gridlines(2)

        # Columns width
        self.worksheet.set_column(2, 15, 10)

        # Load writing functions
        self.header()
        self.your_tickets()
        self.total()
        self.random_numbers()
        self.workbook_close()

    def header(self):

        # import correct lottery game
        from package.variations import user_game, currency_sign, total, max_bonus_range, range_lottery_game_numbers, max_extra_number

        # Create empty list for lottery numbers
        lottery_list = []

        # Loop through the lottery game numbers (not incl bonus or extra ball)
        for i in input_numbers_list[:range_lottery_game_numbers]:
            if i in input_numbers_list[:range_lottery_game_numbers]:
                lottery_list.append(i)

        # Sorting the lottery list
        lottery_list.sort()

        if max_bonus_range > 0:
            # Change values variables values if bonus is included in the lottery game
            self.max_length_lottery_list = self.max_length_lottery_list - max_bonus_range
            self.bonus_column = self.max_length_lottery_list + max_bonus_range

            # Show the bonus numbers with the stars*
            for i in input_numbers_list[range_lottery_game_numbers:]:
                if i in input_numbers_list[range_lottery_game_numbers:]:
                    x = "{}*".format(i)
                    lottery_list.append(x)
        
        if max_extra_number > 0:
            # Show the extra ball numbers with the stars*
            for i in input_numbers_list[range_lottery_game_numbers:]:
                if i in input_numbers_list[range_lottery_game_numbers:]:
                    x = "{}*".format(i)
                    lottery_list.append(x)

        lottery_list_new = (" ".join(str(i) for i in lottery_list))

        # Header analyser, incl. numbers
        self.worksheet.merge_range(1, 1, 9, self.total_header_column, "", Writer.header_styling)
        self.worksheet.write_rich_string("B2", user_game, Writer.header_styling, " analyser\n", Writer.header_small_txt,
        "Numbers: ", Writer.header_small_txt, lottery_list_new, Writer.header_small_txt,
        "\nTotal spend: ", Writer.header_small_txt, currency_sign, Writer.header_small_txt, "{:.2f}".format(total), Writer.header_styling)

        # Your tickets 
        self.worksheet.merge_range(11, 1, 11, self.max_length_lottery_list, "Your tickets", Writer.header_default_row)
        
        # Write "bonus" if lottery game has bonus number (not extra ball)
        if max_bonus_range == 1:
            self.worksheet.write(11, self.max_length_lottery_list + 1, "Bonus ({})*".format(max_bonus_range), Writer.header_default_row)
        elif max_bonus_range > 1:
            self.worksheet.merge_range(11, self.max_length_lottery_list + 1, 11, self.bonus_column, "Bonus ({})*".format(max_bonus_range), Writer.header_default_row)

        # Total
        self.worksheet.write(11, self.total_column, "Total", Writer.header_default_row)

        # Random new numbers
        self.worksheet.merge_range(11, self.total_column + 2, 11, self.random_column, "Random new numbers", Writer.header_default_row)

    def your_tickets(self):

        # Import max range from default numbers only
        from package.variations import range_lottery_game_numbers, max_range_number_extra_ball, extra_ball_list

        # Import max_range_number_extra_ball only for extra balls
        
        for key, value in lottery_list.items():

            # Get correct cells formats
            Templates(self.template).check_row()

            # Write tickets, starting from column "B"
            self.worksheet.write(Writer.row_count, 1, key, Writer.tickets_head)
            Writer.title_cell_ticket += 1 # count tickets

            col = 2 # Start writing numbers from column "C"
            
            for i in value[:range_lottery_game_numbers + max_range_number_extra_ball]:

                Templates(self.template).check_even() # Return cell formats
                Templates(self.template).check_odd()  # Return cell formats 

                # Checking equal number for correct cell format
                if i in input_numbers_list[:range_lottery_game_numbers + max_range_number_extra_ball]:
                    if i in extra_ball_list:
                        self.worksheet.write(Writer.row_count, col, str(i) + "*", Writer.number_cell_even) # Check extra ball
                    else:
                        self.worksheet.write(Writer.row_count, col, i, Writer.number_cell_even)
                else:
                    if i in extra_ball_list:
                        self.worksheet.write(Writer.row_count, col, str(i) + "*", Writer.number_cell_odd) # Check extra ball
                    else:
                        self.worksheet.write(Writer.row_count, col, i, Writer.number_cell_odd)
                col += 1 # +1 for each cell

            for i in value[range_lottery_game_numbers:]:

                Templates(self.template).check_even() # Return cell formats
                Templates(self.template).check_odd()  # Return cell formats 

                # Checking equal number for correct cell format
                if i in input_numbers_list[range_lottery_game_numbers:]:
                    self.worksheet.write(Writer.row_count, col, str(i) + "*", Writer.number_cell_even)
                else:
                    self.worksheet.write(Writer.row_count, col, str(i) + "*", Writer.number_cell_odd)            

                col += 1 # +1 for each cell

            Writer.row_count += 1 # +1 for each row

        # Reset class variables to standards values
        Writer.title_cell_ticket = 1
        Writer.row_count = 12

    def total(self):

        # Get the max value length of the lotto list
        max_length_lottery_list = len(max(lottery_list.values(), key=len))

        # + 1 because the column is also a key
        max_length_lottery_list = max_length_lottery_list + 1

        max_length_lottery_list_total = max_length_lottery_list + 1

        for key in list_equal.keys():

            Templates(self.template).check_total() # Return cell formats

            if "There are no equal nummers." in list_equal[key]:
                # Set total to 0 if there are no equal numbers
                equal_total = 0

            else:
                # Get the total of equals numbers
                equal_total = int(len(list_equal[key]))
                
            # Write total equal numbers in cell "Total" column
            self.worksheet.write(Writer.row_count, max_length_lottery_list_total, equal_total, Writer.total_cell)

            Writer.row_count += 1 # +1 for each row

        # Reset class variables to standards values
        Writer.row_count = 12

    def random_numbers(self):
        
        # Create a new sorted dict
        random_numbers_sorted = {}
        for key in (random_numbers):
            random_numbers_sorted[key] = sorted(random_numbers[key])

        for key, values in random_numbers_sorted.items():

            Templates(self.template).check_row() # Return cell formats

            # Write tickets
            self.worksheet.write(Writer.row_count, self.total_column + 2, key, Writer.tickets_head)

            Writer.title_cell_ticket += 1 # +1 for each cell

            col = self.total_column + 3 # Start writing numbers
            first_col = self.total_column + 2
            last_col = self.random_column
            for value in random_numbers_sorted[key]:

                Templates(self.template).check_odd() # Return cell formats

                if values[specified_number:]:
                    # Write new random numbers
                    self.worksheet.write(Writer.row_count, col, value, Writer.number_cell_odd)
                else:
                    self.worksheet.merge_range(Writer.row_count, first_col, Writer.row_count, last_col, value, Writer.number_cell_odd)

                col += 1 # +1 for each cell
            Writer.row_count += 1 # +1 for each row
        
        # Set row counter back to standard
        Writer.row_count = 12

    def workbook_close(self):

        # close self.workbook
        self.workbook.close()

        print("\nNew excel file generated:", str(excel_file_name))

        # Testing
        # print("Checking Excel writer done.")

# Template functions
class Templates(Writer):

    def __init__(self, template_style=None):

       self.template_style = template_style

    # Check for templates
    def check_templates(self):

        # Check for default template
        if self.template_style == "default":

            # set the default class variable template
            Writer.template = DefaultStyle.template

            default_style = DefaultStyle()

            # Default template
            default_style.template_functions()

        # Check for green template
        elif self.template_style  == "green":

            Writer.template = GreenStyle.template

            green_style = GreenStyle()

            # Green style functions
            green_style.template_functions()
            
        else:
            print("not working")

    def check_row(self):
        if self.template_style == "default":
            DefaultStyle().tickets_row_head
        elif self.template_style == "green":
            GreenStyle().green_tickets_row_head

    def check_even(self):
        if self.template_style == "default":
            DefaultStyle().default_cell_even
        elif self.template_style == "green":
            GreenStyle().green_cell_even

    def check_odd(self):
        if self.template_style == "default":
            DefaultStyle().default_cell_odd
        elif self.template_style == "green":
            GreenStyle().green_cell_odd

    def check_total(self):
        if self.template_style == "default":
            DefaultStyle().default_total
        elif self.template_style == "green":
            GreenStyle().green_total

# default template style
class DefaultStyle(Writer):

    template = "default"

    def __init__(self):
        super().__init__()

    def template_functions(self):

        # Load template functions
        self.default_header
        self.white_header
        self.row_header

    @property
    def default_header(self):

        default_header = self.workbook.add_format({
            "border": 0,
            'font_size': 30,
            "bold": True,
            "bg_color": "#355C7D",
            "font_color": "#FFFFFF",
            'align': 'center',
            'valign': 'vcenter',
            "text_wrap": True,
        })

        Writer.header_styling = default_header
        return Writer.header_styling

    @property
    def white_header(self):

        default_small_txt = self.workbook.add_format ({
            "font_color": "#FFFFFF",
            "bold": True,
            "text_wrap": True,
            'font_size': 20,
        })

        Writer.header_small_txt = default_small_txt
        return  Writer.header_small_txt

    @property
    def row_header(self):

        default_row = self.workbook.add_format({
            "bg_color": "#BDD2E3",
            "font_size": 12,
            "font_color": "#201313",
            "align": "center",
            "valign": "vcenter",
            "bold": True,
            "border": 0,
        })

        Writer.header_default_row = default_row
        return Writer.header_default_row

    @property
    def tickets_row_head(self):

        default_tickets_head_even = self.workbook.add_format({
            "align": "center",
            "valign": "vcenter",
            "bg_color": "#E9F0F5",
            "font_color": "#201313",
            "bold": False,
            "font_size": 12,
        })

        default_tickets_head_odd = self.workbook.add_format({
            "align": "center",
            "valign": "vcenter",
            "bg_color": "#FFFFFF",
            "font_color": "#201313",
            "bold": False,
            "font_size": 12,
        })
        
        if Writer.title_cell_ticket % 2 == 0:
            Writer.tickets_head = default_tickets_head_odd
        else:
            Writer.tickets_head = default_tickets_head_even

        return Writer.tickets_head

    @property
    def default_cell_even(self):
        
        default_cell_even_true = self.workbook.add_format({
            "border": 0,
            "font_size": 12,
            "bold": True,
            "bg_color": "#E9F0F5",
            "font_color": "#03BD1E",
            'align': 'center',
            'valign': 'vcenter',
        })
        
        default_cell_even_false = self.workbook.add_format({
            "border": 0,
            'font_size': 12,
            "bold": True,
            "bg_color": "#FFFFFF",
            "font_color": "#03BD1E",
            'align': 'center',
            'valign': 'vcenter',
        })

        if Writer.row_count % 2 == 0:
            Writer.number_cell_even = default_cell_even_true
        else:
            Writer.number_cell_even = default_cell_even_false

        return Writer.number_cell_even

    @property
    def default_cell_odd(self):

        default_cell_odd_true = self.workbook.add_format({
            "border": 0,
            "font_size": 12,
            "bold": False,
            "bg_color": "#E9F0F5",
            "font_color": "#141111",
            'align': 'center',
            'valign': 'vcenter',
        })

        default_cell_odd_false = self.workbook.add_format({
            "border": 0,
            'font_size': 12,
            "bold": False,
            "bg_color": "#ffffff",
            "font_color": "#141111",
            'align': 'center',
            'valign': 'vcenter',
        })

        if Writer.row_count % 2 == 0:
            Writer.number_cell_odd = default_cell_odd_true
        else:
            Writer.number_cell_odd = default_cell_odd_false

        return Writer.number_cell_odd
            
    @property
    def default_total(self):

        default_total_even = self.workbook.add_format({
            "bg_color": "#E9F0F5",
            "font_size": 12,
            "font_color": "#141111",
            "bold": True,
            "align": "center",
            "valign": "vcenter",
            "border": 0,
        })

        default_total_odd = self.workbook.add_format({
            "bg_color": "#FFFFFF",
            "font_size": 12,
            "font_color": "#141111",
            "bold": True,
            "align": "center",
            "valign": "vcenter",
            "border": 0,
        })

        if Writer.row_count % 2 == 0:
            Writer.total_cell = default_total_even
        else:
            Writer.total_cell = default_total_odd
            
        return Writer.total_cell

# Green template style
class GreenStyle(Writer):

    template = "green"

    def __init__(self):
        pass

    def template_functions(self):

        # Load template functions
        self.green_header
        self.green_txt_header
        self.green_row_header

    @property
    def green_header(self):

        green_header = self.workbook.add_format({
            "border": 0,
            'font_size': 30,
            "bold": True,
            "bg_color": "#6AD192",
            "font_color": "#FFFFFF",
            'align': 'center',
            'valign': 'vcenter',
            "text_wrap": True,
        })

        Writer.header_styling = green_header
        return Writer.header_styling

    @property
    def green_txt_header(self):

        green_small_txt = self.workbook.add_format ({
            "font_color": "#FFFFFF",
            "bold": True,
            "text_wrap": True,
            'font_size': 20,
        })

        Writer.header_small_txt = green_small_txt
        return  Writer.header_small_txt

    @property
    def green_row_header(self):

        green_row = self.workbook.add_format({
            "bg_color": "#C3E7CE",
            "font_size": 12,
            "font_color": "#201313",
            "align": "center",
            "valign": "vcenter",
            "bold": True,
            "border": 0,
        })

        Writer.header_default_row = green_row
        return Writer.header_default_row

    @property
    def green_tickets_row_head(self):

        green_tickets_head_even = self.workbook.add_format({
            "align": "center",
            "valign": "vcenter",
            "bg_color": "#E4F4E9",
            "font_color": "#201313",
            "bold": False,
            "font_size": 12,
        })

        green_tickets_head_odd = self.workbook.add_format({
            "align": "center",
            "valign": "vcenter",
            "bg_color": "#FFFFFF",
            "font_color": "#201313",
            "bold": False,
            "font_size": 12,
        })
        
        if Writer.title_cell_ticket % 2 == 0:
            Writer.tickets_head = green_tickets_head_odd
        else:
            Writer.tickets_head = green_tickets_head_even

        return Writer.tickets_head

    @property
    def green_cell_even(self):
        
        green_cell_even_true = self.workbook.add_format({
            "border": 0,
            "font_size": 12,
            "bold": True,
            "bg_color": "#E4F4E9",
            "font_color": "#DA773A",
            'align': 'center',
            'valign': 'vcenter',
        })
        
        green_cell_even_false = self.workbook.add_format({
            "border": 0,
            'font_size': 12,
            "bold": True,
            "bg_color": "#FFFFFF",
            "font_color": "#DA773A",
            'align': 'center',
            'valign': 'vcenter',
        })

        if Writer.row_count % 2 == 0:
            Writer.number_cell_even = green_cell_even_true
        else:
            Writer.number_cell_even = green_cell_even_false

        return Writer.number_cell_even

    @property
    def green_cell_odd(self):

        green_cell_odd_true = self.workbook.add_format({
            "border": 0,
            "font_size": 12,
            "bold": False,
            "bg_color": "#E4F4E9",
            "font_color": "#141111",
            'align': 'center',
            'valign': 'vcenter',
        })

        green_cell_odd_false = self.workbook.add_format({
            "border": 0,
            'font_size': 12,
            "bold": False,
            "bg_color": "#ffffff",
            "font_color": "#141111",
            'align': 'center',
            'valign': 'vcenter',
        })

        if Writer.row_count % 2 == 0:
            Writer.number_cell_odd = green_cell_odd_true
        else:
            Writer.number_cell_odd = green_cell_odd_false

        return Writer.number_cell_odd

    @property
    def green_total(self):

        green_total_even = self.workbook.add_format({
            "bg_color": "#E4F4E9",
            "font_size": 12,
            "font_color": "#141111",
            "bold": True,
            "align": "center",
            "valign": "vcenter",
            "border": 0,
        })

        green_total_odd = self.workbook.add_format({
            "bg_color": "#FFFFFF",
            "font_size": 12,
            "font_color": "#141111",
            "bold": True,
            "align": "center",
            "valign": "vcenter",
            "border": 0,
        })

        if Writer.row_count % 2 == 0:
            Writer.total_cell = green_total_even
        else:
            Writer.total_cell = green_total_odd

        return Writer.total_cell
