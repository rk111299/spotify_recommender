import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth  


def connect_to_spotipy():
    CLIENT_ID = '6a08a6a5318d46b3a866b129491f2c59' 
    CLIENT_SECRET = '0a0cfdc3861d47989744668795c73bd4'
    REDIRECT_URI = 'http://localhost:8888/callback'
    SCOPE = None
    AUDIO_FEATURES_ENDPOINT = 'https://api.spotify.com/v1/audio-features/{id}'

    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE)  

    sp = spotipy.Spotify(auth_manager=sp_oauth)

    return sp

def albums_test(sp):
    radiohead = 'spotify:artist:4Z8W4fKeB5YxbusRsdQVPb'

    results = sp.artist_albums(radiohead, album_type='album')
    albums = results['items']
    while results['next']:
        results = sp.next(results)
        albums.extend(results['items'])

    for album in albums:
        print(album['name'])


def get_track_info(track_uri_column):

    # get only unique track uris for those that I have listened to 
    unique_tracks = track_uri_column.unique()

    # empty list
    features_list = []

    for i in unique_tracks:
        
        # get track info as a dict
        track_info_dict = sp.audio_features(i)[0]

        # delete unnecessary cols
        del track_info_dict['type']
        del track_info_dict['id']
        del track_info_dict['track_href']
        del track_info_dict['analysis_url']
        
        # append to list
        features_list.append(track_info_dict)

    # list to df
    track_info_df = pd.DataFrame(features_list)

    track_info_df = track_info_df.rename(columns={'uri': 'spotify_track_uri'})

    return(track_info_df)