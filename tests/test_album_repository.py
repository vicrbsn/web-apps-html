from lib.album_repository import AlbumRepository
from lib.album import Album

def test_get_all_records(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    albums = repository.all()
    assert albums[0].title == 'Doolittle'
    assert albums[2].release_year == 1974

def test_create_record(db_connection):
    db_connection.seed('seeds/music_library.sql')
    repository = AlbumRepository(db_connection)
    repository.create(Album(None, 'Noah Kahan', 2022, 5))
    result = repository.all()
    assert str(result[-1]) == 'Album (4, Noah Kahan, 2022, 5)'
