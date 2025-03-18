class Soccer_Team:
    
    """This class reprents a Soccer Team with a name, country, division, roster, and win/draw/loss record"""

    def __init__(self, name: str, country: str, division: int, record = (0, 0, 0)):

        """Initializes a new team
        
        Parameters:

        Name: string, name of the team.
        Country: string, country of the team
        Divison: string, divison of the team
        record: tuple, win/draw/tie record of the team

        Roster is a seperate list variable
        
        """

        self.name = name
        self.country = country
        self.division = division
        self.roster = []
        self.record = record

    
    def addto_roster(self, player, number):
        
        """Adds a player to the roster with a number

        Parameters:
        
        player: string, the players name
        number: string, the players number
        """

        self.roster.append((player, number))
        print(f"{player}, #{number}, has been added to the {self.name} roster!")
    
    def removefrom_roster(self, player, number):

        """Removes a player from the roster
        
        Parameters:
        
        player: string, the players name
        number: string, the players number"""

        if (player, number) in self.roster:
            print(f"{player}, number {number}, has been removed from the {self.name} roster!")
            self.roster.remove((player, number))
        else:
            print("Player not found")
    
    def set_record(self, wins, draws, losses):

        """Sets the win/draw/loss record for the team
        
        Parameters:
        
        Wins: Int, wins
        Draws: int, draws
        Losses: int, losses
        """
        
        self.record = (wins, draws, losses)

    def print_info(self):

        """Prints info about the team"""

        print(f"{self.name} is a division {self.division} team in {self.country}")
        print(f"HERE IS THE {self.name.upper()} STARTING ROSTER: ")
        for i in range(len(self.roster)):
            print(f"""{self.roster[i][0]} ------------------------------------------------- #{self.roster[i][1]}""")
        print(f"THEY HAVE A REGULAR SEASON RECORD OF {self.record[0]} WIN(S), {self.record[1]} DRAW(S), AND {self.record[2]} LOSS(ES).")

def main():

    #obviously these teams have way more people, and it's possible to add them, but this is just a demo for the classes

    LA_Galaxy = Soccer_Team("LA Galaxy", "America", "1")

    LA_Galaxy.addto_roster("Landon Donovan", "10")
    LA_Galaxy.addto_roster("David Beckham", "23")
    LA_Galaxy.addto_roster("Gabriel Pec", "11")

    LA_Galaxy.set_record(0, 1, 3)

    LA_Galaxy.print_info()



    Liverpool = Soccer_Team("Liverpool", "England", "1")

    Liverpool.addto_roster("Mo Salah", "11")
    Liverpool.addto_roster("Darwin Nunez", "9")
    Liverpool.addto_roster("Virgil Van Dijk", "4")
    Liverpool.addto_roster("Im not a real player", "190281")
    Liverpool.removefrom_roster("Im not a real player", "190281")

    Liverpool.set_record(21, 7, 1)

    Liverpool.print_info()


main()