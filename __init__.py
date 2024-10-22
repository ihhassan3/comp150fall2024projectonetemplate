# Week 1. Character Classes & Basic Interaction
# Character class that will represent player characters and important NPCs.
class Character:
   def __init__(self, name, health):
       self.name = name
       self.health = health
       self.inventory = []


   def take_damage(self, amount):
       self.health -= amount
       print(f"{self.name} took {amount} damage. Health is now {self.health}.")


   def use_item(self, item_name):
       for item in self.inventory:
           if item.name == item_name:
               item.apply_effect(self)
               self.inventory.remove(item)
               print(f"{self.name} used {item_name}.")
               break
       else:
           print(f"{item_name} not found in inventory.")


   def interact_with_npc(self, npc):
       print(f"{self.name} interacts with {npc.name}.")
       npc.give_quest()


# NPC class with dialogue, quests, and ally status.
class NPC(Character):
   def __init__(self, name, dialogue, quest_giver=False, is_ally=False):
       super().__init__(name, health=0)  # NPCs might not need health unless they join as allies.
       self.dialogue = dialogue
       self.quest_giver = quest_giver
       self.is_ally = is_ally


   def give_quest(self):
       if self.quest_giver:
           print(f"{self.name} says: '{self.dialogue}'")
           print(f"{self.name} has given a quest.")
       else:
           print(f"{self.name} says: '{self.dialogue}'")


   def join_player(self):
       if not self.is_ally:
           self.is_ally = True
           print(f"{self.name} has joined the player's team!")
       else:
           print(f"{self.name} is already your ally.")


# Inventory management with item usage.
class Inventory:
   def __init__(self):
       self.items = []


   def add_item(self, item):
       self.items.append(item)
       print(f"Added {item.name} to inventory.")


   def use_item(self, item_name, character):
       for item in self.items:
           if item.name == item_name:
               item.apply_effect(character)
               self.items.remove(item)
               print(f"Used {item_name} on {character.name}.")
               break
       else:
           print(f"Item {item_name} not found in inventory.")


# Items that can be collected and used.
class Item:
   def __init__(self, name, effect, quantity=1):
       self.name = name
       self.effect = effect
       self.quantity = quantity


   def apply_effect(self, character):
       if self.effect == "heal":
           character.health += 20
           print(f"{character.name} healed for 20 points. Health is now {character.health}.")
       self.quantity -= 1
       if self.quantity <= 0:
           print(f"{self.name} has been used up.")




# Manages the story progression based on player decisions.
class StoryManager:
   def __init__(self):
       self.story_path = []
       self.introduce_story()


   def introduce_story(self):
       print("In the Shadow Mushroom Kingdom, a dark force looms. The Shadow Overlord has kidnapped Princess Peach!")
       print("Mario, your quest begins now. You must rescue her and defeat the Shadow Overlord.")
       self.update_story_path("Introduction: Princess Peach is kidnapped")


   def update_story_path(self, path):
       self.story_path.append(path)
       print(f"Story path updated: {path}")


   def check_moral_choice(self, choice):
       if choice == "help_npc":
           print("You chose to help the NPC. This will affect future story arcs.")
       elif choice == "ignore_npc":
           print("You chose to ignore the NPC. This will impact your alliances.")
           # Add a consequence for ignoring NPC
           self.update_story_path("Ignored Toad's request for help. Toad's trust in you decreases.")


   def unlock_story_arc(self, arc):
       print(f"New story arc unlocked: {arc}")


# Manages NPC conversations and player choices.
class DialogueManager:
   def display_dialogue(self, npc):
       print(f"{npc.name} says: '{npc.dialogue}'")


   def choose_response(self, responses):
       print("Choose a response:")
       for idx, response in enumerate(responses, start=1):
           print(f"{idx}. {response}")
       # Simulate the player's choice
       choice = 1  # Simulating that the player chose the first option
       print(f"Player chose: {responses[choice - 1]}")
       return choice  # Return the choice for further processing


