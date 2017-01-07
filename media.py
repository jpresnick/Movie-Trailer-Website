import webbrowser
class Video():
    """ This class provides a way to store video related information"""
    def __init__(self, video_title, video_storyline, poster_image, trailer_youtube):
        self.title = video_title
        self.storyline = video_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
            
class Movie(Video):
    """ This class provides a way to store movie specific information"""
    
    def __init__(self, movie_title, movie_stars, movie_storyline, poster_image, trailer_youtube, movie_duration, movie_rating):
        Video.__init__(self, movie_title, movie_storyline, poster_image, trailer_youtube)
        self.stars = movie_stars
        self.duration = movie_duration
        self.rating = movie_rating
        
class Tvshow(Video):
    """ This class provides a way to store tv show specific information"""

    def __init__(self, tvshow_title, tvshow_storyline, poster_image, trailer_youtube, tvshow_network):
        Video.__init__(self, tvshow_title, tvshow_storyline, poster_image, trailer_youtube)
        self.network = tvshow_network
