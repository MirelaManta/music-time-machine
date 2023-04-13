from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv.main import load_dotenv
import os

load_dotenv()
spotipy_client_id = os.environ["SPOTIPY_CLIENT_ID"]
spotipy_client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]

# Scraping Billboard 100
date_choice = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = f"https://www.billboard.com/charts/hot-100/{date_choice}"
response = requests.get(url=URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
song_names_span = soup.find_all("h3", class_="a-no-trucate", id="title-of-a-story")
song_names = [song.getText().strip() for song in song_names_span]
# print(song_names)

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    redirect_uri="http://example.com",
    client_id=spotipy_client_id,
    client_secret=spotipy_client_secret,
    show_dialog=True,
    cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

# Searching Spotify for songs by title
song_URIs = []
for song in song_names:
    result = sp.search(q=f"track:{song} year {date_choice.split('-')[0]}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_URIs.append(uri)
    except IndexError:
        print(f"{song} doesn't exist on spotify. Skipped.")

# Creating new private playlist in Spotify
new_playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date_choice} Billboard 100",
    public=False,
)

print(new_playlist)
# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_URIs)
