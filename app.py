import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist


# Create a new Flask app
app = Flask(__name__)

@app.route('/albums', methods=['GET'])
def post_html_albums():

    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    albums = repository.all()

    return render_template('music/index.html', albums=albums)

@app.route('/albums/<album_id>', methods=['GET'])
def get_album(album_id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)

    album = repository.find(album_id)[0] 
    artist = repository.find(album_id)[1]
    return render_template('music/album.html', album=album, artist=artist)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

