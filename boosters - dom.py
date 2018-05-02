from mtgsdk import Set
import requests
from pathlib import Path
import os


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


card = Set.generate_booster('dom')
current_pack = pack_number()


for i in card:
    img_data = requests.get(
        'http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=' +
        str(i.multiverse_id) + '&type=card').content
    with create_and_open(current_pack + str(i.name) + '.jpg', 'wb') as f:
        f.write(img_data)
