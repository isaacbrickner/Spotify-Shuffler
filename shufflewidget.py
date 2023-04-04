import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import time
import random

pp = pprint.PrettyPrinter(indent=4)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="482f4b048fb44d07962d5be42f20d1ce",
                                               client_secret="39f9aec6713c449e84be1e33be8f04f2",
                                               redirect_uri="http://127.0.0.1:9090",
                                               scope="user-top-read user-library-read user-read-currently-playing user-follow-read user-read-playback-state user-modify-playback-state app-remote-control playlist-read-private"))


def main():
    root = tk.Tk()
    app = MusicPlayer(master=root)
    app.mainloop()
    start = time.time()
    end = time.time()
    print(end - start, 'seconds')


class MusicPlayer(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.play_button = tk.Button(
            self, text="Shuffle", command=self.shuffle)
        self.play_button.pack(side="left")

        self.play_button = tk.Button(self, text="Play", command=self.play)
        self.play_button.pack(side="left")

        self.pause_button = tk.Button(
            self, text="Pause", command=self.pause,)
        self.pause_button.pack(side="left")

        self.prev_button = tk.Button(self, text="Prev", command=self.prev)
        self.prev_button.pack(side="left")

        self.slider = tk.Scale(self, from_=0, to=100,
                               orient="horizontal", command=self.slider_changed)
        self.slider.pack(side="bottom")

    def slider_changed(self, event):
        print(event)
        self.change_volume(event)

    def shuffle(rand_song):
        play_new_song(get_random_liked_song())
        print("New song shuffled.")

    def play(self):
        resume_playing()
        print("Play button pressed.")

    def pause(self):
        print("Pause button pressed.")
        sp.pause_playback()

    def prev(self):
        last_track()
        print("Prev button pressed.")

    def change_volume(self, val):
        vol_change = int(val)
        sp.volume(vol_change)


def get_total_liked_tracks():
    random_song = sp.current_user_saved_tracks(1, 0)
    trackcnt = random_song['total']
    print('number of liked songs:', trackcnt)
    return trackcnt


def get_random_liked_song():
    total_tracks = get_total_liked_tracks()
    random_song = sp.current_user_saved_tracks(
        1, random.randint(0, total_tracks))
    pp.pprint(random_song)
    for i, item in enumerate(random_song['items']):
        song_data = {
            'song_name': item['track']['album']['name'], 'uri': item['track']['album']['uri'], 'artist_name': item['track']['album']['artists'][0]['name']}
        pp.pprint(song_data['song_name'])
    return song_data


def play_new_song(rand_song):
    parse_dict = rand_song
    sp.start_playback(
        device_id=None, context_uri=parse_dict['uri'], uris=None, offset=None, position_ms=None)


def resume_playing():
    sp.start_playback()


def last_track():
    sp.previous_track()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
