# Define the global list to store student names
studentNames = []

def studList():
    """
    Creates a list of student names and prints each name with the last name 'Evans'.
    """
    global studentNames
    # Initialize the list with the given names
    studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
    print("Initial student list:")
    # Use a for loop to print each name with 'Evans'
    for name in studentNames:
        print(name + " Evans")

def addToList():
    """
    Prompts the user to add a new name, appends it to the list, and reprints the updated list.
    """
    global studentNames
    # Get user input and remove extra whitespace
    new_name = input("Please enter a new name to add to the list: ").strip()
    # Add the new name to the list
    studentNames.append(new_name)
    print("Updated student list:")
    # Use a for loop to print the updated list with 'Evans'
    for name in studentNames:
        print(name + " Evans")

# Main program execution
if __name__ == "__main__":
    # Call studList to display the initial list
    studList()
    # Call addToList to add a new name and display the updated list
    addToList()
