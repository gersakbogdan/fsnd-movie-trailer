class Movie():
    """Basic Movie class representation.

    Attributes:
        title: Movie title.
        year: Released year.
        storyline: Movie short description.
        poster_image: URL to movie poster.
        trailer_youtube: URL to movie trailer.
    """
    
    def __init__(self, title, year, storyline, poster_image, trailer_youtube):
        """Inits Movie class with title, year, storyline, poster and trailer."""

        self.title = title
        self.year = year
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
