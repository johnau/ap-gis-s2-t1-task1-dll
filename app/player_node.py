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
        if player is None or not isinstance(player, Player):  
            raise ValueError("Must provide PlayerNode instance!")  # Ignore unreachable IDE hint...

        self.__player = player
        self.__prev_player = None  # is 'last' more "pythonic" than 'prev'?
        self.__next_player = None

    @property
    def previous(self):
        """
        Get the linked PlayerNode before this node.

        Returns:
            PlayerNode: A node representing a player 
            OR None if at the head of the node sequence.
        """

        return self.__prev_player

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

        # Ensure not None and correct object type.
        if player_node is None or not isinstance(player_node, PlayerNode):
            raise ValueError("Must provide PlayerNode instance!")
        
        # Ensure node is not added to itself. 
        # ? Perhaps this logic is better suited in the DoublyLinkedList 
        # implementation, as it should set it's own rules.
        # > Leaving for now as it is not unreasonable...
        if player_node is self:
            raise ValueError("Cannot link a node to itself!")
        
        self.__prev_player = player_node

    @previous.deleter
    def previous(self):
        """
        Sets the previous node to None.
        """
        
        self.__prev_player = None

    @property
    def next(self):
        """
        Get the linked PlayerNode after this node.

        Returns:
            PlayerNode: A node representing a player 

            *Or None* if at the tail of the node sequence.
        """

        return self.__next_player

    @next.setter
    def next(self, player_node):
        """
        Set the linked PlayerNode after this node.

        Args:
            player_node (PlayerNode): The PlayerNode to be linked as the 
             next node. Must not be None and must be an instance of
             PlayerNode.

        Raises:
            ValueError: If the node argument is not an instance of 
             PlayerNode or is None.

            ValueError: If the node argument is this node 

        Notes:
            Intended to be used in a Doubly Linked List structure. 
        """

        # Ensure not None and correct object type
        if player_node is None or not isinstance(player_node, PlayerNode):
            raise ValueError("Must provide PlayerNode instance!")
        
        # Ensure node is not added to itself.
        # ? Perhaps this logic is better suited in the DoublyLinkedList 
        # implementation, as it should set it's own rules.
        # > Leaving for now as it is not unreasonable...
        if player_node is self:
            raise ValueError("Cannot link a node to itself!")

        self.__next_player = player_node

    @next.deleter
    def next(self):
        """
        Sets the next node to None.
        """

        self.__next_player = None

    @property
    def player(self):
        """
        Get the Player assosciated with this node.

        Returns:
            Player: An object representing a player.
        """

        return self.__player
    
    @property
    def key(self) -> str:
        """
        Get the Player Unique ID assosciated with this node.

        Returns:
            str: A Unique ID string.
        """

        return self.__player.uid
        
    def __str__(self):
        """
        Returns a string representation of this object instance, 
        including:
        - Previous node's Player Name and Unique ID (if there is one)
        - This node Player Name and Unique ID
        - Next node's Player Name and Unique ID (if there is one)

        Returns:
            str: A string representation of this object instance
        """

        # Create current node string
        current = self.__player                     # Can't be equal to None
        this_player_str = f"{current.uid} ('{current.name}')"
        
        # Create default previous node string
        previous = self.__prev_player               # Can be equal to None
        previous_str = "AT HEAD (No prior nodes)"

        # Create previous node string if node is present
        if previous is not None:
            previous_str = f"{previous.key} ('{previous.player.name}')"

        # Create default next node string
        next = self.__next_player                   # Can be equal to None
        next_str = "AT TAIL (No more nodes)"
        
        # Create next node string if not is present
        if next is not None:
            next_str = f"{next.key} ('{next.player.name}')"
            
        return (
            f"PlayerNode(Previous Node=[{previous_str}], "
            f"Current Node=[{this_player_str}], "
            f"Next Node=[{next_str}] "
            f")"
        )