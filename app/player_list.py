# player_list.py
import logging

from app.player_node import PlayerNode

class PlayerList:
    """
    A Double-Linked List implementation for a list of Player instaces.
    """

    # Static properties for messages
    EMPTY_OR_INVALID_NODE_MSG = "PlayerNode argument was empty or invalid!"
    DUPLICATE_NODE_MSG = "Player or PlayerNode with ID: {uid} already exists in the list!"
    SUCCESS_INSERT_MSG = "Inserted at {position} of list: {node}"
    SUCCESS_REMOVE_MSG = "Removed from {position} of list: {node}"

    def __init__(self):
        self.__head = None
        self.__tail = None

        logging.basicConfig(level=logging.INFO)

    @property
    def head(self):
        """
        Get the PlayerNode at the head of the list.

        Returns:
            PlayerNode: The node at the head of the list.
        """

        return self.__head                      # return the head property
    
    @property
    def tail(self):
        """
        Get the PlayerNode at the tail of the list.

        Returns:
            PlayerNode: The node at the tail of the list.
        """

        return self.__tail                      # return the tail property

    def is_empty(self):
        """
        Checks if the list is empty.

        Returns:
            True if the list is empty, otherwise False.
        """

        return self.__head is None                  # No head to the list, 
                                                    # no list
    
    def push(self, new_node: PlayerNode):
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

        # Inserting when the list is empty...
        if self.is_empty():
            self.__insert_first_entry(new_node)     # Insert first node
        
        # Inserting when the list is not empty...
        else:
            self.__insert_at_head(new_node)         # Insert at head

        logging.debug(f"{self.SUCCESS_INSERT_MSG.format(position='HEAD', node=new_node)}")  # Debug
        return

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
        
        # Inserting when the list is empty...
        if self.is_empty():                             
            self.__insert_first_entry(new_node)         # Always insert first
            return                                      
        
        # Insert at head or tail...
        if index == 0:
            self.__insert_at_head(new_node)             # Insert at head
            return
        elif index == -1:
            self.__insert_at_tail(new_node)             # Insert at tail
            return

        # Check the index value is valid for other additions
        raise RuntimeError(f"Adding internal nodes not yet supported")

        return

    def append(self, new_node: PlayerNode):
        """
        Add a new node at the tail of the list.
        
        Args:
            new_node(PlayerNode): 
                The PlayerNode instance to insert at tail of list.
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

        # Inserting when the list is empty...
        if self.is_empty():
            self.__insert_first_entry(new_node)     # Insert first node
        
        # Inserting when the list is not empty...
        else:
            self.__insert_at_tail(new_node)         # Insert at tail

        logging.debug(f"{self.SUCCESS_INSERT_MSG.format(position='TAIL', node=new_node)}")

        return

    def shift(self) -> PlayerNode:
        """
        Remove the Head node from the list.

        Returns:
            PlayerNode: The node that was removed.
        """

        if self.is_empty():
            raise IndexError("The list is empty!")

        removing = self.__head                  # Local reference
        new_head = self.__head.next             # May be None
        self.__head = new_head                  # Shift the head pointer

        if new_head:                            # If there is another node
            del new_head.previous               # Update new head node state
        else:                                   # otherwise...
            self.__tail = None                  # clear the tail too

        logging.debug(f"{self.SUCCESS_REMOVE_MSG.format(position='HEAD', node=removing)}")

        del removing.next                       # Detach the old head node
        return removing                         # Return detached node

    def pop(self) -> PlayerNode:
        """
        Remove the Tail node from the list.

        Returns:
            PlayerNode: The node that was removed.
        """
        
        if self.is_empty():
            raise IndexError("The list is empty!")

        removing = self.__tail                  # Local reference
        new_tail = self.__tail.previous         # May be None
        self.__tail = new_tail                  # Shift the tail pointer

        if new_tail:                            # If there is another node
            del new_tail.next                   # Update new tail node state
        else:                                   # otherwise...
            self.__head = None                  # clear the head too
        
        logging.debug(f"{self.SUCCESS_REMOVE_MSG.format(position='TAIL', node=removing)}")
        
        del removing.previous                   # Detach the old tail node
        return removing                         # Return detached node

    def remove(self, key: str) -> PlayerNode:
        """
        Remove a node by key.

        Returns:
            PlayerNode: The node that was removed

            *OR None* if the key was not found.
        """

        current = self.__head                   # Start at head of list

        while current is not None:              # Iterate to the end of the list
            if current.key == key:              # Check for a match
                # Handle removal...
                if current.previous:            # Is there a previous node?
                    current.previous.next = current.next      # Link it to next

                elif current == self.__head:    # if not, should be at head,
                    self.__head = current.next  # Set next as head

                if current.next:                # Is there a next node?
                    current.next.previous = current.previous  # Link it to previous

                elif current == self.__tail:    # if not, should be at tail,
                    self.__tail = current.previous  # Set previous as tail               

                del current.previous            # Disconnect current
                del current.next
                print(f"Removed: {current}")
                break                           # End the loop, current was removed

            # if current key did not match provided key...
            current = current.next              # ...move to the next node

        return current

    def display(self, reversed: bool = False):
        """
        Prints the list from head to tail, or tail to head.

        Args:
            reversed (bool):
                Defaults to descending order (head to tail),
                set reversed = True to print ascending order (tail to head).
        """
        
        if self.is_empty():
            print("The list is empty!")         # Early exit if empty
            return

        # Map format node func against iterator
        nodes2 = list(map(self._format_node, self._iterate(reversed)))

        # Join strings
        start_label = "<TAIL>" if reversed else "<HEAD>"
        end_label = "<HEAD>" if reversed else "<TAIL>"
        nodes_string = '\n'.join(nodes2)         # Nodes with line separator
        
        print(f"<== Player list"                # Print the display string
              f"{' (Reversed) ' if reversed else ' '}"
              f"==>\n"
              f"{start_label} \n{nodes_string} \n{end_label}")

        return

    def _iterate(self, reversed: bool = False):
        """
        Generator function to iterate through the linked list 
          from head to tail, or tail to head, based on the 'reversed' 
          flag.
        *Intended for internal use, but may be used externally*
          
        Args:
            reversed (bool):
                Iteration direction: 
                - False = HEAD to TAIL,    
                - True = TAIL to HEAD.
          
        Yields:
            PlayerNode: The current node in the list.
        """
        
        current = self.__tail if reversed else self.__head  # Set current

        while current is not None:                          # Iterate + yield
            yield current
            current = current.previous if reversed else current.next  # Next

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

    def __ok_to_add(self, new_node: PlayerNode) -> bool:
        """
        Checks for duplicate PlayerNodes or Players through the 
         existing items in the list
        """

        # Filter the list with node.equals func to find collisions
        # return not any(node.equals(new_node) for node in self._iterate())
        return not any(filter(new_node.equals, self._iterate()))
        
    def __insert_first_entry(self, new_node: PlayerNode):
        """
        Inserts the first entry to the list
        """

        # Inserting when the list is empty...
        #
        # - Force node state
        # - Update list
        del new_node.previous               # Ensure the new node state 
        del new_node.next                   # is correct (for empty list)

        self.__head = new_node              # Set the new node as the head
        self.__tail = new_node              # node. Also as tail.

    def __insert_at_head(self, new_node: PlayerNode):
        """
        Inserting when the list is not empty...
        
        - Force node state
        - Create new links
        - Update list
        """

        current_head = self.__head          # For clarity

        del new_node.previous               # Ensure the head note state
                                            # is correct

        new_node.next = current_head        # Create link between new head
        current_head.previous = new_node    # node and old

        self.__head = new_node              # Set the new node as the head 
                                            # node. No change to tail.
        return
    
    def __insert_at_tail(self, new_node: PlayerNode):
        """
        Inserting when the list is not empty...
        
        - Force node state
        - Create new links
        - Update list reference
        """

        current_tail = self.__tail          # For clarity

        del new_node.next                   # Ensure the tail note state
                                            # is correct

        new_node.previous = current_tail    # Create link between new tail
        current_tail.next = new_node        # node and old

        self.__tail = new_node              # Set the new node as the tail 
                                            # node. No change to head.
        return