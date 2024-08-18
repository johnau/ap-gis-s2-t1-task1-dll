# player.py

class Player:
    """
    An object that represents a Player, with a unique identifier, and a
    name.
    """

    def __init__(self, uid: str, name: str):
        self.__uid = uid
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @property
    def name(self) -> str:
        return self.__name
    
    def __str__(self):
        return f"Player(id='{self.__uid}', name='{self.__name}')"