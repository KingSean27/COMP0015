# This module contains Project and Person class
import verify_funcs as vf

class Project:
    """The project class contains 3 
    atrributes a name, number of
    members and a list of team members"""

    MINIMUM_NAME_LENGTH = 3
    MAXIMUM_NAME_LENGTH = 10

    MINIMUM_TEAM_SIZE = 3
    MAXIMUM_TEAM_SIZE = 5

    def __init__(self, theName, theNoOfMems, theMembers=[]):
        self.name = theName
        self.NoOfMems = theNoOfMems
        self.members = theMembers

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, theName):
        self._name = theName

    @property
    def NoOfMems(self):
        return self._NoOfMems

    @NoOfMems.setter
    def NoOfMems(self, theNoOfMems):
        self._NoOfMems = theNoOfMems

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, theMembers):
        self._members = theMembers

    def __str__(self):
         return '{} {} {}'.format(self.name, self.NoOfMems, self.members)

    def getProjectName():
        """Receives an input for the team name
        from the user, verifies it is valid
        and returns the project name variable"""

        projectName = input("\n\tEnter project name: ")

        while vf.isValidName(projectName, vf.MINIMUM_NAME_LENGTH, vf.MAXIMUM_NAME_LENGTH) == False:
            print(("\n\t\tThe project name must be more than {} characters long, "
                   "less than {} characters long and must contain only "
                   "alphabetic characters. Try again.\n")
                  .format(MINIMUM_NAME_LENGTH - 1, MAXIMUM_NAME_LENGTH + 1))
            projectName = input("\n\tEnter project name: ")
        return projectName

    def getTeamSize():
        """Verifies an input team is acceptable
        and an integer of the team size"""

        teamSize = input("\n\tHow many people in the team: ")

        while Project.isValidTeamSize(teamSize, Project.MINIMUM_TEAM_SIZE, Project.MAXIMUM_TEAM_SIZE) == False:
            print(("\n\t\tThe team size must be more than {} and less than {}. "
                   "Try again.").format(Project.MINIMUM_TEAM_SIZE - 1, Project.MAXIMUM_TEAM_SIZE + 1))
            teamSize = input("\n\tHow many people in the team: ")

        return int(teamSize)

    def isValidTeamSize(size, minimum, maximum):
        """Verifies an input team is acceptable
        and returns a boolean"""

        return vf.isInteger(size) and int(size) >= minimum and int(size) <= maximum

    def getTeamNames(teamSize, projectName):
        """Returns a list containing the
        members of a team. Also creates
        the team membersand assigns them
        to the correct project name"""

        teamNames = []
        teamMembers = []
        i = 1
        while i <= teamSize:
            teamName = Person.getPersonName()
            if teamName not in teamNames:
                teamNames.append(teamName)
                teamMember = Person(theName=teamName, theProject=projectName, theVotes={})
                teamMembers.append(teamMember)
                i = i + 1

            else:
                print("\n\t\tSorry, you already have a team"
                      "member called {}, try again."
                      .format(teamName))
        return teamMembers


class Person:
    """The person class contains 3 
    atrributes the name of the project
    they are assigned to, their name and 
    their votes for other team members as 
    a dictionary"""

    def __init__(self, theProject, theName, theVotes={}):
        self.project = theProject
        self.name = theName
        self.votes = theVotes

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, theProject):
        self._project = theProject

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, theName):
        self._name = theName

    @property
    def votes(self):
        return self._votes

    @votes.setter
    def votes(self, theVotes):
        self._votes = theVotes


    def __str__(self):
        return '{} {} {}'.format(self.project, self.name, self.votes)

    def getPersonName():
        """Verifies a name input is acceptable
        and returns it if it is"""

        personName = input("\n\tEnter name: ")

        while vf.isValidName(personName, Project.MINIMUM_NAME_LENGTH, Project.MAXIMUM_NAME_LENGTH) == False:
            print(("\n\t\tThe name must be more than {} characters long,"
                   " less than {} characters long and cannot contain "
                   "numbers or punctuation characters.").format(Project.MINIMUM_NAME_LENGTH - 1,
                                                                Project.MAXIMUM_NAME_LENGTH + 1))
            personName = input("\n\tEnter name: ")
        return personName
