# player_node.py

from app.player import Player

class PlayerNode:
    """
    A node that can be used with a Doubly-Linked List of PlayerNode
    instances.
    """

    def __init__(self, player: Player):
        """
        Initialize a PlayerNode. Must provide a Player object.

        Args:
            player (Player): The player object for this node.

        Notes:
            A node is initialized with no connections.  Add nodes
             before and after this node with the next(...) and
             previous(...) functions.
        """

        # Explicit enforce None and correct type
        if player is None:  
            raise ValueError("Must provide PlayerNode instance!")

        self._player = player
        self._prev_player = None
        self._next_player = None

    @property
    def previous(self):
        """
        Get the linked PlayerNode before this node.

        Returns:
            PlayerNode: A node representing a player 
            OR None if at the head of the node sequence.
        """

        return self._prev_player

    @previous.setter
    def previous(self, player_node):
        """
        Set the linked PlayerNode before this node.

        Args:
            player_node (PlayerNode): The PlayerNode to be linked as the 
             previous node. Must not be None and must be an instance of
             PlayerNode.

        Raises:
            ValueError: If the node argument is not an instance of 
             PlayerNode or is None.

            ValueError: If the node argument is this node 

        Notes:
            Intended to be used in a Doubly Linked List structure. 
        """

        if player_node is None:
            raise ValueError("Must provide PlayerNode instance!")
        
        self._prev_player = player_node

    @previous.deleter
    def previous(self):
        """
        Clears the reference
        """
        
        self._prev_player = None

    @property
    def next(self):
        """
        Get the linked PlayerNode after this node.

        Returns:
            PlayerNode: A node representing a player 

            *Or None* if at the tail of the node sequence.
        """

        return self._next_player

    @next.setter
    def next(self, player_node):
        """
        Set the linked PlayerNode after this node.

        Args:
            player_node (PlayerNode): The PlayerNode to be linked as the 
             next node. Must not be None and must be an instance of
             PlayerNode.

        Raises:
            ValueError: If the node argument is None.

        Notes:
            Intended to be used in a Doubly Linked List structure. 
        """

        if player_node is None:
            raise ValueError("Must provide PlayerNode instance!")

        self._next_player = player_node

    @next.deleter
    def next(self):
        """
        Clears the reference
        """

        self._next_player = None

    @property
    def player(self):
        """
        Get the Player assosciated with this node.

        Returns:
            Player: An object representing a player.
        """

        return self._player
    
    @property
    def key(self) -> str:
        """
        Get the Player Unique ID assosciated with this node.

        Returns:
            str: A Unique ID string.
        """

        return self._player.uid
    
    def equals(self, other):
        """
        Equality check, compares:
        - node instance equals
        - node player instance equals
        - node player uid equals
        """
        if isinstance(other, PlayerNode):
            return (self == other or 
                    self.player == other.player or
                    self.key == other.key) 
        
        return False

    def __str__(self):
        current = self._player
        this_player_str = f"{current.uid} ({repr(current.name)})"
        
        previous = self._prev_player
        previous_str = "AT HEAD (No prior nodes)"
        if previous is not None:
            previous_str = f"{previous.key} ({repr(previous.player.name)})"

        next = self._next_player
        next_str = "AT TAIL (No more nodes)"
        if next is not None:
            next_str = f"{next.key} ({repr(next.player.name)})"
            
        return (
            f"PlayerNode([{this_player_str}], "
            f"Previous Node=[{previous_str}], "
            f"Next Node=[{next_str}] "
            f")"
        )
