# player.py

class Player:
    """
    An object that represents a Player, with a unique identifier, and a
    name.
    """

    def __init__(self, uid: str, name: str):
        self._uid = uid
        self._name = name

    @property
    def uid(self) -> str:
        return self._uid

    @property
    def name(self) -> str:
        return self._name
    
    def __str__(self):
        return f"Player(id={repr(self._uid)}, name={repr(self._name)})"