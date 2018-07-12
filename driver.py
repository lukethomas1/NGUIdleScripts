
# System Imports
from time import sleep, time

# Local Imports
import config
import positioner
import nguplayer
import utilities_mouse

if __name__ == "__main__":
    do_update = False
    player = nguplayer.NGUPlayer(do_reset=do_update)
    player.thirty_min_run()
