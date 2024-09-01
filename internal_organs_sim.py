from config import *
import random


class Heart:

    _TYPE = 'Heart'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class Brain:

    _TYPE = 'Brain'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class kidney:

    _TYPE = 'Kidney'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class liver:

    _TYPE = 'Liver'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class Stomach:

    _TYPE = 'Stomach'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class Spleen:

    _TYPE = 'Spleen'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class Peepee:

    _TYPE = 'Peepee'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class Poopoo:

    _TYPE = 'Poopoo'

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }
    
    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def interact(self, other):
        pass

    def update(self):
        pass

    def get_state(self):
        pass

class Blood:

    _TYPE = "Blood"

    def __init__(self, condition, colour, side) -> None:
        self.condition = condition
        self.colour = colour
        self.side = side

        self.nutients = {
            "protein": 50,  # functions as a metric to rebuild the organ
            "oxygen": 50,  # functions as a way to tell if the organ is maintained (depends on blood flow)
            "nourished": 50  # functions as a general metric for how the organ is doing
        }

        # private variable to hold a list of all applicable functions that can be executed as an
        # interaction on the specified entity. e.g., blood flows to brain. if the blood has poison
        # which would be checked by one of the functions in the list, the brain would be affected accordingly.
        # this way, functions can be added and left as needed in the lists to be iterated over. They will be written
        # in another library to be imported.
        self._inter_funcs = {
            "Heart": [],
            "Brain": [],
            "Kidney": [],
            "Heart": [],
            "Heart": []
        }

    def get_type(self):
        return self._TYPE

    def repair(self):
        self.condition += self.nutrients['protein'] / 50 + random.randint(-10, 10) / 10
        if self.condition > 100:
            self.condition = 100 + (1 / (self.condition - 100))

    def get_inter_funcs(self, key):
        return self._inter_funcs[key]

    def interact(self, other):
        interact_key = other.get_type()
        interactables = self.get_inter_funcs(interact_key)
        for func in interactables:

            # the self keyword will be used to access this specific instance of the class
            func(self)

    def update(self):
        pass

    def get_state(self):
        pass