import sys
import os
import logging
import unittest

# Add the root directory of the project to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from project_code.src.main import Statistic, Character, Event

# Set up logging for the test cases
logging.basicConfig(level=logging.INFO)

# StoryManager class definition
class StoryManager:
    def __init__(self):
        self.story_path = []

    def unlock_story_arc(self, arc_name):
        """Unlocks a new story arc and logs the action."""
        self.story_path.append(arc_name)
        logging.info(f"New story arc unlocked: {arc_name}")  # Ensure this logs at INFO level

# Test class for StoryManager
class TestStoryManager(unittest.TestCase):

    def setUp(self):
        """Set up the StoryManager for testing."""
        self.story_manager = StoryManager()

    def test_unlock_story_arc(self):
        """Test if a new story arc is unlocked correctly."""
        with self.assertLogs(level='INFO') as log:
            self.story_manager.unlock_story_arc("Battle with Shadow Creatures")
        
        # Check that logs were generated and contain the expected message
        self.assertTrue(log.output)  # Check that some logs were indeed captured
        self.assertIn("INFO:root:New story arc unlocked: Battle with Shadow Creatures", log.output[0])

if __name__ == '__main__':
    unittest.main()

