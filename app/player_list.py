# player_list.py

from app.player_node import PlayerNode

class PlayerList:
    """
    A Double-Linked List implementation for a list of Player instaces.
    """

    # Static properties for messages
    EMPTY_OR_INVALID_NODE_MSG = "PlayerNode argument was empty or invalid!"
    DUPLICATE_NODE_MSG = "Player or PlayerNode with ID: {uid} already exists in the list!"
    SUCCESS_INSERT_MSG = "Inserted successfully at head of list: {node}"

    def __init__(self):
        self.__head = None

    @property
    def head(self):
        """
        Get the PlayerNode at the head of the list

        Returns:
            PlayerNode: The node at the head of the list
        """

        return self.__head

    def is_empty(self):
        """
        Checks if the list is empty.

        Returns:
            True if the list is empty, otherwise False.
        """

        return self.__head is None              # No head to the list currently
                                                # means no list, (but will 
                                                # change with addition of tail)
    
    def insert_at_head(self, new_node: PlayerNode):
        """
        Insert a new node at the head of the list.
        
        Args:
            new_node(PlayerNode): 
                The PlayerNode instance to insert at head of list.
        """

        # Enforce not None and correct object type
        # 
        # - Prevents an invalid state to the list

        if new_node is None or not isinstance(new_node, PlayerNode):
            raise ValueError(self.EMPTY_OR_INVALID_NODE_MSG)

        # Check if the node or player is already in the list
        # 
        # - Prevents an invalid state to the list

        if not self.__ok_to_add(new_node):
            raise ValueError(f"{self.DUPLICATE_NODE_MSG.format(uid=new_node.key)}")

        current_head = self.__head              # For clarity

        # Inserting when the list is empty...
        #
        # - Force node state
        # - Update list

        if self.is_empty():
            del new_node.previous               # Ensure the head node state 
            del new_node.next                   # is correct (for empty list)

            self.__head = new_node              # Set the new node as the head
                                                # node.
        
        # Inserting when the list is not empty...
        #
        # - Force node state
        # - Create new links
        # - Update list

        else:
            del new_node.previous               # Ensure the head note state
                                                # is correct

            new_node.next = current_head        # Create link between new head
            current_head.previous = new_node    # node and old

            self.__head = new_node              # Set the new node as the head 
                                                # node.

        print(f"{self.SUCCESS_INSERT_MSG.format(node=new_node)}")
        return

    def __ok_to_add(self, new_node: PlayerNode) -> bool:
        """
        Checks for duplicate PlayerNodes or Players through the 
         existing items in the list
        """

        curr_checking = self.__head             # Start at the head
        while curr_checking is not None:
            if (curr_checking == new_node
                    or curr_checking.player == new_node.player
                    or curr_checking.key == new_node.key):
                return False                    # Existing match found
                
            curr_checking = curr_checking.next  # Move to next
        
        return True                             # No existing matches
        
