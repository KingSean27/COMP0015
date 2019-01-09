import sic

class Calcs_member:
    """This class contains the name and votes for each class member"""

    def __init__(self, theName, theVotes):
        self.name = theName
        self.votes = theVotes

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
        return "{} {}".format(self.name, self.votes)


def vote_extractor(member_list, member_name):
    """Extracts votes for a candidate from the other candidates
    in a list"""

    votes = []

    for item in member_list:
        if item != member_name:
            for key in item.votes:
                if key == member_name:
                    votes.append((item.name, item.votes[key]))

    return votes

def member_creator(theLookup, search_dict, index=0, ):
    """Creates a new calcs_member for each object in the member
    list which can be processed in calculations more easily"""

    member_list = search_dict[theLookup].members

    member_name = member_list[index].name

    votes = vote_extractor(member_list=member_list, member_name=member_name)

    calcs_member = Calcs_member(theName=member_name, theVotes=votes)

    return calcs_member

def score_calc(calc_member):
    """Calculates the point allocation for a member
    based on the votes stored in the object"""

    vote1 = (100 - calc_member.votes[0][1]) / calc_member.votes[0][1]
    vote2 = (100 - calc_member.votes[0][1]) / calc_member.votes[1][1]

    score = 1/(1 + vote1 + vote2)

    return round(score*100)