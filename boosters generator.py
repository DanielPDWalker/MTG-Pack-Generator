from mtgsdk import Set
import requests
from pathlib import Path
import os
import sys
import time

sets = Set.all()
sets_names = []


for i in sets:
    sets_names.append(i.name.lower())

# || User input and Interface ||
# ||||||||||||||||||||||||||||||


class KeyboardDisable():
    """Makes an object with which you can disable keyboard input."""

    def __init__(self):
        self.on = False
        import msvcrt

    def start(self):
        self.on = True

    def stop(self):
        self.on = False

    def __call__(self):
        while self.on:
            msvcrt.getwch()


def type_out(text):
    """First disables keyboard input then prints out the passed
    text's characters over time in the console/terminal window.
    """
    disable_typing.start()
    text = text + "\n"
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
    disable_typing.stop()


def check_input(saved_input):
    """Checks for yes and no awnsers from the user."""
    if saved_input.lower() == "!yes":
        return True
    if saved_input.lower() == "!no":
        return False


def select_input_set(saved_input):
    for i in sets:
        if saved_input == i.name.lower():
            return i.code


def choose_set():
    type_out("Please enter a set you would like a booster pack from:")
    saved_input = input()
    if saved_input.lower() in sets_names:
        return select_input_set(saved_input.lower())
    else:
        type_out("Sorry but {} is not a set.".format(saved_input))
        choose_set()


def choose_quantity():
    type_out("How many boosters would you like to generate?")
    type_out("(Please note each booster takes roughly 15 seconds).")
    saved_input = input()
    try:
        saved_input = int(saved_input)
        return saved_input
    except:
        type_out("Please enter only whole numerical values.")
        choose_quantity()


# This sets the object to disable the keyboard. Used in type_out().
disable_typing = KeyboardDisable()


# || Generating Packs ||
# ||||||||||||||||||||||


def create_and_open(pack_name, filename, mode):
    os.makedirs(pack_name, exist_ok=True)
    return open(filename, mode)


def pack_number(selected_set):
    n = 1
    f = Path(str(n) + ' ' + selected_set)
    while os.path.exists(f):
        n += 1
        f = Path(str(n) + ' ' + selected_set)
    return str(n) + ' ' + selected_set + '/'


def generate_packs(selected_set, quantity):
    while quantity > 0:
        counter = 1
        card = Set.generate_booster(selected_set)
        current_pack = pack_number(selected_set)
        for i in card:
            img_data = requests.get(
                'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=' +
                str(i.multiverse_id) + '&type=card').content
            with create_and_open(current_pack, current_pack + str(counter) + ' ' + str(i.name) + '.jpg', 'wb') as f:
                f.write(img_data)
                counter += 1
        quantity -= 1


def main():
    """Runs the menu and set up"""
    print("")
    print("##################################################")
    print("")
    the_loop = True
    while the_loop:
        set_holder = choose_set()
        quantity_holder = choose_quantity()
        generate_packs(set_holder, quantity_holder)


main()
