import pytest

import sys
sys.path.insert(0, "./")

from utils.soundcloud import SoundCloudAPI

def test_validate_client_credentials():
    sc = SoundCloudAPI()
    client_id_is_valid, auth_token_is_valid = sc.validate_client()
    assert client_id_is_valid
    assert auth_token_is_valid

def test_get_user_id_from_profile_name():
    sc = SoundCloudAPI()
    expected = 62408522
    actual = sc.get_user_id_from_profile_name("Eli Jaghab")
    assert expected == actual