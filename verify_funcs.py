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



    
# Function from:
# Rae Harbird
# Deliverable 1 Sample Answer

def isValidName(theString, minimum, maximum) :
    """Verifies an input name is 
    acceptable and returns a boolean"""

    return theString.isalpha() == True \
           and len(theString) >= minimum \
           and len(theString) <= maximum

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
    def isInteger(number) :
        """Verifies an input is an integer"""

        try:
            int(number)
            return True
        except ValueError:
            return False

def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True




