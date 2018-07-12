# System Imports
from pickle import dump, load

# Local Imports
import utilities_mouse
import config


def set_mouse_positions():
    position_dict = {}
    for button in config.NGUButtons:
        print("Click at the location of: " + str(button))
        # Store in dictionary
        x, y = utilities_mouse.get_mouse_click_position()
        position_dict[button] = (x, y)

    # Write dictionary to pickle file
    with open(config.PICKLE_FILE, "wb") as file:
        dump(position_dict, file)


def get_mouse_positions():
    with open(config.PICKLE_FILE, "rb") as file:
        return load(file)


if __name__ == "__main__":
    positions = get_mouse_positions()
    print(str(positions))
