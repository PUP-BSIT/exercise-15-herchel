class FitnessTracker:   
    def __init__(self):
        self.activities = []
        self.completed_activities = []
        self.MAX_ACTIVITIES = 100

    def log_activity(self, activity_name, minutes):
        if len(self.activities) >= self.MAX_ACTIVITIES:
            return "Activity list is full. Cannot add more activities."

        for activity in self.activities:
            if activity["name"] == activity_name:
                activity["minutes"] += minutes
                return (f'Logged {minutes} minutes for "{activity_name}". '
                        f'Total: {activity["minutes"]} minutes.')

        self.activities.append({"name": activity_name, "minutes": minutes})
        return f'Activity "{activity_name}" added with {minutes} minutes.'

    def remove_activity(self, activity_name):
        for activity in self.activities:
            if activity["name"] == activity_name:
                self.activities.remove(activity)
                return f'Activity "{activity_name}" removed from the list.'
            
        return f'Activity "{activity_name}" not found in the list.'

    def list_activities(self):
        if not self.activities:
            return "No activities logged yet."

        activities_list = "Activities Logged:\n"
        for activity in self.activities:
            activities_list += (f'- {activity["name"]}: '
                                f'{activity["minutes"]} minutes\n')
            
        return activities_list
    
    def list_completed_activities(self):
        if not self.completed_activities:
            return "No activities completed yet."

        completed_list = "Completed Activities:\n"

        for activity in self.completed_activities:
            completed_list += f'- {activity}\n'
        return completed_list

    def mark_completed(self, activity_name):
        for activity in self.activities:
            if activity["name"] == activity_name:
                self.activities.remove(activity)
                self.completed_activities.append(activity_name)
                return f'Activity "{activity_name}" marked as completed.'
            
        return f'Activity "{activity_name}" not found in the list.'

    def display_menu(self):
        while True:
            print("\nFitness Tracker")
            print("1. Log Activity")
            print("2. Remove Activity")
            print("3. Display Activities")
            print("4. Display Completed Activities")
            print("5. Mark Activity as Completed")
            print("6. Exit")

            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    activity_name = input("Enter the activity name: ")
                    minutes = int(input("Enter the number of minutes: "))
                    print(self.log_activity(activity_name, minutes))
                case "2":
                    activity_name = input("Enter the activity name to remove: ")
                    print(self.remove_activity(activity_name))
                case "3":
                    print(self.list_activities())
                case "4":
                    print(self.list_completed_activities())
                case "5":
                    activity_name = input("Enter the activity name to mark" + 
                                          "as completed: ")
                    print(self.mark_completed(activity_name))
                case "6":
                     return
                case _:
                    print("Invalid choice. Please try again.")