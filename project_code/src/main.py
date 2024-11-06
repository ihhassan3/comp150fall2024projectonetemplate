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
import random
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Week 2
#Combat Class with Turn-Based System
class Combat:
    def __init__(self, player, boss):
        self.player = player
        self.boss = boss

    def calculate_damage(self, attacker):
        # Basic damage calculation
        damage = random.randint(10, 30)
        return damage

    def enagage_combat(self):
        logging.info(f"{self.player.name} encounters the {self.boss.name}!")

        while self.player.health > 0 and self.boss.health > 0:
            # Player's turn
            logging.info(f"\n{self.player.name}'s turn!")
            action = input("Choose an action: (1) Attack (2) Use Item\n> ")
            if action == '1':
                damage = self.calculate_damage(self.player)
                logging.info(f"{self.player.name} attacks {self.boss.name} for {damage} damage!")
                self.boss.take_damage(damage)
            elif action == '2':
                item = self.player.inventory.get_item() # Simulated item use
                if item:
                    self.player.use_item(item)
                else:
                    logging.info("No useable item found in inventory.")

            # Check if boss is defeated
            if self.boss.health <= 0:
                logging.info(f"{self.boss.name} has been defaeted! You win!")
                break

            # Boss's turn
            logging.info(f"\n{self.boss.name}'s turn!")
            damage = self.calculate_damage(self.boss)
            logging.info(f"{self.boss.name} attacks {self.player.name} for {damage} damage!")
            if not self.player.take_damage(damage):
                logging.info("You have been defeated by the Shadow Overlord.")
                break

# Character Classes for Player and Boss
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = Inventory()

    def take_damage(self, amount):
        self.health -= amount
        logging.info(f"{self.name} has {self.health} health remaining.")
        return self.health > 0

    def use_item(self, item):
        if item:
            logging.info(f"{self.name} uses {item.name}!")
            item.apply_effect(self)

# Inventory Management with Edge Case Handling
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_item(self):
        if self.items:
            return self.items.pop(0) #Get the first item for simplicity
        return None

class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply_effect(self, character):
        if self.effect == "heal":
            character.health += 20
            logging.info(f"{character.name}'s health is now {character.health}.")

#Simulated LLM Integration for Dialogue and Story
class DialogueManager:
    def display_dialogue(self, npc, player_choice):
        npc_response = self.generate_npc_response(npc, player_choice)
        logging.info(f"{npc.name}: {npc_response}")

    def generate_npc_response(self, npc, player_choice):
        # Simulate adaptive responses based on choices
        if player_choice == "help":
            return "Thank you, Brave warrior! I'll assist you in your joruney."
        elif player_choice == "ignore":
            return "How dissapointing! I thought you were here to help."
        return "Good luck, traveler."

# Example Characters and Combat
player = Character("Mario", 100)
boss = Character("Shadow Overlord", 150)
combat_system = Combat(player, boss)

# Adding items to inventory for testing edge cases
healing_potion = Item("healing Potion", "heal")
player.inventory.add_item(healing_potion)

#Dialogue and Story Interaction (Simulated LLM Content)
dialogue_manager = DialogueManager()

# Playtesting Structure 
def playtest():
    # Adaptive dialogue test
    logging.info("\n--- Dialogue Testing ---")
    player_choice = input("Do you choose to (help/ignore) the NPC? ")
    dialogue_manager.display_dialogue(NPC("Mystic Toad", "Thank you for helping me."), player_choice)

    # Edge case handling for missing item
    logging.info("\n--- Combat Testing ---")
    combat_system.engage_combat()

# NPC Class for testing purposes 
class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

# Running the playtest
playtest()

# Week 3: Final Adjustments, Debugging, and User Feedback

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Random Event Generator for Exploration
class RandomEventGenerator:
    def generate_event(self, player):
        event_type = random.choice(['item', 'enemy', 'nothing'])
        if event_type == 'item':
            self.find_item_event(player)
        elif event_type == 'enemy':
            self.enemy_encounter_event(player)
        else:
            logging.info("You continue exploring without any encounters.")

    def find_item_event(self, player):
        item = Item(name="Mushroom of Power", effect="heal")
        player.inventory.add_item(item)
        logging.info(f"Event: {player.name} found a hidden item: {item.name}!")

    def enemy_encounter_event(self, player):
        enemy = Character("Shadow Minion", health=30)
        combat_system = Combat(player, enemy)
        logging.info("Event: A weak enemy appeared!")
        combat_system.engage_combat()

# Combat Class with Turn-Based System
class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def calculate_damage(self, attacker):
        return random.randint(5, 20) # Reduced damage for minor enemies

    def engage_combat(self):
        logging.info(f"{self.player.name} is in combat with {self.enemy.name}!")

        while self.player.health > 0 and self.enemy.health > 0:
            damage = self.calculate_damage(self.player)
            logging.info(f"{self.player.name} attacks {self.enemy.name} for {damage} damage!")
            self.enemy.take_damage(damage)

            if self.enemy.health <= 0:
                logging.info(f"{self.player.name} defeated!")
                return True

            # Enemy's turn
            damage = self.calculate_damage(self.enemy)
            logging.info(f"{self.enemy.name} attacks {self.player.name} for {damage} damage!")
            if not self.player.take_damage(damage):
                logging.info("You were defeated by the enemy.")
                return False

# Character Class
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = Inventory()

    def take_damage(self, amount):
        self.health -= amount
        logging.info(f"{self.name}'s health: {self.health}")
        return self.health > 0

    def use_item(self, item):
        item.apply_effect(self)
        logging.info(f"{self.name} uses {item.name} and gains effect: {item.effect}")

# Inventory Management
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        logging.info(f"Added item: {item.name}")

    def use_item(self):
        if self.items:
            return self.items.pop(0)
        return None

# Item Class
class Item:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

    def apply_effect(self, character):
        if self.effect == "heal":
            character.health += 20
            logging.info(f"{character.name} heals and now has {character.health} health.")

# Dialogue Manager (Simualted)
class DialogueManager:
    def display_dialogue(self, npc, player_choice):
        response = self.generate_npc_response(npc, player_choice)
        logging.info(f"{npc.name}: {response}")

    def generate_npc_response(self, npc, player_choice):
        if player_choice == "help":
            return "Thank you for your help, brave hero!"
        elif player_choice == "ignore":
            return "I hoped you would help... but I see you have other priorities."

# Playtesting and User Feedback Preparation
def playtest():
    player = Character("Mario", 100)
    boss = Character("Shadow Overlord", 150)
    random_event_generator = RandomEventGenerator()

    # Testing dialogue interactions
    logging.info("\n--- Random Event Testing ---")
    random_event_generator.generate_event(player)

    # Testing random event generation
    logging.info("\n--- Random Event Testing ---")
    random_event_generator.generate_event(player)

    # Testing combat with boss
    combat_system = Combat(player, boss)
    logging.info("\n--- Boss Combat Testing ---")
    combat_system.engage_combat()

# NPC Class for Dialogue Testing
class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

# Run playtest
playtest()

# Documentation for Finalization 
def create_documentation():
    logging.info("\n--- Documentation and User Guide ---")
    logging.info("Welcome to 'Mario's Warriors' Game!")
    logging.info("In this game, you will explore, fight, and make decisions to protect the Mushroom Kingdom.")
    logging.info("Character Actions:\n- Choose actions in combat\n- Interact with NPCs for quests\n- Use items to regain health.")
    logging.info("Objective:\n- Defeat the Shadow Overload to restore peace.")
    logging.info("Explore, choose wisely, and become a hero!")

# Finalization call
create_documentation()
        