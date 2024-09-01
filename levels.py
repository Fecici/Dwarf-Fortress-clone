from config import *
"""
perhaps i need to make a json file containing all of the
level data. this would probably help a lot.
"""

class Level:
    def __init__(self, tilemap, level_id) -> None:
        self.level_id = level_id
        self.tilemap = tilemap

        # objects holding dynamic information
        self.doors_dict = {}
        self.npc_dict = {}