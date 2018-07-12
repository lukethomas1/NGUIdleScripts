from pynput.mouse import Button, Controller, Listener


pause = False


# Error to be used to retrieve mouse position after a click
class MouseLeftClick(Exception):
    pass


class MouseRightClick(Exception):
    pass


def consume_nonrightclicks(x, y, button, pressed):
    if button == Button.right and pressed:
        raise MouseRightClick(x, y, button, pressed)


def on_click(x, y, button, pressed):
    global pause

    if not pressed:
        return  # Return if this is a key up event

    if button == Button.right and pressed:
        if pause:
            print("Unpausing")
        else:
            print("Pausing")
        pause = not pause
    elif pause:
        pass
    elif button == Button.left and pressed:
        raise MouseLeftClick(x, y)


def get_mouse_click_position():
    while True:
        with Listener(on_click=on_click) as listener:
            try:
                listener.join()
            except MouseLeftClick as e:
                return e.args[0], e.args[1]
            except MouseRightClick as e:
                pass

