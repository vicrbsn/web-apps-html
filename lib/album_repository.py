from lib.album import Album
from lib.artist import Artist

class AlbumRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * ' \
                                        'FROM albums')
        albums = []
        for row in rows:
            item = Album(row['id'], row['title'], row['release_year'], row['artist_id'])
            albums.append(item)
        return albums

    def create(self, album):
        self._connection.execute('INSERT INTO albums ' \
                                '(title, release_year, artist_id)' \
                                'VALUES(%s, %s, %s)' , [album.title, album.release_year, album.artist_id])
        
    
    def find(self, id):
        row = self._connection.execute('SELECT albums.id AS album_id, * ' \
                                        'FROM albums ' \
                                        'JOIN artists ON artists.id = albums.artist_id ' \
                                        'WHERE albums.id = %s', [id])
        
        album = Album(row[0]['album_id'], row[0]['title'], row[0]['release_year'], row[0]['artist_id'])
        artist = Artist(row[0]['artist_id'], row[0]['name'], row[0]['genre'])
        return [album, artist]