from config import *

"""
this should definitely also use a json file to 
hold class/race information, npc stuff, att/def/etc
stats. this would probably make it more modular,
easier to maintain. chatboxes could also be stored in
this sprites file, with text stored in the json perhaps?

TODO:
i also should try to stick to proper conventions for classes
to keep it modular and readable. things like private attributes,
etc.

- can kind of achieve modularity if i implement
an interact method that gets called in the update method, 
which would essentially check its surroundings and interact
accordingly. for example, if there is a plant on an
adjacent tile, a herbivore might eat it if its hungry, etc.
"""

class Sprite:

    """
    holds all relevant sprite information
    and methods
    """
    
    def __init__(self) -> None:
        pass

class Class:

    """
    holds all information and methods
    for specific classes, like attack,
    defence, special moves, spells, etc

    may or may not inherit from a super class,
    or perhaps it is the super class
    """
    
    def __init__(self) -> None:
        pass

class Race:

    """
    similar to Class but for race.
    """

    def __init__(self) -> None:
        pass

class NPC(Sprite):

    """
    Npc-specific methods and information
    """
    
    def __init__(self, npc_class, race) -> None:
        super().__init__()
        self.npc_class = npc_class
        self.race = race

class Player(Sprite):

    """
    similar to the npc class,
    but contains specific player methods
    """
    
    def __init__(self, npc_class, race) -> None:
        super().__init__()
        self.npc_class = npc_class
        self.race = race

