class Artist:
    # initialise the self variables 
    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre 
    
    # ensure equality between self and other 
    def __eq__(self, other):
        return self.__dict__ == other.__dict__ 
    
    # format the data 
    def __repr__(self):
        return f"Artist ({self.id}, {self.name}, {self.genre})"