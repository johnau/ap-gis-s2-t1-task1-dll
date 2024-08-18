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

class TestPlayerBehavior(unittest.TestCase):

    def test_constructor_with_uid_property(self):
        print("\nStart Test: New Player arguments (uid)...")

        guid = str(uuid.uuid4())        # uuid4 is parameterless
        player = Player(guid, "not tested")

        self.assertEqual(player.uid, guid)
        
        print(f"\nPlayer uid was as expected... {player.uid}")
        print(player)

    def test_constructor_with_name_property(self):
        print("\nStart Test: New Player arguments (name)...")

        name = "John Wick"
        player = Player("not tested", name)
        
        self.assertEqual(player.name, name)
        
        print(f"\nPlayer name was as expected... {player.name}")
        print(player)

if __name__ == "__main__":
    unittest.main()