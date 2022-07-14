import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

class Spotify():
    def __init__(self):
        self.client_id = "d22e1351aa4a4ddfb7c0550137efdd7a"
        self.client_secret = "7f23c73eb6cb447ea7dbb1840b43d778"
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.client_id, client_secret = self.client_secret))
    
    def get_features(self, track: str, artist: str):

        def _get_track_id(self):
            track_id_results = self.client.search(q='artist:' + artist + ' track:' + track, type='track')
            if track_id_results['tracks']['items']:
                first_result = track_id_results['tracks']['items'][0]
                track_name = first_result['name']
                track_artist = first_result['artists'][0]['name']
                track_id = first_result['external_urls']['spotify'][31:]
                return track_name, track_artist, track_id
            return None, None, None
            
        def _get_features(self):
            track, artist, track_id = _get_track_id(self)
            if track_id:
                features = self.client.audio_features(track_id)[0]
                features['track_name'] = track
                features['artist_name'] = artist
            else:
                features = {
                    "track_name": None,
                    "artist_name": None,
                    "danceability": None,
                    "energy": None,
                    "key": None,
                    "loudness": None,
                    "mode": None,
                    "speechiness": None,
                    "acousticness": None,
                    "instrumentalness": None,
                    "liveness": None,
                    "valence": None,
                    "tempo": None,
                    "type": None,
                    "id": None,
                    "uri": None,
                    "track_href": None,
                    "analysis_url": None,
                    "duration_ms": None,
                    "time_signature": None,
                    "track_name": None,
                    "artist_name": None
                }
            return features
            
        return _get_features(self)