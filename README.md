# Lottery analyzer
Lottery analyzer is a powerful and simple script. Lottery script can use worldwide with some small changes. It will generate new unique tickets and more

![Lottery analyzer](https://i.postimg.cc/gk0F4yxz/Analyzer-1.jpg)

## **INSTALLATION**
Download or clone the whole folder and open the whole folder in an editor. Open main.py file in your editor an run it.
## **1 Reading Excel file:**
   No matter how many tickets you have just remember that you cannot have the same keys. 
   In this case, the keys will store in column A:

- Ticket 1
- Ticket 1
- Ticket 3
- Ticket 4
- etc...
  

   Input the numbers starting from column B. We will take for this example the lottery game Powerball in the USA which allows us to use 5 numbers with 1 bonus number.
*NOTE: You should always use the bonus number last (22 is in this case my bonus number):
 - Ticket 1, 10, 16, 18, 22, 47, 22,

 The bonus number is an extra number that you must indicate on your Powerball ticket.
 

## 2 Playing the lottery game

   In the root of the folder, run the main.py. It will run the game. For this option we will choose number 1: "Powerball 5 numbers + 1 bonus number" It will ask the first 2 questions:

 - What is the maximum allowed number?
 - What is the maximum allowed bonus number?

The answer for the Powerball lottery game:

 - 69
 - 26

Input 5 numbers from 1 to 69.
Then input 1 Powerball number from 1 to 26.

The script will run.

## 3 Generated new tickets:

When you see the text "New Excel file generated: Your_File_Name" then the script is done with the new analysis.

## External explanation:

**Bonus Number:**
This is an extra number that allows you to choose on a lottery ticket. For winning the lottery means in this case that you need to have also, the default numbers + the bonus number in your ticket.

**Extra ball:**
Some countries have multiple lottery games and Extra ball is one of them. In most cases you enter 6 numbers. If you get these 6 numbers correct, you win the lottery. But some countries, as I said before, have an extra number. This means that you get a number from them "for free". This is called *Extra ball*.

The maximum allowed extra ball number is the same as the default numbers. When you choose this game it will, you ask you 1 question:

 - What is the maximum allowed number?

**Reading Excel file:**
In the example "tickets.xlsx" you get some tickets as preview. Remember, if you have bonus numbers then it should be always at last. In column A you enter the tickets starting from Ticket 1:
From column B you need to enter the numbers.

*NOTE: Always save the file as a XLSX format, otherwist it the script will not work.

**Creating you own game:**
Find the file varations.py in the folder \package
We will take for this example the default_lottery

    * Change name of the lottery game:              default_lottery_title
    * Change the name of the bonus:                 default_lottery_title_bonus
    * Chang the name of the extra ball:             default_lottery_title_extra_ball
    * The maximum allowed numbers to enter:         default_lottery_max_number_input
    * The maximum allowed bonus numbers to enter:   default_lottery_max_bonus_input
    * The maximum allow extra balls to enter:       default_lottery_extra_ball
    * The lottery price per ticket:                 default_lottery_ticket_price

NOTE: If there are 0 Extra balls then enter 0, also for bonus numbers.
You cannot have *Extra balls* and *Bonus numbers* included in one single game.

**Random new numbers:**
In the file random_generator.py you can change when then script must generate new numbers:

    specified_number

Sometimes you will get 3 equal numbers or more in one tickets. Unfortunately, you didn't win much but with the module **Random** you can generate new unique tickets.

**Exporting new tickets:**
The new generated tickets will be also exported in a xlsx format. The numbers with * are the bonus numbers or the extra balls. You can change the output xlsx file name by change the excel_file_name in file excel_writer in \package.

**Valuta:**
In variations file you can change the currency you want.

**Templates:**
While this is still under development I'm happy to let you know that they are 2 simple excel based templates. In the Excel writer file you can change "my_template" from **default** to **green**.

**Required modules:**

 - Pandas
 - NumPy
 - Xlrd
 - Xlsxwriter

Have any ideas? Let me know it.