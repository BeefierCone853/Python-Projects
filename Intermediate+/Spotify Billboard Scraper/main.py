import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# User input for date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Get the webpage and scrape the data
URL = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
div_songs = soup.find_all("div", class_="o-chart-results-list-row-container")

song_titles_artists = []
for div in div_songs:
    song_title = div.find("h3", class_="c-title", id="title-of-a-story")
    song_artist = div.find("span", class_="a-no-trucate")
    song_titles_artists.append(song_title.getText().strip() + " " + song_artist.getText().strip())

song_titles = [song.replace("'", "") for song in song_titles_artists]

# print(song_titles) #Check song titles

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ["NT_CLIENT_ID"],
                                               client_secret=os.environ["NT_CLIENT_SECRET"],
                                               redirect_uri=os.environ["NT_REDIRECT_URI"],
                                               scope="playlist-modify-public"))

# Create playlist, get song URIs and add them to the created playlist
song_uri = []
playlist_name = f"Spotify Billboard {date}"
user_id = sp.current_user()["id"]
playlist_exists = False
print("Checking if playlist with that name exists.")
for playlist in sp.current_user_playlists()["items"]:
    if playlist["name"] == playlist_name:
        playlist_exists = True

if playlist_exists:
    print("Playlist with that name already exists.")

else:
    print("Creating playlist.")
    playlist = sp.user_playlist_create(user_id, playlist_name)
    playlist_id = playlist["id"]
    print(f"Searching for Billboard 100 on date : {date}")
    for song in song_titles:
        searchResults = sp.search(song)
        song_uri.append(searchResults["tracks"]["items"][0]["uri"])

    try:
        print("Addings songs to playlist.")
        sp.playlist_add_items(playlist_id = playlist_id, items = song_uri)
        print("Success! Check your Spotify playlists.")

    except spotipy.SpotifyException:
        print("There was an error.")
