class CustomDictOne(dict):
    def __init__(self):
        super().__init__()
        self.Dict_Movies = []
    
    def set_movies(self, movies):
        self.Dict_Movies = movies
    
    def get_movies(self):
        return self.Dict_Movies