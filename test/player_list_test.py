# player_list_test.py

import unittest
import uuid

import sys
import os

# Add the project directory to sys.path so the file can be run without 
# running module.
# Added for convenience to run from VSCode rather than running module
# or pytest from terminal.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.player import Player
from app.player_node import PlayerNode
from app.player_list import PlayerList

class TestPlayerListBehavior(unittest.TestCase):
    """
    Test the behavior of the Doubly Linked List implementation
    """

    WRONG_NODE_INSTANCE_MSG = "The {name} node did not match expected instance"

    def setUp(self):
        """
        unittest function for setup before each test
        """

        self.player_list = PlayerList()

        # Create some test objects
        uid1 = uuid.uuid4()
        uid2 = uuid.uuid4()
        uid3 = uuid.uuid4()
        player1 = Player(uid1, "John Wick")
        player2 = Player(uid2, "Iosef Tarasov")
        player3 = Player(uid3, "Viggo Tarasov")
        node1 = PlayerNode(player1)
        node2 = PlayerNode(player2)
        node2_sim = PlayerNode(player2)
        node3 = PlayerNode(player3)

        # Stash them in the class
        self.node1 = node1
        self.node2 = node2
        self.node2x = node2_sim
        self.node3 = node3

    def test_insert_at_head_empty_list(self):
        """
        Testing Doubly-Linked list behavior for insert to empty list.
        (Insert to head)
        """

        print("\nStart Test: Insert to list head, empty list...")

        self.assertTrue(self.player_list.is_empty())

        # Insert node (will succeed)
        self.player_list.push(self.node1)     # Insert only Player/node
        
        self.assertFalse(self.player_list.is_empty())
        self.assertEqual(self.player_list.head, self.node1)
        self.assertEqual(self.player_list.tail, self.node1)

        print(f"List head is as expected: {self.player_list.head}")
        print(f"List tail is as expected: {self.player_list.tail}")

        print("\nTest success!")

    def test_insert_at_head_non_empty_list(self):
        """
        Testing Doubly-Linked List behavior for insert to non-empty 
        list. (Insert to head)
        """

        print("\nStart Test: Insert to list head, non empty list...")

        self.assertTrue(self.player_list.is_empty())

        # Insert first two players (will succeed)
        self.player_list.push(self.node2)      # Insert Player 2
        self.player_list.push(self.node1)      # Insert Player 1 infront

        self.assertEqual(self.player_list.head, self.node1, 
                         self.WRONG_NODE_INSTANCE_MSG.format(name='HEAD'))
        
        self.assertEqual(self.player_list.head.next, self.node2,
                         self.WRONG_NODE_INSTANCE_MSG.format(name='HEAD.NEXT'))
        
        self.assertEqual(self.node2.previous, self.node1,
                         self.WRONG_NODE_INSTANCE_MSG.format(name='2ND'))
        
        self.assertEqual(self.player_list.tail, self.node2,
                         self.WRONG_NODE_INSTANCE_MSG.format(name='TAIL'))

        print(f"List head is as expected: {self.player_list.head}")
        print(f"List tail is as expected: {self.player_list.tail}")

        print("\nTest success!")

    def test_insert_at_head_with_duplicate_node(self):
        """
        Testing Doubly-Linked List behavior for invalid insert to list
        (duplication of node or player) (Insert to Head)
        """

        print("\nStart Test: Insert to list head with duplicates...")

        self.assertTrue(self.player_list.is_empty())

        # Insert first two players (will succeed)
        self.player_list.push(self.node2)      # Insert Player 2
        self.player_list.push(self.node1)      # Insert Player 1 infront

        # Insert a node again (will fail)
        with self.assertRaises(ValueError):
            self.player_list.push(self.node2)  # Insert duplicate node

        print(f"Error raised trying to add same node twice...")

        # Insert a player again (will fail)
        with self.assertRaises(ValueError):
            self.player_list.push(self.node2x) # Insert duplicate player

        print(f"Error raised trying to add same player twice...")

        # Insert a new player (will succeed)
        self.player_list.push(self.node3)      # Insert Player 3

        self.assertEqual(self.player_list.head, self.node3)
        self.assertEqual(self.player_list.tail, self.node2)

        print(f"List head is as expected: {self.player_list.head}")
        print(f"List tail is as expected: {self.player_list.tail}")

        print("Test success!")

    def test_insert_at_tail_empty_list(self):
        """
        Testing Doubly-Linked list behavior for insert to empty list.
        (Insert to tail)
        """

        print("\nStart Test: Insert to list tail, empty list...")

        self.assertTrue(self.player_list.is_empty())

        # Insert node (will succeed)
        self.player_list.append(self.node1)     # Insert only Player/node
        
        self.assertFalse(self.player_list.is_empty())
        self.assertEqual(self.player_list.head, self.node1)
        self.assertEqual(self.player_list.tail, self.node1)

        print(f"List head is as expected: {self.player_list.head}")
        print(f"List tail is as expected: {self.player_list.tail}")

        print("\nTest success!")

    def test_insert_at_tail_non_empty_list(self):
        """
        Testing Doubly-Linked List behavior for insert to non-empty 
        list. (Insert to tail)
        """

        print("\nStart Test: Insert to list tail, non empty list...")

        self.assertTrue(self.player_list.is_empty())

        # Insert first two players (will succeed)
        self.player_list.append(self.node1)      # Insert Player 1
        self.player_list.append(self.node2)      # Insert Player 2 after

        self.assertEqual(self.player_list.head, self.node1)
        self.assertEqual(self.player_list.head.next, self.node2)
        self.assertEqual(self.player_list.tail, self.node2)
        self.assertEqual(self.player_list.tail.previous, self.node1)

        print(f"List head is as expected: {self.player_list.head}")
        print(f"List tail is as expected: {self.player_list.tail}")

        print("\nTest success!")

    def test_insert_at_tail_with_duplicate_node(self):
        """
        Testing Doubly-Linked List behavior for invalid insert to list
        (duplication of node or player) (Insert to Tail)
        """

        print("\nStart Test: Insert to list tail with duplicates...")

        self.assertTrue(self.player_list.is_empty())

        # Insert first two players (will succeed)
        self.player_list.append(self.node1)      # Insert Player 1
        self.player_list.append(self.node2)      # Insert Player 2 after

        # Insert a node again (will fail)
        with self.assertRaises(ValueError):
            self.player_list.append(self.node1)  # Insert duplicate node

        print(f"Error raised trying to add same node twice...")

        # Insert a player again (will fail)
        with self.assertRaises(ValueError):
            self.player_list.append(self.node2x) # Insert duplicate player

        print(f"Error raised trying to add same player twice...")

        # Insert a new player (will succeed)
        self.player_list.append(self.node3)      # Insert Player 3

        self.assertEqual(self.player_list.head, self.node1)
        self.assertEqual(self.player_list.tail, self.node3)

        print(f"List head is as expected: {self.player_list.head}")
        print(f"List tail is as expected: {self.player_list.tail}")

        print("Test success!")

    def test_remove_from_head(self):
        """
        Testing Doubly-Linked List behavior; removing from head
        """

        print("\nStart Test: Remove from list head...")

        # add some nodes
        self.player_list.append(self.node1)     # Insert Player 1
        self.player_list.append(self.node2)     # Insert Player 2
        self.player_list.append(self.node3)     # Insert Player 3
        self.player_list.display()

        self.assertEqual(self.player_list.head, self.node1)
        print(f"Current list head: {self.player_list.head}")

        self.player_list.shift()                # Remove from head
        self.player_list.display()

        self.assertEqual(self.player_list.head, self.node2)

        print(f"Success, new list head: {self.player_list.head}")

        self.player_list.shift()
        self.player_list.display()

        self.player_list.shift()
        self.player_list.display()

        self.assertTrue(self.player_list.is_empty())

        with self.assertRaises(IndexError):
            self.player_list.shift()

        print("Test success!")

    def test_remove_from_tail(self):
        """
        Testing Doubly-Linked List behavior; removing from tail
        """

        print("\nStart Test: Remove from list tail...")

        # add some nodes
        self.player_list.append(self.node1)     # Insert Player 1
        self.player_list.append(self.node2)     # Insert Player 2
        self.player_list.append(self.node3)     # Insert Player 3
        self.player_list.display()

        self.assertEqual(self.player_list.tail, self.node3)
        print(f"Current list tail: {self.player_list.tail}")

        self.player_list.pop()                  # Remove from tail
        self.player_list.display()

        self.assertEqual(self.player_list.tail, self.node2)

        print(f"Success, new list tail: {self.player_list.tail}")

        self.player_list.pop()                  # Remove other nodes
        self.player_list.display()

        self.player_list.pop()
        self.player_list.display()
        
        self.assertTrue(self.player_list.is_empty())

        with self.assertRaises(IndexError):
            self.player_list.pop()

        print("Test success!")        

    def test_remove_with_key(self):
        """
        Testing Doubly-Linked List behavior; removing by key
        """

        print("\nStart Test: Remove from list by key...")

        # add some nodes
        self.player_list.append(self.node1)     # Insert Player 1
        self.player_list.append(self.node2)     # Insert Player 2
        self.player_list.append(self.node3)     # Insert Player 3

        self.assertEqual(self.player_list.tail.previous, self.node2)
        print(f"Node before TAIL node: {self.player_list.tail.previous}")

        removed = self.player_list.remove(self.node2.key) # Remove by key (succeed)

        self.assertIsNotNone(removed)
        self.assertEqual(self.player_list.head.next, self.node3)
        self.assertEqual(self.player_list.tail.previous, self.node1)

        print(f"After removal...",
                f"\n\tBefore tail: {self.player_list.tail.previous}",
                f"\n\tAfter head: {self.player_list.head.next}")

        removed = self.player_list.remove(self.node2.key) # Remove by key (fail)
        self.assertIsNone(removed)

        print("Test success!")     

    def test_display_list_descending(self):
        """
        Testing Doubly-Linked List behavior; display list in descending
        or ascending order.
        """

        print("\nStart Test: Display list descending...")

        # add some nodes
        self.player_list.append(self.node1)     # Insert Player 1
        self.player_list.append(self.node2)     # Insert Player 2
        self.player_list.append(self.node3)     # Insert Player 3

        # display the nodes descending (default; head to tail)
        self.player_list.display()

    def test_display_list_ascending(self):
        """
        Testing Doubly-Linked List behavior; display list in descending
        or ascending order.
        """

        print("\nStart Test: Display list descending...")

        # add some nodes
        self.player_list.append(self.node1)     # Insert Player 1
        self.player_list.append(self.node2)     # Insert Player 2
        self.player_list.append(self.node3)     # Insert Player 3

        # display the nodes descending (default; head to tail)
        self.player_list.display(True)

if __name__ == '__main__':
    unittest.main()