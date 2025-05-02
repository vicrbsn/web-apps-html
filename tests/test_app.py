from lib.album import Album
from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

# test that html page accurate displays all the information of the albums present
def test_get_html_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    paragraph_tags = page.locator("p")
    expect(h2_tags).to_have_text(['Doolittle', 'Surfer Rosa', 'Waterloo'])
    expect(paragraph_tags).to_have_text(['Released: 1989', 'Released: 1988', 'Released: 1974'])


# test that getting a single album by album id returns the accurate information (multiple IDs used to show flexibility)
def test_get_single_album_html(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums/3")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text(['Waterloo'])
    expect(p_tags).to_have_text(['Released: 1974', 'Artist: ABBA'])

    page.goto(f"http://{test_web_address}/albums/1")
    h1_tags = page.locator("h1")
    p_tags = page.locator("p")
    expect(h1_tags).to_have_text(['Doolittle'])
    expect(p_tags).to_have_text(['Released: 1989', 'Artist: Pixies'])