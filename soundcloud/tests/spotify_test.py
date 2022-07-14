import pytest
import json

import sys
sys.path.insert(0, "./")

from utils.spotify import Spotify

def test_get_features_lucid():
    s = Spotify()
    actual = s.get_features("Lucid Dreams", "Juice WRLD")
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