import sic

## Constants
MINIMUM_NAME_LENGTH = 3
MAXIMUM_NAME_LENGTH = 10

MINIMUM_TEAM_SIZE = 3
MAXIMUM_TEAM_SIZE = 5

MIN_VOTES = 0
MAX_VOTES = 100

    
# Rae Harbird
# Deliverable 1 Sample Answer

def isValidName(theString, minimum, maximum) :
    """Verifies an input name is 
    acceptable and returns a boolean"""

    return theString.isalpha() == True \
           and len(theString) >= minimum \
           and len(theString) <= maximum


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

def isInteger(number) :
    """Verifies an input is an integer"""

    try:
        int(number)
        return True
    except ValueError:
        return False
    
def isValidTeamSize(size, minimum, maximum) :
    """Verifies an input team is acceptable 
    and returns a boolean"""

    return isInteger(size) and int(size) >= minimum and int(size) <= maximum

        
def is_empty(any_structure):
    'Checks whether a list is empty'
    if any_structure:
        return False
    else:
        return True
    

    
def cutter(project_dict):

    for item in project_dict:
        masterstring = ''
        lookup = project_dict[item].name
        masterstring += (project_dict[item].name) + ','
        masterstring += str((project_dict[item].NoOfMems)) + ','
        
        i = 0
        for item in project_dict[lookup].members:
                masterstring += project_dict[lookup].members[i].name + ','
                i += 1
        
        i = 0
        for item in project_dict[lookup].members:
                masterstring += project_dict[lookup].members[i].name + ','
                votestring = str(project_dict[lookup].members[i].votes)
                votestring = votestring.replace('{', '')
                votestring = votestring.replace('}', '')
                votestring = votestring.replace(':', '')
                
                votelist = votestring.split()
                votestring = ''
                j = 0
                
                for item in votelist:
                    word = item
                    if j == 0: 
                        word = word[1:-1]
                        word = str(word)
                        votestring += word + ','                   
                        j += 1
                    else:
                        if word [-1:] == ',':
                            word = word[:-1]
                            word = str(word)
                        else: 
                            word = str(word)  
                        votestring += word + ','
                        j += -1 
                
                masterstring += votestring 
                i += 1
                
        print (masterstring) 
