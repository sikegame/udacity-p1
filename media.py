"""
Create Movie class
"""

import webbrowser


class Movie():
    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 release_date, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.release_date = release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Show Youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
