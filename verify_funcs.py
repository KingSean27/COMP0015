import sic

## Constants
MINIMUM_NAME_LENGTH = 3
MAXIMUM_NAME_LENGTH = 10

MINIMUM_TEAM_SIZE = 3
MAXIMUM_TEAM_SIZE = 5

MIN_VOTES = 0
MAX_VOTES = 100

# Function from:
# Rae Harbird
# Deliverable 1 Sample Answer

def getProjectName() :
    """Receives an input for the team name 
    from the user, verifies it is valid
    and returns the project name variable"""

    projectName = input("\n\tEnter project name: ")

    while isValidName(projectName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :
        print(("\n\t\tThe project name must be more than {} characters long, "
               "less than {} characters long and must contain only "
               "alphabetic characters. Try again.\n")
              .format(MINIMUM_NAME_LENGTH - 1, MAXIMUM_NAME_LENGTH + 1))
        projectName = input("\n\tEnter project name: ")
    return projectName

    
# Function from:
# Rae Harbird
# Deliverable 1 Sample Answer

def isValidName(theString, minimum, maximum) :
    """Verifies an input name is 
    acceptable and returns a boolean"""

    return theString.isalpha() == True \
           and len(theString) >= minimum \
           and len(theString) <= maximum

            
# Function from:
# Rae Harbird
# Deliverable 1 Sample Answer

def getTeamSize() :
    """Verifies an input team is acceptable 
    and an integer of the team size"""

    teamSize = input("\n\tHow many people in the team: ")

    while isValidTeamSize(teamSize, MINIMUM_TEAM_SIZE, MAXIMUM_TEAM_SIZE) == False :
        print(("\n\t\tThe team size must be more than {} and less than {}. "
               "Try again.").format(MINIMUM_TEAM_SIZE - 1, MAXIMUM_TEAM_SIZE + 1))
        teamSize = input("\n\tHow many people in the team: ")

    return int(teamSize)

    
# Function from:
# Rae Harbird
# Deliverable 1 Sample Answer

def isValidTeamSize(size, minimum, maximum) :
    """Verifies an input team is acceptable 
    and returns a boolean"""

    return isInteger(size) and int(size) >= minimum and int(size) <= maximum

    
# Function adapted from:
# Rae Harbird
# Deliverable 1 Sample Answer

def isInteger(number) :
    """Verifies an input is an integer"""

    try:
        int(number)
        return True 
    except ValueError:
         return False

        
# Function adapted from:
# Rae Harbird
# Deliverable 1 Sample Answer

def getTeamNames(teamSize, projectName):
    """Returns a list containing the 
    members of a team. Also creates 
    the team membersand assigns them
    to the correct project name"""

    teamNames = []
    teamMembers = []
    i = 1
    while i <= teamSize:
        teamName = getPersonName()
        if teamName not in teamNames:
            teamNames.append(teamName)
            teamMember = sic.Person(theName=teamName, theProject=projectName, theVotes={})
            teamMembers.append(teamMember)
            i = i + 1

        else:
            print("\n\t\tSorry, you already have a team" 
                  "member called {}, try again."
                  .format(teamName))
    return teamMembers

    
# Function from:
# Rae Harbird
# Deliverable 1 Sample Answer

def getPersonName() :
    """Verifies a name input is acceptable 
    and returns it if it is"""

    personName = input("\n\tEnter name: ")

    while isValidName(personName, MINIMUM_NAME_LENGTH, MAXIMUM_NAME_LENGTH) == False :
        print(("\n\t\tThe name must be more than {} characters long,"
               " less than {} characters long and cannot contain "
               "numbers or punctuation characters.").format(MINIMUM_NAME_LENGTH - 1,
                                                                MAXIMUM_NAME_LENGTH + 1))
        personName = input("\n\tEnter name: ")
    return personName
   
   
def voteInput(number):
    """This verifies that a vote input is in 
    the allowable range and an integer """

    counter = False
    while counter == False:

        if isInteger(number) == True:
            number = int(number)
            if voteCheck(number) == True:
                counter = True
            else:
                print("\n\t\tPlease enter an integer between {} and {}"
                      .format(MIN_VOTES, MAX_VOTES))
                number = input("\n\tEnter votes: ")

        else:
            print("\n\t\tPlease enter an integer between {} and {}"
                  .format(MIN_VOTES, MAX_VOTES))
            number = input("\n\tEnter votes: ")

    return number


def voteCheck(number):
    """This verifies a vote input is 
    in the allowable range"""

    if number >= MIN_VOTES and number <= MAX_VOTES:
        return True
    else:
        return False
    number = input("\n\tEnter votes: ")


    # Rae Harbird
    # Deliverable 1 Sample Answer
    def isValidName(theString, minimum, maximum) :
        """Verifies an input name is 
        acceptable and returns a boolean"""

        return theString.isalpha() == True \
               and len(theString) >= minimum \
               and len(theString) <= maximum

            
    # Function from:
    # Rae Harbird
    # Deliverable 1 Sample Answer
    def getTeamSize() :
        """Verifies an input team is acceptable 
        and an integer of the team size"""

        teamSize = input("\n\tHow many people in the team: ")

        while Rae.isValidTeamSize(teamSize, MINIMUM_TEAM_SIZE, MAXIMUM_TEAM_SIZE) == False :
            print(("\n\t\tThe team size must be more than {} and less than {}. "
                   "Try again.").format(MINIMUM_TEAM_SIZE - 1, MAXIMUM_TEAM_SIZE + 1))
            teamSize = input("\n\tHow many people in the team: ")

        return int(teamSize)

    
    # Function from:
    # Rae Harbird
    # Deliverable 1 Sample Answer

    def isValidTeamSize(size, minimum, maximum) :
        """Verifies an input team is acceptable 
        and returns a boolean"""

        return Rae.isInteger(size) and int(size) >= minimum and int(size) <= maximum

    
    # Function from:
    # Rae Harbird
    # Deliverable 1 Sample Answer
    def isInteger(number) :
        """Verifies an input is an integer"""

        try:
            int(number)
            return True
        except ValueError:
            return False

        
    # Function adapted from:
    # Rae Harbird
    # Deliverable 1 Sample Answer
    def getTeamNames(teamSize, projectName):
        """Returns a list containing the 
        members of a team. Also creates 
        the team membersand assigns them
        to the correct project name"""

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

            else:
                print("\n\t\tSorry, you already have a team" 
                      "member called {}, try again."
                      .format(teamName))
        return teamMembers

    
    # Function from:
    # Rae Harbird
    # Deliverable 1 Sample Answer
    def getPersonName() :
        """Verifies a name input is acceptable 
        and returns it if it is"""

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
        """This verifies that a vote input is in 
        the allowable range and an integer """

        counter = False
        while counter == False:

            if Rae.isInteger(number) == True:
                number = int(number)
                if verif2.voteCheck(number) == True:
                    counter = True
                else:
                    print("\n\t\tPlease enter an integer between {} and {}"
                          .format(MIN_VOTES, MAX_VOTES))
                    number = input("\n\tEnter votes: ")

            else:
                print("\n\t\tPlease enter an integer between {} and {}"
                      .format(MIN_VOTES, MAX_VOTES))
                number = input("\n\tEnter votes: ")

        return number


    def voteCheck(number):
        """This verifies a vote input is 
        in the allowable range"""

        if number >= MIN_VOTES and number <= MAX_VOTES:
            return True
        else:
            return False
        number = input("\n\tEnter votes: ")

