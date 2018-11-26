class Project:

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
        return self._name

    @NoOfMems.setter
    def NoOfMems(self, theNoOfMems):
        self._NoOfMems = theNoOfMems

    @property
    def members(self):
        return self._name

    @members.setter
    def members(self, theMembers):
        self._members = theMembers

    def __str__(self):
        return self.name, self.NoOfMems, self.members


class Person:

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
        self._name = theVotes


    def __str__(self):
        return self.name, self.project, self.votes
