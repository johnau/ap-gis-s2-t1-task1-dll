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

class TestPlayerNodeBehavior(unittest.TestCase):

    def test_player_node_with_bad_args(self):
        print("\nStart Test: New PlayerNode with bad arguments...")

        with self.assertRaises(ValueError):
            playerNode = PlayerNode(None)
        
        print("\nNew PlayerNode with bad arguments test failed successfully!")

    def test_player_node_with_player(self):
        print("\nStart Test: New PlayerNode with valid arguments...")

        name = "John Wick"
        guid = str(uuid.uuid4())  # uuid4 is parameterless
        player = Player(guid, name)
        print(player)

        playerNode = PlayerNode(player)
        
        self.assertIsNotNone(playerNode)
        self.assertIsInstance(playerNode, PlayerNode)
        self.assertEqual(guid, playerNode.key)
        self.assertEqual(player, playerNode.player)

        print(playerNode)
        print(f"\nNew PlayerNode with valid arguments test passed successfully!")

if __name__ == "__main__":
    unittest.main()