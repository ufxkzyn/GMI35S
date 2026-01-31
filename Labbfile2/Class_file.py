class CustomDictOne(dict):
    def __init__(self):
        super().__init__()
        self.List_Movies = []
    
    def set_movies(self, movies):
        self.List_Movies = movies
    
    def get_movies(self):
        return self.List_Movies
