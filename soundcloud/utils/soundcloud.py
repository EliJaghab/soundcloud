import json 

from soundcloud import SoundCloud

class SoundCloudAPI():
    def __init__(self):
        self.client_id = "ZA68dFpqtNM36uKAmylwTlo5n0KjJ140"
        self.auth_token = "2-293488-62408522-LPj8q4Jqxfkhq3A"
        self.client = SoundCloud(self.client_id, self.auth_token)
    
    def validate_client(self):
        return self.client.is_client_id_valid(), self.client.is_auth_token_valid()
    
    def get_user_id_from_profile_name(self, name: str):
        first_result = next(self.client.search_users(name))
        user_id = first_result.id
        return user_id


        