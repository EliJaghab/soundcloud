import pytest
import json

import sys
sys.path.insert(0, "./")

from utils.spotify import Spotify


def test_get_track_id_lucid():
    s = Spotify()
    actual = s.get_track_id("Lucid Dreams", "Juice WRLD")
    expected = "285pBltuF7vW8TeWk8hdRR"
    assert actual == expected

def test_get_track_id_roses():
    s = Spotify()
    actual = s.get_track_id("Roses", "benny")
    expected = "1KVczjazCcCCgM3gXXUl47"
    assert actual == expected

def test_get_track_id_unknown():
    s = Spotify()
    actual = s.get_track_id("@#$%@#$%", "@#$%@")
    expected = None
    assert actual == expected

def test_get_track_id_memories():
    s = Spotify()
    actual = s.get_track_id("Memories (feat. Kid Cudi) [2021 Remix] (2021 Remix)", "David Guetta")
    expected = "2ZivKpq32CqkNB7b2xiRO3"
    assert actual == expected

def test_get_track_id_split_example():
    s = Spotify()
    actual = s.get_track_id("Drake - A Keeper", "octobersveryown")
    expected = "0nAZGkBGKQCXyaoSJfRhC1"
    assert actual == expected

def test_get_track_id_giving_up():
    s = Spotify()
    actual = s.get_track_id("Giving Up (feat. Mafro)", "TSHA")
    expected = "61rELAKbEKXdidjxXviWd0"
    assert actual == expected


def test_get_features_giving_up(spotify_client):
    actual = spotify_client.get_features("Lucid Dreams", "Juice WRLD")
    f = open('tests/expected_responses/expected_lucid.json')
    expected = json.load(f)
    assert expected == actual

def test_get_features_roses():
    s = Spotify()
    actual = s.get_features("Roses", "benny")
    f = open('tests/expected_responses/expected_roses.json')
    expected = json.load(f)
    assert expected == actual

def test_get_features_unknown_song():
    s = Spotify()
    actual = s.get_features("@#$%@#$%", "@#$%@")
    f = open('tests/expected_responses/expected_unknown.json')
    expected = json.load(f)
    assert expected == actual

def test_get_features_memories():
    s = Spotify()
    actual = s.get_features("Memories (feat. Kid Cudi) [2021 Remix] (2021 Remix)", "David Guetta")
    f = open('tests/expected_responses/expected_unknown.json')
    expected = json.load(f)
    assert actual == expected

def test_get_features_split_example():
    s = Spotify()
    actual = s.get_features("Drake - A Keeper", "octobersveryown")
    f = open('tests/expected_responses/expected_keeper.json')
    expected = json.load(f)
    assert actual == expected


def test_get_features_giving_up():
    s = Spotify()
    actual = s.get_features("Giving Up (feat. Mafro)", "TSHA")
    f = open('tests/expected_responses/expected_keeper.json')
    expected = json.load(f)
    assert actual == expected
