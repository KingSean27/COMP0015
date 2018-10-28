# imports modules used
import time
import os

# all definitions
def menu_screen():
    """This function prints the menu options."""

    os.system('clear')
    print("Welcome to Split-it!")

    print('''
    About          (A)
    Create Project (C)
    Enter Votes    (V)
    Show Projects  (S)
    Quit           (Q)
    ''')

def menu_redirect():
    """This function redirects the user to a different page.

    The user provides an input and is then redirected to the corresponding page.
    If an invalid choice is entered then the user is prompted to make another choice."""

    menu_choice = str(input("Please choose an option and press <Enter>: "))
    menu_choice = menu_choice.upper()

    if menu_choice == "A":
        about()
    elif menu_choice == "C":
        create_project()
    elif menu_choice == "V":
        enter_votes()
    elif menu_choice == "S":
        show_projects()
    elif menu_choice == "Q":
        os.system('clear')
        print("Thanks for using Split-it! Closing application...")
        time.sleep(2)
        os.system('clear')
        quit()
    else:
        print("Please choose again")
        menu_redirect()

def menu():
    """This calls the functions which allow the menu to be displayed and operate."""

    menu_screen()
    menu_redirect()

def enter_votes():
    """This displays a message for two seconds then clears the console."""

    os.system('clear')
    print("New features coming soon!")
    time.sleep(2)
    menu()

def show_projects():
    """This displays a message for two seconds then clears the console."""

    os.system('clear')
    print("New features coming soon!")
    time.sleep(2)
    menu()

def about():
    """This displays information about the programme and returns to the menu screen on the user's command """

    os.system('clear')
    print("This is Split-it a coursework marking app")
    input("\n\nPress any key followed by <Enter> to return to the main menu.")
    menu()

def create_project():
    """This function allows the user to add a new team and participants."""

    os.system('clear')
    group = input("Enter the project name: ")
    number = int(input("Enter the number of team members: "))
    if number > 2 and number < 99:
        for i in range(number):
            input("Enter the name of team member {}: ".format(i + 1))
    else:
        print("Please enter a number between 3 and 99")
        time.sleep(2)
        create_project()
    input("\n\nPress the any key to return to main menu.")
    menu()

#Call the menu function to begin the programme
menu()
