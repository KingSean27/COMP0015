# 00000000000000000000000000000000000000000000000000000000000000000000000000079
 

# imports modules used
import time
import os
from rae import Rae
import sic

# constants 
MAX_VOTES = 100   

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

    app_open = "*"
  
    while app_open != "q": 
        global menu_choice
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
            app_open = "q"
        else:
            print("Please choose again")
            time.sleep(2)
            menu_screen ()
            
            
def menu():
    global project_dict
    project_dict = {}
    menu_screen()
    menu_redirect()

###############  ################################################  ####################  ###############
def enter_votes():
    """This looks up the project and lets members enter votes"""

    os.system('clear')
    global menu_choice
    global project_dict
    menu_choice = ""
    
    lookup = str(input("Enter the project name: " ))
    
    if lookup in project_dict:
        number = project_dict[lookup].NoOfMems
        proname = project_dict[lookup].name
        #promembers = project_dict[lookup].members
        print("There are {} team members in {}".format(number, proname))
        
        #print (promembers)
        i = 0
        
        while i < number:
          askvote1 = project_dict[lookup].members[i].name
          #print(askvote1)
          print ("Enter {}'s points the number must add up to 100".format(askvote1))
          
          for item in project_dict[lookup].members:
            askvote2 = str(item.name)
            
            if askvote1 == askvote2:
              print (".")
            else:
              vote = input (" Enter {}'s points for {} ".format(askvote1, askvote2))
              
              
            
          i = i + 1
        else: 
          print ("All votes have been successfully entered")
          
        input("\n\nPress the any key to return to main menu.")  
        
        
        
    else:
        print ("This project does not exist in the database")
        
    
    
    time.sleep(5)
    menu_screen()
###########   ####################################################  ##################  ###############

def show_projects():
    """This displays a message for two seconds then clears the console."""
    
    os.system('clear')
    global menu_choice
    menu_choice = ""
    print("New features coming soon!")
    time.sleep(2)
    menu_screen()


def about():
    """This displays information about the programme and returns
    to the menu screen on the user's command """

    os.system('clear')
    global menu_choice
    menu_choice = ""
    print("This is Split-it a coursework marking app")
    input("\n\nPress any key followed by <Enter> to return to the main menu.")
    menu_screen()
    

def create_project():
    """This function allows the user to
    add a new team and participants."""

    os.system('clear')
    global menu_choice
    menu_choice = ""
    projectName = Rae.getProjectName()
    teamSize = Rae.getTeamSize()
    members = Rae.getTeamNames(teamSize, projectName)

    global project_dict
    project_dict = {}
    project_dict[projectName] = sic.Project(theName=projectName, theNoOfMems=teamSize, theMembers=members)

  
    input("\n\nPress the any key to return to main menu.")
    menu_screen()
    


#Call the main function to begin the programme
menu()

# 00000000000000000000000000000000000000000000000000000000000000000000000000079
