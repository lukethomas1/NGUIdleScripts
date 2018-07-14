
# System Imports
from time import sleep, time
import sys
import os
# Third Party Imports
from pynput.keyboard import Listener, Key

# Local Imports
import nguplayer


class HomeKeyPressed(Exception):
    pass


def on_press(key):
    if key == Key.home:
        os._exit(0)


if __name__ == "__main__":
    listener = Listener(on_press=on_press)
    listener.start()
    do_update = False
    player = nguplayer.NGUPlayer(do_reset=do_update)
    player.thirty_min_run()
