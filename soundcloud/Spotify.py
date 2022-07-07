import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

class SpotifyAPI():
    def __init__(self):
        self.client_id = "d22e1351aa4a4ddfb7c0550137efdd7a"
        self.client_secret = "7f23c73eb6cb447ea7dbb1840b43d778"
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.client_id, client_secret = self.client_secret))
    
    def get_features(self, track: str, artist: str):

        def _get_track_i(self):
            track_id_results = self.client.search(q='artist:' + artist + ' track:' + track, type='track')
            try:
                first_result = track_id_results['tracks']['items'][0]
                track_name = first_result['name']
                track_artist = first_result['artists'][0]['name']
                track_id = first_result['external_urls']['spotify'][31:]
            except IndexError:
                pprint(track_id_results)
            return track_name, track_artist, track_id
        
        def _get_features(self):
            track, artist, track_id = _get_track_id(self)
            features = self.client.audio_features(track_id)[0]
            features['track_name'] = track
            features['artist_name'] = artist
            return features
        
        return _get_features(self)