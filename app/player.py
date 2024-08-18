class Player:
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
        return f"Player(id='{self._uid}', name='{self._name}')"