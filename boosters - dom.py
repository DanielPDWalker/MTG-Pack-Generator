from mtgsdk import Set
import requests
from pathlib import Path
import os
import sys
import time


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


# This sets the object to disable the keyboard. Used in type_out().
disable_typing = KeyboardDisable()


def create_and_open(filename, mode):
    os.makedirs(current_pack, exist_ok=True)
    return open(filename, mode)


def pack_number():
    n = 1
    f = Path(str(n))
    while os.path.exists(f):
        n += 1
        f = Path(str(n))
    return str(n) + '/'


selected_set = 'dom'
card = Set.generate_booster(selected_set)
current_pack = pack_number()


for i in card:
    img_data = requests.get(
        'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=' +
        str(i.multiverse_id) + '&type=card').content
    with create_and_open(current_pack + str(i.name) + '.jpg', 'wb') as f:
        f.write(img_data)
