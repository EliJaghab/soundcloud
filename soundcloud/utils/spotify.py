import spotipy
import json
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.exceptions import SpotifyException
from urllib.error import HTTPError

class Spotify():
    def __init__(self):
        self.client_id = "d22e1351aa4a4ddfb7c0550137efdd7a"
        self.client_secret = "7f23c73eb6cb447ea7dbb1840b43d778"
        self.client = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=self.client_id, client_secret = self.client_secret))
        self.null_response = {
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
    
    def get_features(self, sc_track: str, sc_artist = ""):

        def _get_track_id():

            def _search_track(sc_track = sc_track, sc_artist = sc_artist):
                try:
                    track_id_results = self.client.search(q='artist:' + sc_artist + ' track:' + sc_track, type='track')
                    return track_id_results
                except (SpotifyException, HTTPError) as error:
                    print(error)
                    return None

            def _get_track_id_basic():
                return _search_track()
            
            def _get_track_id_advanced():
                blank_artist = ""
                return _search_track(sc_artist = blank_artist)
            
            def _get_track_id_split_on_hyphen():
                if "-" in sc_track:
                    split_track = sc_track.rsplit("-", 1)
                    sc_artist = split_track[0]
                    sc_track = split_track[1]
                    return _search_track(sc_track, sc_artist)
                return None

            def _is_valid_response(results):
                if results:
                    if results['tracks']['items']:
                        return True
                return False

            track_id_results = _get_track_id_basic()
            if not _is_valid_response(track_id_results):
                track_id_results = _get_track_id_advanced()
            if not _is_valid_response(track_id_results):
                track_id_results = _get_track_id_split_on_hyphen()
            if not _is_valid_response(track_id_results):
                return None, None, None
            first_result = track_id_results['tracks']['items'][0]
            sp_track = first_result['name']
            sp_artist = first_result['artists'][0]['name']
            sp_track_id = first_result['external_urls']['spotify'][31:]
            return sp_track, sp_artist, sp_track_id

        def _get_features(sp_track: str, sp_artist: str, sp_track_id: str):
            sp_track, sp_artist, sp_track_id = _get_track_id()
            if sp_track_id:
                features = self.client.audio_features(sp_track_id)[0]
                if features: 
                    features['track_name'] = sp_track
                    features['artist_name'] = sp_artist
                else:
                    features = self.null_response
            else:
                features = self.null_response
            return features
        
        sp_track, sp_artist, sp_track_id = _get_track_id()
        return _get_features(sp_track, sp_artist, sp_track_id)
    