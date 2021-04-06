import os
import pathlib
import json


class GameController(object):
    """ handles game functions """
    players = []

    def start():
        # initialize new game
        setup_players()

    def load():
        # use loader to initialize saved game
        print("load")

    def setup_players():
        # setup players
        print()