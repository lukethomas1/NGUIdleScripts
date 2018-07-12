
# System Imports
from pickle import dump, load
from time import sleep, time
from random import random

# Third Party Imports
from pynput.mouse import Button, Controller

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
        self.mouse = Controller()
        self.threads = []
        self.bt_toggle = 0

    def click_button(self, button_name, delay=0.2):
        sleep(delay)
        if button_name not in self.position_dict:
            raise NotAButtonError("The button name: {} does not exist".format(button_name))
        x_pos, y_pos = self.position_dict[button_name]
        self.mouse.position = (x_pos, y_pos)
        self.mouse.click(Button.left)

    def set_mouse_positions(self):
        self.position_dict = {}
        for button in config.NGUButtons:
            print("Click at the location of: " + str(button))
            # Store in dictionary
            x, y = utilities_mouse.get_mouse_click_position()
            self.position_dict[button] = (x, y)

        # Write dictionary to pickle file
        with open(config.PICKLE_FILE, "wb") as file:
            dump(self.position_dict, file)

    def get_mouse_positions(self):
        with open(config.PICKLE_FILE, "rb") as file:
            return load(file)

    def reset_all_energy(self):
        # Press 'r' on the keyboard
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

    def basic_training_descending(self, alternate=True):
        self.reset_all_energy()
        if alternate and self.bt_toggle == 0:
            self.bt_toggle = 1
            self.click_button(config.NGUButtons.ATTACK6_CAP)
            self.click_button(config.NGUButtons.ATTACK5_CAP)
            self.click_button(config.NGUButtons.ATTACK4_CAP)
            self.click_button(config.NGUButtons.ATTACK3_CAP)
            self.click_button(config.NGUButtons.ATTACK2_CAP)
            self.click_button(config.NGUButtons.ATTACK1_CAP)
            self.click_button(config.NGUButtons.DEFENSE6_CAP)
            self.click_button(config.NGUButtons.DEFENSE5_CAP)
            self.click_button(config.NGUButtons.DEFENSE4_CAP)
            self.click_button(config.NGUButtons.DEFENSE3_CAP)
            self.click_button(config.NGUButtons.DEFENSE2_CAP)
            self.click_button(config.NGUButtons.DEFENSE1_CAP)
        else:
            self.bt_toggle = 0
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

    def nuke_bosses(self, random_fight_chance=0.25):
        self.click_button(config.NGUButtons.MENU_FIGHTBOSS)
        self.click_button(config.NGUButtons.MENU_FIGHTBOSS_NUKE)
        if random() < random_fight_chance:
            self.click_button(config.NGUButtons.MENU_FIGHTBOSS_FIGHT)

    def adventure_forest(self):
        self.click_button(config.NGUButtons.MENU_ADVENTURE)
        self.click_button(config.NGUButtons.MENU_ADVENTURE_SCROLLBAR)
        self.click_button(config.NGUButtons.MENU_ADVENTURE_SCROLLFOREST)

    def feed_pit(self):
        self.click_button(config.NGUButtons.MENU_MONEYPIT)
        self.click_button(config.NGUButtons.MENU_MONEYPIT_FEED)
        self.click_button(config.NGUButtons.MENU_MONEYPIT_FEEDCONFIRM)

    def rebirth(self):
        self.click_button(config.NGUButtons.MENU_REBIRTH)
        self.click_button(config.NGUButtons.MENU_REBIRTH_REBIRTH)
        self.click_button(config.NGUButtons.MENU_REBIRTH_CONFIRM)

    def thirty_min_run(self):
        start_time = time() - 3000
        for index in range(30):
            print("30 Minute Run #" + str(index + 1))
            print("Time: " + str(time()))
            print("Start: " + str(start_time))
            while time() - start_time < 3650:
                self.basic_training_descending()
                self.nuke_bosses()
                self.adventure_forest()
                self.click_button(config.NGUButtons.MENU_BASICTRAINING)
                sleep(10)
            print("Feeding pit...")
            self.feed_pit()
            print("Rebirthing...")
            self.rebirth()
            self.click_button(config.NGUButtons.MENU_BASICTRAINING)
            start_time = time()
