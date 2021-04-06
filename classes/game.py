import os
import pathlib
import json

class GameController(object):
    """ handles game functions """
    players = []

    def setup_players(self):
        # setup players
        print("How many people will be traveling with you? (0-6)")

    def start(self):
        # initialize new game
        print("\nWelcome to the Maryland Trail!")
        print("On your journey you will have the opportunity to explore the Old Line State in all of its grandeur, with YOU deciding what to explore and how to explore it.")
        print("Make wise decisions and make the most of your trip. Safe travels!\n")
        self.setup_players()

    def load(self):
        # use loader to initialize saved game
        print("load")