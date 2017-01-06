import webbrowser

class Movie():
    """ This class provides a way to store movie related information"""
    
    def __init__(self, movie_title, movie_stars, movie_storyline, poster_image, trailer_youtube, movie_duration, movie_rating):
        self.title = movie_title
        self.stars = movie_stars
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = movie_duration
        self.rating = movie_rating
        
