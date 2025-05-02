class Album:
    # function to initialise the variables as self variables
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # ensure equality between self and other
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    # format the data 
    def __repr__(self):
        return f"Album ({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    