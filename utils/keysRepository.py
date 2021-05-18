import requests
import os
from flask import jsonify
import json


class KeysRepository(object):

    def __init__(self):
        self.keys_server = os.getenv("KEY_STORAGE")

    def _get_request(self, parameters: str):
        r = requests.get(f"{self.keys_server}{parameters}")
        if r.status_code == 200:
            return json.loads(r.content.decode("utf-8"))
        return json.loads(r.content.decode("utf-8"))

    def get_public_key(self, device_id: str):
        data = self._get_request(parameters=f"/query/{device_id}/")
        return data.get("data")

    def get_private_key(self, device_id: str):
        data = self._get_request(parameters=f"/query/private/{device_id}/")
        return data.get("data")
