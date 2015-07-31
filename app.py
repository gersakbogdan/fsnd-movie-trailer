import os
import re
import webbrowser

def get_template(tpl_name):
    """Gets template file content.

    Opens and reads the content of the given template.

    Args:
        tpl_name: Name of the template file without extension.

    Returns:
        A string representing template content.
    """
    tpl_file = open('./templates/' + tpl_name + '.tpl')
    content = tpl_file.read()

    return content

def create_movie_tiles_content(tpl, movies):
    """Generates html content.

    Generates a formatted string using the template and the list of movies
    received as parameters.

    Args:
        tpl: A string to use as template for html.
        mmovies: A list of Movie class instances.

    Returns:
        A formatted string representing the movie tiles HTML.
    """

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += tpl.format(
            movie_title=movie.title,
            movie_year=movie.year,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_page(movies):
    """Generate main index page.

    Creates and opens into a web browser an HTML page using the list of
    movies received as parameter.

    Args:
        movies: A list of Movie class instances.
    """

    # Retrieve templates content
    head_tpl = get_template('head')
    modal_tpl = get_template('modal')
    movie_tile_tpl = get_template('movie_tile')
    main_tpl = get_template('main')
    index_tpl = get_template('index')
    footer_tpl = get_template('footer')

    # Create or overwrite index.html file
    index_file = open('index.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_tpl.format(movie_tiles=create_movie_tiles_content(movie_tile_tpl, movies))
    index_content = index_tpl.format(
                        head_template=head_tpl,
                        main_template=rendered_content,
                        modal_template=modal_tpl,
                        footer_template=footer_tpl)

    # Write content into index file
    index_file.write(index_content)
    index_file.close()

    # Open index file in the browser
    url = os.path.abspath(index_file.name)
    webbrowser.open('file://' + url, new = 2) # open in a new tab, if possible
