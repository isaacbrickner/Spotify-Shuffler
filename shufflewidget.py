import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from tkinter import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import pandas as pd
import logging
import datetime
import numpy as np
import timeit
import time
import random




pp = pprint.PrettyPrinter(indent=4)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="c6d8222701234542ab1296cb5a242c46",
                                               client_secret="8800442a25954135b6c47a6696661602",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope="user-top-read user-library-read user-read-currently-playing user-follow-read user-read-playback-state user-modify-playback-state app-remote-control playlist-read-private"))

results = sp.current_user_saved_tracks()
top_tracks = sp.artist_top_tracks("0oSGxfWSnnOXhD2fKuz2Gy", 'US')
results = sp.current_user_top_artists(time_range='short_term', limit=20)
top_artists = sp.current_user_top_artists(20, 0, 'medium_term')
queue = sp.queue()
analysis = sp.audio_analysis(
    'https://open.spotify.com/track/13T8SvWHczyBPzOemKtEe7?si=21d4eefb66184d0d')
logger = logging.getLogger('examples.artist_recommendations')
logging.basicConfig(level='INFO')


def main():
    main_window = Tk()
    main_window.title('Spotify Shuffler')
    main_window.geometry("800x600+10+20")

    play_button = Button(main_window, text="Shuffle", fg="Black")
    play_button.pack(expand=True, side = LEFT)
    start = time.time()
    #play_new_song(random_liked_song())
    end = time.time()
    print(end - start,'seconds')
    change_volume()
    
def random_liked_song():
    random_song = sp.current_user_saved_tracks(1, random.randint(0, 4150))
    for i, item in enumerate(random_song['items']):
        playlist_ids = {
            'song_name': item['track']['album']['name'], 'uri': item['track']['album']['artists'][0]['uri'], 'artist_name': item['track']['album']['artists'][0]['name']}
    return playlist_ids

def play_new_song(rand_song): 
    parse_dict = rand_song 
    sp.start_playback(device_id=None, context_uri=parse_dict['uri'], uris=None, offset=None, position_ms=None)   

def resume_playing():
    sp.start_playback()
    
def pause():
    sp.pause_playback()
    
def last_track():
    sp.previous_track()
    
def change_volume(percent=0):
    while(True):
        try:
            print('enter value to change volume')
            vol_change = int(input())
            sp.volume(vol_change)
        except ValueError:
            print("Not an integer! Please enter an integer.")
            continue    
            
    
    
if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()









    
# def get_devices():
#     print(sp.devices())
#     return sp.devices()


# def get_liked_songs():
#     multiplier = 0
#     testarray = []
#     ls_playlist = [] 
#     for i in range(4200):
#         testarray.append(sp.current_user_saved_tracks(1, multiplier))
#         multiplier += 1    
#     for i in range(len(testarray)):
#         for i, item in enumerate(testarray[i]['items']):
#             playlist_ids = {
#                 'song_name': item['track']['album']['name'], 'uri': item['track']['album']['artists'][0]['uri'], 'artist_name': item['track']['album']['artists'][0]['name']}
#             ls_playlist.append(playlist_ids)
#     pp.pprint(ls_playlist)
    