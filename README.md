# Music Time Machine

This project scrapes the Billboard Hot 100 chart for a specified date, searches for each song on Spotify, and creates a new private playlist with those songs.
## Getting started
Before running the script, you need to set up a Spotify Developer account and create an app to obtain a client ID and secret. Then, set those as environment variables in a __.env__ file in the same directory as the script:
```
SPOTIPY_CLIENT_ID=your-spotify-client-id
SPOTIPY_CLIENT_SECRET=your-spotify-client-secret
```
### Prerequisites
Before running the script, install the following dependencies:
* __beautifulsoup4__
* __requests__
* __spotipy__
* __python-dotenv__
### Authentication
This program uses the __Spotipy__ library for authentication. When you run the script for the first time, you will be prompted to authenticate the application through a webpage. The authentication token will be stored in token.txt for future use.
## Usage

* Run the script by running ``python filename.py`` in your terminal.  
* When prompted, enter the date in the format YYYY-MM-DD.
* The script will scrape the Billboard Hot 100 chart for that date and search for each song on Spotify. If a song is found, its URI will be added to a list. If not, will be skipped.
*  After all songs have been searched for, a new private playlist will be created on your Spotify account, named after the chosen date, with all of the songs found.
