
#imports modules used
import time
import os


#all definitions 
def menu_screen():
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
#TODO: Add code to break after too many failed attempts

        
def menu():
    menu_screen()
    menu_redirect()

def enter_votes():
    os.system('clear')
    print("New features coming soon!")
    time.sleep(2)
    menu()

def show_projects():
    os.system('clear')
    print("New features coming soon!")
    time.sleep(2)
    menu()   

def about():
    os.system('clear')
    print("This is Split-it a coursework marking app")
    input("\n\nPress the any key to return to main menu.")
    menu()    
    
def create_project():
    os.system('clear')
    group = input("Enter the project name: ")
    number = int(input("Enter the number of team members: "))
    if number >2 and number < 99:
        for i in range(number):
            input("Enter the name of team member {}: ".format(i+1))
    else:
        print("Please enter a number between 2 and 99")
        time.sleep(2)
        create_project()
    input("\n\nPress the any key to return to main menu.")
    menu()
    
    
menu()
