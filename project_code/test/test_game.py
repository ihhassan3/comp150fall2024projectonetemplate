import sys
import os

# Add the root directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from project_code.src.main import Statistic, Character, Event
import unittest

class TestStatistic(unittest.TestCase):

    def setUp(self):
        self.strength = Statistic("Strength", value=10)

    def test_statistic_initialization(self):
        self.assertEqual(self.strength.name, "Strength")
        self.assertEqual(self.strength.value, 10)

    def test_statistic_modify(self):
        self.strength.modify(5)
        self.assertEqual(self.strength.value, 15)
        self.strength.modify(-10)
        self.assertEqual(self.strength.value, 5)

    def test_statistic_min_max_bounds(self):
        self.strength.modify(1000)
        self.assertEqual(self.strength.value, self.strength.max_value)
        self.strength.modify(-1000)
        self.assertEqual(self.strength.value, self.strength.min_value)

class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.character = Character(name="Hero")

    def test_character_initialization(self):
        self.assertEqual(self.character.name, "Hero")
        self.assertEqual(self.character.strength.name, "Strength")
        self.assertEqual(self.character.intelligence.name, "Intelligence")

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.event_data = {
            "primary_attribute": "Intelligence",
            "secondary_attribute": "Strength",
            "prompt_text": "A mysterious door blocks your path, with a riddle inscribed. What will you do?",
            "pass": {"message": "You solved the riddle and pushed the door open. You may proceed."},
            "fail": {"message": "You failed to solve the riddle and push the door open. You must find another way."},
            "partial_pass": {"message": "You managed to solve the riddle or push the door, but not both."}
        }
        self.event = Event(self.event_data)

    def test_event_initialization(self):
        self.assertEqual(self.event.primary_attribute, "Intelligence")
        self.assertEqual(self.event.secondary_attribute, "Strength")
        self.assertEqual(self.event.prompt_text, self.event_data["prompt_text"])
        self.assertEqual(self.event.pass_message, self.event_data["pass"]["message"])
        self.assertEqual(self.event.fail_message, self.event_data["fail"]["message"])
        self.assertEqual(self.event.partial_pass_message, self.event_data["partial_pass"]["message"])

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch

# Sample classes based on Week 2 code

class TestCombatSystem(unittest.TestCase):

    def setUp(self):
        self.player = Character("Mario", health=100)
        self.enemy = Character("Shadow Overlord", health=150)
        self.combat = Combat(self.player, self.enemy)

    @patch('random.randint', return_value=10)
    def test_calculate_damage(self, mock_randint):
        """ Test that calculate_damage returns expected mocked value"""
        damage = self.combat.calculate_damage(self.player)
        self.assertEqual(damage, 10, "Damage calculation should return 10 based on mock")

    def test_engage_combat_player_win(self):
        """ Test that engage_combat ends with player victory when enemy health goes to 0"""
        self.enemy.health = 10 # Set low enemy health to simulate win
        result = self.combat.engage_combat()
        self.assertTrue(result, "Player should win if enemy reaches zero")

    def test_engage_combat_player_loss(self):
        """ Test that engage_combat ends with player defeat if player health reaches 0"""
        self.player.health = 5
        self.enemy.health = 10
        result = self.combat.engage_combat()
        self.assertFalse(result, "Player shoud lose if their health reaches zero")

class TestInventory(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.item1 = Item(name="Health Potion", effect="heal")
        self.item2 = Item(name="Power-up", effect="boost")

    def test_add_item(self):
        """ Test that items are added to inventory correctly """
        self.inventory.add_item(self.item1)
        self.inventory.add_item(self.item2)
        self.assertEqual(len(self.inventory.items), 2, "Inventory should contain 2 items")
        self.assertIn(self.item1, self.inventory.items, "Inventory shoudl contain item1")
        self.assertIn(self.item2, self.inventory.items, "Inventory should contain item2")

    def test_use_item(self):
        """ Test  taht items are used and removed from inventory in FIFO order """
        self.inventory.add_item(self.item1)
        self.inventory.add_item(self.item2)
        used_item = self.inventory.use_item()
        self.assertEqual(used_item, self.item1, "First used item should be item1")
        self.assertEqual(len(self.inventory.items), 1, "Inventory should have 1 item left after using one")

class TestDialogueManager(unittest.TestCase):

    def setUp(self):
        self.dialogue_manager = DialogueManager()
        self.npc = NPC(name="Wise Toad", dialogue="Thanks for helping us!")
    
    @patch('builtins.print')
    def test_display_dialogue_help_center(self, mock_print):
        """ Test that NPC gives correct response based on player choice """
        self.dialogue_manager.display_dialogue(self.npc, "help")
        mock_print.assert_called_with("Wise Toad: Thank you for your help, brace hero!")

    @patch('builtins.print')
    def test_display_ignore_choice(self, mock_print):
        """ Test NPC's response when player chooses to ignore """
        self.dialogue_manager.display_dialogue(self.npc, "ignore")
        mock_print.assert_called_with("Wise Toad: I hope you would help... but I see you have other priorities.")

class TestItem(unittest.TestCase):

    def setUp(self):
        self.character = Character("Luigi", 80)
        self.item = Item(name="Healing Mushroom", effect="heal")

    def test_apply_effect(self):
        """ Test that item effect modifies character stats correctly """
        initial_health = self.character.health
        self.item.apply_effect(self.character)
        self.assertEqual(self.character.health, initial_health + 20, "Health should increases by 20")

# Main test runner
if __name__ == "__main__":
    unittest.main()