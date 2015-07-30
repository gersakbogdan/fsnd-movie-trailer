import json
import movie
import app

# Get movies details from json file
json_data = open('./data/movies.json').read();
movies_data = json.loads(json_data)

# Create the list of movies
movies = []
for m in movies_data:
    movies.append(movie.Movie(m["title"], m["storyline"], m["poster_image_url"], m["trailer_youtube_url"]))

# Open movies page
app.open_page(movies)
