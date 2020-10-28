import pandas as pd

# Create empty dictionary
lottery_list = {}

# Count total tickets
ticket_count = 0

my_file = "tickets.xlsx"

def read_file():
    global my_file
    global ticket_count

    try:
        # reading in xlsx format only!
        data = pd.read_excel(my_file, header=None)
        nan_value = data.isnull().values.any()
        if nan_value == False:
            for number in data.values:
                for i in number[1:]:
                    # Check for correct numbers input!
                    if type(i) == int:
                        continue
                    if type(i) == str:
                        print("String error: {} contains string '{}'. Only integers are possible.".format(number[0], i))
                        raise SystemExit(0)
                    else:
                        print("Float error: {} contains float '{}'. Only integers are possible.".format(number[0], i))
                        raise SystemExit(0)

                # Write numbers into dictionary
                lottery_list[number[0]] = (number[1:])
                ticket_count += 1
        else:
            print("NaN error: Please check your xlxs file.")
            raise SystemExit(0) 

    except (FileNotFoundError):
        print("FileNotFoundError: xlsx file not found.")
        raise SystemExit(0)

    # Testing
    # print("Checking excel file done.")