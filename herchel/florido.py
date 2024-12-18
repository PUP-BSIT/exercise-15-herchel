class Christmas:
    def __init__(self):
        self.name = "Maydelyn Florido"
        self.event = "Christmas"
        self.greet = "Merry Christmas"
    
    def print_christmas_tree(self, rows):
        from colorama import Fore, Style, init

        init(autoreset=True)
        STAR_COLOR = Fore.YELLOW + Style.BRIGHT
        END_OF_RANGE = rows + 1

        for row in range(1, END_OF_RANGE):
            if row == 1:
                print(" " * (rows - row) + STAR_COLOR + "*" * (row + (row -1)))
            else:    
                print(" " * (rows - row) + Fore.GREEN + "*" * (row + (row -1)))

        if rows == 1 or rows == 2 or rows == 3:
            print(" " * (rows - 1) + Fore.YELLOW + "|")
        else:
            print(" " * (rows - 2) + Fore.YELLOW + "| |")
            print(" " * (rows - 2) + Fore.YELLOW + "|_|")

    def count_days_left_before_christmas(self):
        import datetime 

        date_today = datetime.date.today()
        year_today = date_today.year
        christmas_date = datetime.date(year_today, 12, 25)

        if date_today > christmas_date and date_today.year != year_today:
            christmas_date = datetime.date(year_today + 1, 12, 25)
        
        days_left = (christmas_date - date_today).days
        
        if days_left == 0:
            print("It's Christmas today!")
        else:
            print(f"There are {days_left} days left until Christmas!")

    def print_christmas_greetings(self):
        from art import text2art
        from colorama import Fore, init

        init(autoreset=True)

        ascii_art = text2art("Namamasko po!")
        lines = ascii_art.split("\n")
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

        for i, line in enumerate(lines):
            print(colors[i % len(colors)] + line)

    def print_12_days_of_christmas_lyrics(self):
        from colorama import Fore, Back, Style, init

        init(autoreset=True)

        gifts = [
            "a Partridge in a Pear Tree",
            "Two Turtle Doves",
            "Three French Hens",
            "Four Calling Birds",
            "Five Gold Rings",
            "Six Geese-a-Laying",
            "Seven Swans-a-Swimming",
            "Eight Maids-a-Milking",
            "Nine Ladies Dancing",
            "Ten Lords-a-Leaping",
            "Eleven Pipers Piping",
            "Twelve Drummers Drumming"
        ]

        ordinal_numbers = [
            "first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
        ]

        BACK_COLOR = Back.GREEN + Style.NORMAL
        FORE_COLOR = Fore.RED + Style.BRIGHT

        for day in range(12):
            print(BACK_COLOR + FORE_COLOR + f"On the {ordinal_numbers[day]} "
                  + "day of Christmas, my true love sent to me:")
            for gift_day in range(day, -1, -1):
                if gift_day == 0 and day != 0:
                    print("And", end=" ")

                print(gifts[gift_day], end="")

                if gift_day != 0:
                    print(",", end=" ")
                else:
                    print(".\n")

    def print_message(self):
        print("\nMay the Christmas season fill your home with joy, ")
        print("your heart with love, and your life with laughter. ")
        print(f"{self.greet} and Happy Holidays!")
        print(f"                               - {self.name}")

    def display_menu(self):
        UNSET_OPTION = 0
        BACK_TO_MAIN_MENU_OPTION = 6
        choice = UNSET_OPTION

        while choice != BACK_TO_MAIN_MENU_OPTION:
            print("\n==== Florido's Module Menu ===")
            print("1. Christmas Tree")
            print("2. Days Left Before Christmas")
            print("3. Christmas Greetings")
            print("4. 12 Days Of Christmas Lyrics")
            print("5. Christmas Message")
            print("6. Go Back to Main Menu")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1: 
                    christmas = Christmas()
                    rows = int(input("Enter the number of rows for the "
                                     + "Christmas tree: "))
                    print("\n")
                    christmas.print_christmas_tree(rows)
                case 2:
                    christmas = Christmas()
                    christmas.count_days_left_before_christmas()
                case 3:
                    christmas = Christmas()
                    christmas.print_christmas_greetings()
                case 4:
                    christmas = Christmas()
                    christmas.print_12_days_of_christmas_lyrics()
                case 5:
                    christmas = Christmas()
                    christmas.print_message()
                case 6:
                    pass
                case _:
                    print("\nError: Invalid input. "
                          + "Please enter a number between 1 and 6.")