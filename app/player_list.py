# player_list.py
import logging

from app.player_node import PlayerNode

class PlayerList:
    """
    A Double-Linked List implementation for a list of Player instaces.
    """

    def __init__(self):
        self._head = None
        self._tail = None

        logging.basicConfig(level=logging.INFO)


    @property
    def head(self):
        """
        Get the PlayerNode at the head of the list.

        Returns:
            PlayerNode: The node at the head of the list.
        """

        return self._head
    
    @property
    def tail(self):
        """
        Get the PlayerNode at the tail of the list.

        Returns:
            PlayerNode: The node at the tail of the list.
        """

        return self._tail

    def is_empty(self):
        """
        Checks if the list is empty.

        Returns:
            True if the list is empty, otherwise False.
        """

        return self._head is None
    
    def push(self, new_node: PlayerNode):
        """
        Insert a new node at the head of the list.
        
        Args:
            new_node(PlayerNode): 
                The PlayerNode instance to insert at head of list.

        Raises:
            ValueError when node is None

        """

        if new_node is None:
            raise ValueError("PlayerNode argument was empty or invalid!")

        if not self._check_for_dupes(new_node):
            raise ValueError(f"Player or PlayerNode with ID: {new_node.key} already exists in the list!")

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._insert_at_head(new_node)

        logging.debug(f"Inserted at HEAD of list: {new_node}")

    def insert(self, index: int, new_node: PlayerNode):
        """
        Insert a new node to the list with the given index.

        Args:
            index(int):
                The index for the new node. 
                - A value of 0 will insert to the head of the list.
                - A value of -1 will insert to the tail of the list.
                - A positive value greater than 0 will try to insert to
                    the list from the head of the list, provided the
                    index is valid.
                - A negative value less than -1 will try to insert from
                    the tail of the list, provided the index is valid.

            new_node(PlayerNode): 
                The PlayerNode instance to insert at head of list.
        """

        if new_node is None:
            raise ValueError("PlayerNode argument was empty or invalid!")

        if not self._check_for_dupes(new_node):
            raise ValueError(f"Player or PlayerNode with ID: {new_node.key} already exists in the list!")
        
        if self.is_empty():                             
            self._head = new_node
            self._tail = new_node
            return                                      
        
        if index == 0:
            self._insert_at_head(new_node)
            return
        elif index == -1:
            self._insert_at_tail(new_node)
            return

        # Check the index value is valid for other additions
        raise RuntimeError(f"Adding internal nodes not yet supported")

    def append(self, new_node: PlayerNode):
        """
        Add a new node at the tail of the list.
        
        Args:
            new_node(PlayerNode): 
                The PlayerNode instance to insert at tail of list.

        Raises:
            ValueError if new node is None
        """

        if new_node is None:
            raise ValueError("PlayerNode argument was empty or invalid!")

        if not self._check_for_dupes(new_node):
            raise ValueError(f"Player or PlayerNode with ID: {new_node.key} already exists in the list!")

        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        
        else:
            self._insert_at_tail(new_node)

        logging.debug(f"Inserted at TAIL of list: {new_node}")

    def shift(self) -> PlayerNode:
        """
        Remove the Head node from the list.

        Returns:
            PlayerNode: The node that was removed.
        """

        if self.is_empty():
            raise IndexError("The list is empty!")

        removing = self._head
        new_head = self._head.next              # May be None
        self._head = new_head                   # Shift the head pointer

        if new_head:
            del new_head.previous               # Deleter clears reference
        else:
            self._tail = None

        logging.debug(f"Removed from HEAD of list: {removing}")

        del removing.next
        return removing

    def pop(self) -> PlayerNode:
        """
        Remove the Tail node from the list.

        Returns:
            PlayerNode: The node that was removed.
        """
        
        if self.is_empty():
            raise IndexError("The list is empty!")

        removing = self._tail
        new_tail = self._tail.previous         # May be None
        self._tail = new_tail                  # Shift the tail pointer

        if new_tail:
            del new_tail.next                  # Deleter clears refernce
        else:
            self._head = None
        
        logging.debug(f"Removed from TAIL of list: {removing}")
        
        del removing.previous
        return removing

    def remove(self, key: str) -> PlayerNode:
        """
        Remove a node by key.

        Returns:
            PlayerNode: The node that was removed

            *OR None* if the key was not found.
        """

        current = self._head

        while current is not None:
            if current.key is not key:
                current = current.next
                continue

            # Handle removal...
            if current.previous:
                current.previous.next = current.next

            elif current == self._head:
                self._head = current.next

            if current.next:
                current.next.previous = current.previous

            elif current == self._tail:
                self._tail = current.previous

            del current.previous
            del current.next
            logging.debug(f"Removed: {current}")
            break

        return current

    def display(self, reverse: bool = False):
        """
        Prints the list from head to tail, or tail to head.

        Args:
            reversed (bool):
                Defaults to descending order (head to tail),
                set reversed = True to print ascending order (tail to head).
        """
        
        if self.is_empty():
            print("The list is empty!")
            return

        nodes_list = list(map(self._format_node, reversed(self) if reverse else self))

        # Join strings
        start_label = "<TAIL>" if reverse else "<HEAD>"
        end_label = "<HEAD>" if reverse else "<TAIL>"
        nodes_string = '\n'.join(nodes_list)
        
        print(f"<== Player list"
              f"{' (Reversed) ' if reverse else ' '}"
              f"==>\n"
              f"{start_label} \n{nodes_string} \n{end_label}")

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current
            current = current.next 

    def __reversed__(self):
        current = self._tail

        while current is not None:
            yield current
            current = current.previous         

    def _format_node(self, node):
        """
        Returns a formatted string representation of a node.
        *Intended for internal use, but may be used externally*

        Args:
            node (PlayerNode): The node to format. Not checked.

        Returns:
            str: A formatted string representation of the node.
        """

        return f"> {node.player.name:<20} [{node.key}]"

    def _check_for_dupes(self, new_node: PlayerNode) -> bool:
        """
        Checks for duplicate PlayerNodes or Players through the 
         existing items in the list
        """

        # Filter the list with node.equals func to find collisions
        # return not any(node.equals(new_node) for node in self)
        return not any(filter(new_node.equals, self))

    def _insert_at_head(self, new_node: PlayerNode):
        """
        Inserting when the list is not empty...
        
        - Force node state
        - Create new links
        - Update list
        """

        current_head = self._head

        if new_node.previous:
            raise ValueError("New node should not be connected to other nodes")

        new_node.next = current_head        # Connect the new head
        current_head.previous = new_node

        self._head = new_node               # Update the head ref
    
    def _insert_at_tail(self, new_node: PlayerNode):
        """
        Inserting when the list is not empty...
        
        - Force node state
        - Create new links
        - Update list reference
        """

        current_tail = self._tail

        if new_node.next:
            raise ValueError("New node should not be connect to other nodes")

        new_node.previous = current_tail    # Connect the new tail
        current_tail.next = new_node

        self._tail = new_node               # Update the tail ref