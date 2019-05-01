from card import *
import json
class Bank:
    def __init__(self):
        with open("game_info.json", "r") as json_file:
            data = json.load(json_file)
        self.resource_cards = data['resource_cards']
        self.development_cards = data['development_cards']