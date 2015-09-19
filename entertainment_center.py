"""
This Python code creates a single-page movie review HTML
and launch it on the user's default browser.
"""

import fresh_tomatoes
import media
from datetime import date

___author___ = "Shinsuke Ikegame"

# Create new objects with data
bad_boys = media.Movie("Bad Boys",  # Movie title
                       "Whatcha gonna do?",  # Movie storyline
                       date(1995, 4, 7),  # Release date
                       ("https://upload.wikimedia.org/"
                        "wikipedia/en/a/a8/Bad_Boys.jpg"),  # Poster image URL
                       ("https://www.youtube.com/"
                        "watch?v=6GaPkMqAS44"))  # Youtube Trailer URL

bourne = media.Movie("The Bourne Identity",
                     "A marine on an alien planet",
                     date(2002, 6, 14),
                     ("https://upload.wikimedia.org/"
                      "wikipedia/en/a/ae/BourneIdentityfilm.jpg"),
                     "https://www.youtube.com/watch?v=cD-uQreIwEk")

hangover = media.Movie("The Hangover Part II",
                       "Bangkok has them now",
                       date(2011, 5, 26),
                       ("https://upload.wikimedia.org/"
                        "wikipedia/en/9/9d/HangoverPart2MP2011.jpg"),
                       "https://www.youtube.com/watch?v=RYL_T7f59o8")

school_of_rock = media.Movie("School of Rock",
                             "Storyline",
                             date(2003, 10, 3),
                             ("https://upload.wikimedia.org/"
                              "wikipedia/en/1/11/School_of_Rock_Poster.jpg"),
                             "https://www.youtube.com/watch?v=oP7kExN8LFA")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Storyline",
                                date(2011, 5, 11),
                                ("https://upload.wikimedia.org/"
                                 "wikipedia/en/9/9f/"
                                 "Midnight_in_Paris_Poster.jpg"),
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "Storyline",
                           date(2012, 3, 12),
                           ("https://upload.wikimedia.org/"
                            "wikipedia/en/4/4b/"
                            "Hunger_Games_Film_Poster.jpg"),
                           "https://www.youtube.com/watch?v=KmYNkasYthg")

# Insert objects into the array
movies = [bad_boys,
          bourne,
          school_of_rock,
          hangover,
          midnight_in_paris,
          hunger_games]

# Generate the HTML file and display on a browser
fresh_tomatoes.open_movies_page(movies)
