# This module contains the project and person class 

class Project:
    """The project class contains 3 
    atrributes a name, number of
    members and a list of team members"""

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
