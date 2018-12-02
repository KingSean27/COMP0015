#  Author: Rae Harbird
#  Date: November 2018
# Used to validate team member's name and project name

import sic

## Constants
MINIMUM_NAME_LENGTH = 3
MAXIMUM_NAME_LENGTH = 10

MINIMUM_TEAM_SIZE = 3
MAXIMUM_TEAM_SIZE = 5

MIN_VOTES = 0
MAX_VOTES = 100

##  Sets up a project from the information entered by the user.  
#   @return a tuple containing the project name and the names
#           of team members
class Rae:



##  Prompts the user for a project name and validates it.
#   @return a string containing the project name.
#
#   Invariants: a project name must be between the minimum and maximum length
#               and cannot be blank. The name must contain only alphabetic 
#               characters.
#           
    def getProjectName() :
        projectName = input("\n\tEnter project name: ")

        while Rae.isValidName(projectName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :
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

        while Rae.isValidTeamSize(teamSize, MINIMUM_TEAM_SIZE, MAXIMUM_TEAM_SIZE) == False :
            print(("\n\t\tThe team size must be more than {} and less than {}. "
                   "Try again.").format(MINIMUM_TEAM_SIZE - 1, MAXIMUM_TEAM_SIZE + 1))
            teamSize = input("\n\tHow many people in the team: ")

        return int(teamSize)



    def isValidTeamSize(size, minimum, maximum) :

        return Rae.isInteger(size) and int(size) >= minimum and int(size) <= maximum



    def isInteger(number) :
        try:
            int(number)
            return True
        except ValueError:
            return False


    def getTeamNames(teamSize, projectName):
        teamNames = []
        teamMembers = []
        i = 1
        while i <= teamSize:
            teamName = Rae.getPersonName()
            if teamName not in teamNames:
                teamNames.append(teamName)
                teamMember = sic.Person(theName=teamName, theProject=projectName, theVotes={})
                teamMembers.append(teamMember)
                i = i + 1
                # TODO: the project should have the right project name!!!!
            else:
                print("\n\t\tSorry, you already have a team member called {}, try again."
                      .format(teamName))
        return teamMembers



    def getPersonName() :
        personName = input("\n\tEnter name: ")

        while Rae.isValidName(personName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :
            print(("\n\t\tThe name must be more than {} characters long,"
                   " less than {} characters long and cannot contain "
                   "numbers or punctuation characters.").format(MINIMUM_NAME_LENGTH - 1,
                                                               MAXIMUM_NAME_LENGTH + 1))
            personName = input("\n\tEnter name: ")
        return personName

class verif2:

    def voteInput(number):

        counter = False
        while counter == False:

            if Rae.isInteger(number) == True:
                number = int(number)
                if verif2.voteCheck(number) == True:
                    counter = True
                else:
                    print(("\n\t\tPlease enter an integer between {} and {}").format(MIN_VOTES, MAX_VOTES))
                    number = input("\n\tEnter votes: ")

            else:
                print(("\n\t\tPlease enter an integer between {} and {}").format(MIN_VOTES, MAX_VOTES))
                number = input("\n\tEnter votes: ")
                
        return number


    def voteCheck(number):
        if number >= MIN_VOTES and number <= MAX_VOTES:
            return True
        else:
            return False
        number = input("\n\tEnter votes: ")

