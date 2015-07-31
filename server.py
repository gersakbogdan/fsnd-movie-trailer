import json
import movie
import app

def get_movies(filename):
    """Fetches movie information from a file.

    Retrieves movies details from the file given as parameter.

    Args:
        filename: A JSON file which contains the required movie information:
            title, year, story line, poster image url, trailer youtube url

    Returns:
        A list of Movie class instances
    """

    # Get movies details from the json file
    json_data = open(filename).read();
    movies_data = json.loads(json_data)

    # Create the list of movies
    movies = []
    for m in movies_data:
        movies.append(movie.Movie(m["title"], m["year"], m["storyline"], m["poster_image_url"], m["trailer_youtube_url"]))

    return movies

def main():
    """Application start point."""
    # Get movies list
    movies = get_movies('./data/movies.json')
    # Open movies page
    app.open_page(movies)

if __name__ == '__main__':
    main()
