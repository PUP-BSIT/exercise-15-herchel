def menu():
    UNSET_OPTION = 0
    EXIT_OPTION = 5
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)

def display_get_choice():
    print("\n=== Main Menu ===")
    print("1. Durante")
    print("2. Florido")
    print("3. Riomalos")
    print("4. Siervo")
    print("5. Exit")

    return int(input("Enter your choice: "))

def process_choice(choice):
    match choice:
        case 1: 
            from herchel import durante

            durante.FitnessTracker().display_menu()
        case 2:
            from herchel import florido
            
            florido.Christmas.display_menu()
        case 3:
            from herchel import riomalos

            riomalos.KDramaList.display_menu()
        case 4:
            # TODO(Siervo): call the menu in your module
        case 5:
            pass
        case _:
            print("\nError: Invalid input. "
                  + "Please enter a number between 1 and 5.")
            
menu()