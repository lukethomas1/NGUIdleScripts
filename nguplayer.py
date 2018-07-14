
# System Imports
from pickle import dump, load
from time import sleep, time
from random import random
from os import path

# Third Party Imports
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyController

# Local Imports
import config
import utilities_mouse


class NotAButtonError(Exception):
    pass


class NGUPlayer:
    def __init__(self, do_reset=False):
        if do_reset:
            self.set_mouse_positions()
        else:
            self.position_dict = self.get_mouse_positions()
        self.mouse = MouseController()
        self.keyboard = KeyController()
        self.threads = []

    def click_button(self, button_name, delay=0.4):
        sleep(delay)
        if button_name not in self.position_dict:
            raise NotAButtonError("The button name: {} does not exist".format(button_name))
        x_pos, y_pos = self.position_dict[button_name]
        self.mouse.position = (x_pos, y_pos)
        self.mouse.click(Button.left)

    def set_mouse_positions(self):
        menu_buttons = input("Set positions for NGUButtons? (Blank for no): ")
        inventory_buttons = input("Set positions for InventoryButtons? (Blank for no): ")
        adventure = input("Set positions for AdventureButtons? (Blank for no): ")
        augmentation = input("Set positions for AugmentationButtons? (Blank for no): ")
        time_machine = input("Set positions for TimeMachineButtons? (Blank for no): ")
        blood_magic = input("Set positions for BloodMagicButtons? (Blank for no): ")
        self.position_dict = self.get_mouse_positions()

        buttons = []
        if menu_buttons:
            buttons += config.NGUButtons
        if inventory_buttons:
            buttons += config.InventoryButtons
        if adventure:
            buttons += config.AdventureButtons
        if augmentation:
            buttons += config.AugmentationButtons
        if time_machine:
            buttons += config.TimeMachineButtons
        if blood_magic:
            buttons += config.BloodMagicButtons

        for button in buttons:
            print("Click at the location of: " + str(button))
            # Store in dictionary
            x, y = utilities_mouse.get_mouse_click_position()
            self.position_dict[button] = (x, y)

        # Write dictionary to pickle file
        with open(config.PICKLE_FILE, "wb") as file:
            dump(self.position_dict, file)

    def get_mouse_positions(self):
        if path.isfile(config.PICKLE_FILE):
            with open(config.PICKLE_FILE, "rb") as file:
                return load(file)
        else:
            return {}

    def press_button(self, button_type, delay=0.5):
        self.keyboard.press(button_type)
        sleep(delay)
        self.keyboard.release(button_type)

    def reset_all_energy(self):
        # Press 'r' on the keyboard
        self.keyboard.press('r')
        self.keyboard.release('r')
        # Go to basic training menu
        self.click_button(config.NGUButtons.MENU_BASICTRAINING)
        # Click all minuses
        self.click_button(config.NGUButtons.ATTACK1_MINUS)
        self.click_button(config.NGUButtons.ATTACK2_MINUS)
        self.click_button(config.NGUButtons.ATTACK3_MINUS)
        self.click_button(config.NGUButtons.ATTACK4_MINUS)
        self.click_button(config.NGUButtons.ATTACK5_MINUS)
        self.click_button(config.NGUButtons.ATTACK6_MINUS)
        self.click_button(config.NGUButtons.DEFENSE1_MINUS)
        self.click_button(config.NGUButtons.DEFENSE2_MINUS)
        self.click_button(config.NGUButtons.DEFENSE3_MINUS)
        self.click_button(config.NGUButtons.DEFENSE4_MINUS)
        self.click_button(config.NGUButtons.DEFENSE5_MINUS)
        self.click_button(config.NGUButtons.DEFENSE6_MINUS)

    def basic_training_descending(self):
        self.click_button(config.NGUButtons.MENU_BASICTRAINING)
        self.press_button('r')
        self.click_button(config.NGUButtons.DEFENSE6_CAP)
        self.click_button(config.NGUButtons.DEFENSE5_CAP)
        self.click_button(config.NGUButtons.DEFENSE4_CAP)
        self.click_button(config.NGUButtons.DEFENSE3_CAP)
        self.click_button(config.NGUButtons.DEFENSE2_CAP)
        self.click_button(config.NGUButtons.DEFENSE1_CAP)
        self.click_button(config.NGUButtons.ATTACK6_CAP)
        self.click_button(config.NGUButtons.ATTACK5_CAP)
        self.click_button(config.NGUButtons.ATTACK4_CAP)
        self.click_button(config.NGUButtons.ATTACK3_CAP)
        self.click_button(config.NGUButtons.ATTACK2_CAP)
        self.click_button(config.NGUButtons.ATTACK1_CAP)

    def nuke_bosses(self, random_fight_chance=1):
        self.click_button(config.NGUButtons.MENU_FIGHTBOSS)
        self.click_button(config.NGUButtons.MENU_FIGHTBOSS_NUKE)
        if random() < random_fight_chance:
            self.click_button(config.NGUButtons.MENU_FIGHTBOSS_FIGHT)

    def adventure_forest(self):
        self.click_button(config.NGUButtons.MENU_ADVENTURE)
        self.click_button(config.NGUButtons.MENU_ADVENTURE_SCROLLBAR)
        self.click_button(config.AdventureButtons.CAVE)

    def feed_pit(self):
        self.click_button(config.NGUButtons.MENU_MONEYPIT)
        self.click_button(config.NGUButtons.MENU_MONEYPIT_FEED)
        self.click_button(config.NGUButtons.MENU_MONEYPIT_FEEDCONFIRM)

    def rebirth(self):
        self.click_button(config.NGUButtons.MENU_REBIRTH)
        self.click_button(config.NGUButtons.MENU_REBIRTH_REBIRTH)
        self.click_button(config.NGUButtons.MENU_REBIRTH_CONFIRM)

    def merge_inventory(self):
        """ Hold down D and click on an inventory item to merge all identical items with it """
        self.click_button(config.NGUButtons.MENU_INVENTORY)
        # Hold down d key
        with self.keyboard.pressed('d'):
            self.click_button(config.InventoryButtons.INV_HEAD)
            self.click_button(config.InventoryButtons.INV_CHEST)
            self.click_button(config.InventoryButtons.INV_LEGS)
            self.click_button(config.InventoryButtons.INV_FEET)
            self.click_button(config.InventoryButtons.INV_WEAPON)
            self.click_button(config.InventoryButtons.INV_ACCESSORY1)
            self.click_button(config.InventoryButtons.INV_ACCESSORY2)
            self.click_button(config.InventoryButtons.INV_SLOT1)

    def powerup_inventory(self):
        """ Hold down A and click on an inventory item to apply all possible powerups to it """
        self.click_button(config.NGUButtons.MENU_INVENTORY)
        # Hold down a key
        with self.keyboard.pressed('a'):
            self.click_button(config.InventoryButtons.INV_HEAD)
            self.click_button(config.InventoryButtons.INV_CHEST)
            self.click_button(config.InventoryButtons.INV_LEGS)
            self.click_button(config.InventoryButtons.INV_FEET)
            self.click_button(config.InventoryButtons.INV_WEAPON)
            self.click_button(config.InventoryButtons.INV_ACCESSORY1)
            self.click_button(config.InventoryButtons.INV_ACCESSORY2)
            self.click_button(config.InventoryButtons.INV_SLOT1)
            self.click_button(config.InventoryButtons.INV_INFINITYCUBE)

    def trash_inventory(self):
        """ Hold down shift and click on an inventory item to trash it (items) or consume it (powerups) """
        self.click_button(config.NGUButtons.MENU_INVENTORY)
        # Hold down shift
        with self.keyboard.pressed(Key.ctrl):
            self.click_button(config.InventoryButtons.INV_SLOT2)
            self.click_button(config.InventoryButtons.INV_SLOT3)
            self.click_button(config.InventoryButtons.INV_SLOT4)
            self.click_button(config.InventoryButtons.INV_SLOT5)
            self.click_button(config.InventoryButtons.INV_SLOT6)
            self.click_button(config.InventoryButtons.INV_SLOT7)
            self.click_button(config.InventoryButtons.INV_SLOT8)
            self.click_button(config.InventoryButtons.INV_SLOT9)
            self.click_button(config.InventoryButtons.INV_SLOT10)
            self.click_button(config.InventoryButtons.INV_SLOT11)
            self.click_button(config.InventoryButtons.INV_SLOT12)
            self.click_button(config.InventoryButtons.INV_SLOT13)
            self.click_button(config.InventoryButtons.INV_SLOT14)
            self.click_button(config.InventoryButtons.INV_SLOT15)
            self.click_button(config.InventoryButtons.INV_SLOT16)
            self.click_button(config.InventoryButtons.INV_SLOT17)

    def do_inventory(self):
        self.merge_inventory()
        self.powerup_inventory()
        self.trash_inventory()

    def do_augmentation(self):
        self.click_button(config.NGUButtons.MENU_BASICTRAINING)
        self.click_button(config.NGUButtons.ENERGY_INFINITE)
        self.click_button(config.NGUButtons.MENU_AUGMENTATION)
        self.click_button(config.AugmentationButtons.DANGERSCISSORS_PLUS)
        sleep(3)
        self.click_button(config.AugmentationButtons.DANGERSCISSORS_MINUS)
        self.click_button(config.AugmentationButtons.SAFETYSCISSORS_PLUS)

    def do_bloodmagic(self):
        self.click_button(config.NGUButtons.MENU_BLOODMAGIC)
        self.click_button(config.BloodMagicButtons.TACK_PLUS)
        self.click_button(config.BloodMagicButtons.CAST_SPELLS)
        self.click_button(config.BloodMagicButtons.BLOOD_BOOST)

    def do_time_machine(self):
        self.click_button(config.NGUButtons.MENU_TIMEMACHINE)
        self.click_button(config.NGUButtons.ENERGY_INFINITE)
        self.press_button('r')
        self.click_button(config.TimeMachineButtons.SPEED_PLUS)

    def thirty_min_run(self):
        rebirth_rate_seconds = 1820
        current_time = 1320
        time_before_first_rebirth = rebirth_rate_seconds - current_time
        start_time = time() - (rebirth_rate_seconds - time_before_first_rebirth)
        for index in range(30):
            print("30 Minute Run #" + str(index + 1))
            print("Time: " + str(time()))
            print("Start: " + str(start_time))
            count = 0
            while time() - start_time < rebirth_rate_seconds:
                # Do every time
                self.basic_training_descending()
                if 1400 > time() - start_time > 1200:
                    self.do_time_machine()
                else:
                    self.do_augmentation()
                self.do_bloodmagic()
                # Do every roughly 1 minute
                if count % 4 == 0 or (count < 20 and count % 2 == 0):
                    self.nuke_bosses()
                if count % 2 == 0:
                    self.do_inventory()
                # Specific for adventure
                if count < 3 or count % 4 == 0:
                    self.adventure_forest()

                # Browse through menus so I don't have to do it manually
                self.click_button(config.NGUButtons.MENU_BASICTRAINING)
                sleep(2)
                self.click_button(config.NGUButtons.MENU_FIGHTBOSS)
                sleep(2)
                self.click_button(config.NGUButtons.MENU_ADVENTURE)
                sleep(1)
                self.click_button(config.NGUButtons.MENU_INVENTORY)
                sleep(1)
                self.click_button(config.NGUButtons.MENU_AUGMENTATION)
                sleep(2)
                self.click_button(config.NGUButtons.MENU_BLOODMAGIC)
                sleep(4)
                count += 1
            print("Feeding pit...")
            self.feed_pit()
            print("Rebirthing...")
            self.rebirth()
            self.click_button(config.NGUButtons.MENU_BASICTRAINING)
            start_time = time()
