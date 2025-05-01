from lib.album import *

def test_album_constructs():
    album = Album(1,'Stick Season', 2022, 1)
    assert album.id == 1
    assert album.title == 'Stick Season'
    assert album.release_year == 2022
    assert album.artist_id == 1

def test_albums_format_nicely():
    artist = Album(1,'Stick Season', 2022, 1)
    assert str(artist) == "Album (1, Stick Season, 2022, 1)"

def test_albums_are_equal():
    artist1 = Album(1,'Stick Season', 2022, 1)
    artist2 = Album(1,'Stick Season', 2022, 1)
    assert artist1 == artist2