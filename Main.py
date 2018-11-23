# 00000000000000000000000000000000000000000000000000000000000000000000000000079



# imports modules used
import time
import os

# list of constants to be used
MINIMUM_NAME_LENGTH = 3     
MAXIMUM_NAME_LENGTH = 10

MINIMUM_TEAM_SIZE = 3
MAXIMUM_TEAM_SIZE = 5


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
    The user provides an input and is then redirected
    to the corresponding page. If an invalid choice is entered
    then the user is prompted to make another choice."""

    menu_choice = str(input("Please choose an option and press <Enter>: "))
    menu_choice = menu_choice.upper()
    app_open = "*"

    while app_open != "q":

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
            app_open = "q"
        else:
            print("Please choose again")
            menu_redirect()

def menu():
    """This calls the functions which allows
    the menu to be displayed and operate."""

    menu_screen()
    menu_redirect()

def enter_votes():
    """This displays a message for two seconds then clears the console."""

    os.system('clear')
    menu_choice = 0
    print("New features coming soon!")
    time.sleep(2)
    menu()



def show_projects():
    """This displays a message for two seconds then clears the console."""
    
    os.system('clear')
    menu_choice = 0
    print("New features coming soon!")
    time.sleep(2)
    menu()


def about():
    """This displays information about the programme and returns
    to the menu screen on the user's command """

    os.system('clear')
    menu_choice = 0
    print("This is Split-it a coursework marking app")
    input("\n\nPress any key followed by <Enter> to return to the main menu.")
    menu()

# create project and functions used in it 

def create_project():
    """This function allows the user to
    add a new team and participants."""

    os.system('clear')
    menu_choice = 0
    projectName = getProjectName()
    teamSize = getTeamSize()
    members = getTeamNames(teamSize)
    
    
    input("\n\nPress the any key to return to main menu.")
    menu()


##  Sets up a project from the information entered by the user.  
#   @return a tuple containing the project name and the names
#           of team members



##  Prompts the user for a project name and validates it.
#   @return a string containing the project name.
#
#   Invariants: a project name must be between the minimum and maximum length
#               and cannot be blank. The name must contain only alphabetic 
#               characters.
#           
def getProjectName() :
    projectName = input("\n\tEnter project name: ")
    
    while isValidName(projectName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :
        print(("\n\t\tThe project name must be more than {} characters long, "
               "less than {} characters long and must contain only "
               "alphabetic characters. Try again.\n")
               .format(MINIMUM_NAME_LENGTH - 1, MAXIMUM_NAME_LENGTH + 1))
        projectName = input("\n\tEnter project name: ")
    return projectName


# Check the string contains only characters from the alphabet and check that it is the right length.
# 
# @param theString the string to be validated
# @minimum the minimum length of the string
# @maximum the maximum length of the string
# @return True if the string conforms to the validation conditions and False if it does not.
#
def isValidName(theString, minimum, maximum) :

    return theString.isalpha() == True \
        and len(theString) >= minimum \
        and len(theString) <= maximum
    


##  Prompts the user for the team size and validates it.
#   @return the number of people in the team.
#
#   Invariants: the team size must be between the minimum and maximum size.
#
def getTeamSize() :
    teamSize = input("\n\tHow many people in the team: ")
    
    while isValidTeamSize(teamSize, MINIMUM_TEAM_SIZE, MAXIMUM_TEAM_SIZE) == False :
        print(("\n\t\tThe team size must be more than {} and less than {}. "
               "Try again.").format(MINIMUM_TEAM_SIZE - 1, MAXIMUM_TEAM_SIZE + 1))
        teamSize = input("\n\tHow many people in the team: ")

    return int(teamSize)



def isValidTeamSize(size, minimum, maximum):

    return isInteger(size) and int(size) >= minimum and int(size) <= maximum



def isInteger(number) :
    try: 
        int(number) 
        return True 
    except ValueError:
        return False


def getTeamNames(teamSize):
    teamNames = []
    i = 0
    while i <= teamSize:
        teamName = getPersonName()
        if teamName not in teamNames:
            teamNames.append(teamName)
            i = i + 1
        else:
            print("\n\t\tSorry, you already have a team member called {}, try again."
                  .format(teamName))
    return teamNames



def getPersonName() :
    personName = input("\n\tEnter name: ")
    
    while isValidName(personName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :
        print(("\n\t\tThe name must be more than {} characters long,"
               " less than {} characters long and cannot contain "
               "numbers or punctuation characters.").format(MINIMUM_NAME_LENGTH - 1,
                                                           MAXIMUM_NAME_LENGTH + 1))
        personName = input("\n\tEnter name: ")
    return personName



#Call the main function to begin the programme
menu()

# 00000000000000000000000000000000000000000000000000000000000000000000000000079
