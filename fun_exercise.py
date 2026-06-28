# run this script in online-python.com or github codespace or any python interpreter
# try to figure out what this program does
# add some more items inside the 5 lists and make your own silly sentence

import random

adjectives = ["happy", "sad", "angry"]
characters = ["dragon", "knight", "peasant"]
verbs = ["eat", "crush", "throw"]
objects = ["rocks", "leaves", "apples"]
places = ["beach", "meadow", "airport"]

random_adjective = random.choice(adjectives)
random_character = random.choice(characters)
random_verb = random.choice(verbs)
random_object = random.choice(objects)
random_place = random.choice(places)

print("The " + random_adjective + " " + random_character + " likes to "
      + random_verb + " " + random_object + " on the " + random_place + ".")

















