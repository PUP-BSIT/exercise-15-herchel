class KDramaList:
    def __init__(self):
        self.kdramas = []
        self.watched_kdramas = []
        self.MAX_KDRAMAS = 100

    def add_kdrama(self, title):
        if len(self.kdramas) < self.max_kdramas:
            if title in self.kdramas:
                return f'\nK-drama "{title}" is already in the list.'
            else: 
                self.kdramas.append(title)
                return f'\nK-drama "{title}" added to the list.'
        else: 
            return "\nK-drama list is full. Cannot add more K-dramas."
        
    def remove_kdrama(self, title):
        if title in self.kdramas:
            self.kdramas.remove(title)
            return f'\nK-drama "{title}" removed from the list.'
        
        return f'\nK-drama "{title}" not found in the list.'
    
    def list_kdramas(self):
        if self.kdramas:
            print("\nK-Dramas Added:")
            return "\n".join(self.kdramas)
        else:
            print("\nNo K-dramas have been added yet.")
        
    def list_watched_kdramas(self):
        if self.watched_kdramas:
            print("\nWatched K-Dramas:")
            return "\n".join(self.watched_kdramas)
        else:
            return "\nNo K-dramas watched yet."
        
    def mark_watched(self, title):
        if title in self.kdramas:
            self.kdramas.remove(title)
            self.watched_kdramas.append(title)
            return f'\nK-drama "{title}" marked as watched.'
        else:
            return f'\nK-drama "{title}" not found in the list.'

    def display_menu(self):
        choice = 0
        while choice != 6:
            print("\nK-Drama List")
            print("1. Add K-Drama")
            print("2. Remove K-Drama")
            print("3. List K-Drama to Watch")
            print("4. List of Watched K-dramas")
            print("5. Mark K-Drama as Watched")
            print("6. Return to main menu")
            choice = input("Enter your choice (1-6): ")

            match choice:
                case '1':
                    title = input("Enter the title of the K-drama to add: ")
                    print(self.add_kdrama(title))
                case '2':
                    title = input("Enter the title of the K-drama to remove: ")
                    print(self.remove_kdrama(title))
                case '3':
                    print(self.list_kdramas())
                case '4':
                    print(self.list_watched_kdramas())
                case '5':
                    title = input('Enter the title to mark as watched: ')
                    print(self.mark_watched(title))
                case '6':
                    return
                case _:
                    print("Invalid choice. Please try again.")

KDramaList().display_menu()