# Create a StoryManager instance to introduce the story first.
story_manager = StoryManager()


# Create a few example NPCs with dialogues and quests.
npc1 = NPC(name="Toad", dialogue="The Shadow Overlord threatens our kingdom!", quest_giver=True)
npc2 = NPC(name="Yoshi", dialogue="I can help you in battle if you need me.", quest_giver=False, is_ally=True)


# Sample player character
player = Character(name="Mario", health=100)
player.interact_with_npc(npc1)
# Define the ShadowCreature class
class ShadowCreature(Character):
    def __init__(self, name, health):
        super().__init__(name, health)
        
    def eclipse_burst(self, target):
        damage = 20  # Damage dealt by the Eclipse Burst
        print(f"{self.name} uses Eclipse Burst!")
        target.take_damage(damage)

# Create the shadow creature
shadow_creature = ShadowCreature(name="Shadow Creature", health=50)

# Mario interacts with Toad and receives the quest
player.interact_with_npc(npc1)

# Shadow creature attacks Mario
shadow_creature.eclipse_burst(player)

# Mario uses a health potion to recover health
player.use_item("Health Potion")  # Assuming the health potion heals 10 points

# Check Mario's health after using the potion
print(f"{player.name}'s current health: {player.health}")

# Mario uses Fire Flower to attack the shadow creature twice
class FireFlower(Item):
    def __init__(self, name, effect, quantity=2, damage=15):
        super().__init__(name, effect, quantity)
        self.damage = damage

    def apply_effect(self, target):
        if self.quantity > 0:
            target.take_damage(self.damage)
            self.quantity -= 1
            print(f"{target.name} has {target.health} health remaining.")
        else:
            print(f"{self.name} has been used up.")

# Create Fire Flower instances for Mario
fire_flower = FireFlower(name="Fire Flower", effect="fire_damage", quantity=2)

# Mario attacks the shadow creature twice
for _ in range(2):
    fire_flower.apply_effect(shadow_creature)

# Check if the shadow creature is defeated
if shadow_creature.health <= 0:
    print(f"{shadow_creature.name} has been defeated!")
else:
    print(f"{shadow_creature.name} is still standing with {shadow_creature.health} health.")

# Continue the story
print("With the Shadow Creature defeated, Mario catches his breath.")
print("Toad exclaims, 'You did it, Mario! We are one step closer to defeating the Shadow Overlord!'")
print("As you continue your journey, new challenges await in the depths of the Shadow Mushroom Kingdom.")


# Example of adding items and using them.
potion = Item(name="Health Potion", effect="heal", quantity=2)
player.inventory.append(potion)
player.use_item("Health Potion")


# Story progression example.
story_manager.update_story_path("Met Toad and accepted quest")
story_manager.check_moral_choice("help_npc")  # Simulating helping Toad
story_manager.unlock_story_arc("Battle with Shadow Creatures")


# Dialogue interaction example.
dialogue_manager = DialogueManager()
dialogue_manager.display_dialogue(npc2)
response_choice = dialogue_manager.choose_response(["Let's team up!", "I don't need your help right now."])


# Outcome based on player's choice (option 1)
if response_choice == 1:
   print("Yoshi's eyes light up with excitement!")
   print("Yoshi says: 'Thank you, Mario! Together, we can defeat the Shadow Overlord! Let’s gather more allies and prepare for battle.'")
   print("With Yoshi by your side, you feel a surge of confidence.")
   print("As you journey through the Shadow Mushroom Kingdom, Toad provides valuable information about the Shadow Overlord's minions.")
   print("You collect items, defeat shadow creatures, and grow stronger together.")
   print("Will you be able to rescue Princess Peach and restore peace to the kingdom?")

# Unit Test
import logging
import unittest


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
       self.assertIn("New story arc unlocked: Battle with Shadow Creatures", log.output[0])


if __name__ == '__main__':
   unittest.main()




