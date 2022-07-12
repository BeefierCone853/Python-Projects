# *Spotify Billboard Scraper*

Scrapes all the songs name and artist from the billboard chart on the entered date. 
Once the data is scraped, authentication is done using the *Spotipy* module in order to search for the songs on Spotify
and create a playlist for the user. All of the information needed for authentication are saved as environment variables.

**Note: some of the songs found on the billboard chart might not be available on Spotify, so wrong songs may be added
onto the playlist.**
