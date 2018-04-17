__author__ = 'Meg'

animals = {'alligator': 0, 'ant': 0, 'bear': 0, 'bee': 0, 'bird': 0, 'camel': 0, 'cat': 0, 'cheetah': 0,
           'chicken': 0, 'chimpanzee': 0, 'cow': 0, 'crocodile': 0, 'deer': 0,  'dog': 0,  'dolphin': 0,
           'duck': 0, 'eagle': 0, 'elephant': 0, 'fish': 0, 'fly': 0, 'fox': 0, 'frog': 0, 'giraffe': 0,
           'goat': 0, 'goldfish': 0, 'hamster': 0, 'hippopotamus': 0, 'horse': 0, 'kangaroo': 0, 'kitten': 0,
           'leopard': 0, 'lion': 0, 'lizard': 0, 'lobster': 0, 'monkey': 0, 'octopus': 0, 'ostrich': 0,
           'otter': 0, 'owl': 0, 'oyster': 0, 'panda': 0, 'parrot': 0, 'pelican': 0, 'pig': 0, 'pigeon': 0,
           'porcupine': 0, 'puppy': 0, 'rabbit': 0, 'rat': 0, 'reindeer' : 0, 'rhinoceros': 0, 'rooster': 0,
           'scorpion': 0, 'seal': 0, 'shark': 0, 'sheep': 0, 'shrimp': 0, 'snail': 0, 'snake': 0, 'sparrow': 0,
           'spider': 0, 'squid': 0, 'squirrel': 0, 'swallow': 0, 'swan': 0, 'tiger': 0, 'toad': 0,
           'tortoise': 0, 'turtle': 0, 'vulture': 0, 'walrus': 0, 'weasel': 0, 'whale': 0, 'wolf': 0, 'zebra': 0}

body_parts = {'leg': 0, 'tongue': 0, 'blood': 0, 'bone': 0, 'stomach': 0, 'chin': 0, 'tooth': 0, 'foot': 0, 'skin': 0,
              'wrist': 0, 'hand': 0, 'thumb': 0, 'arm': 0, 'feet': 0, 'brain': 0, 'shoulders': 0, 'nail': 0, 'hands': 0,
              'eye': 0, 'hip': 0, 'thumbs': 0, 'shoulder': 0, 'head': 0, 'eyes': 0, 'beard': 0, 'back': 0, 'toes': 0,
              'ears': 0, 'moustache': 0, 'knees': 0, 'finger': 0, 'hair': 0, 'throat': 0, 'body': 0, 'ear': 0, 'muscle': 0,
              'elbow': 0, 'toe': 0, 'cheek': 0, 'legs': 0, 'chest': 0, 'neck': 0, 'face': 0, 'mouth': 0, 'ankle': 0,
              'nose': 0, 'teeth': 0, 'fingers': 0, 'heart': 0, 'knee': 0, 'flesh': 0, 'lip': 0 }

buildings = {'cathedral': 0, 'supermarket': 0, 'cafe': 0, 'shrine': 0, 'apartment building': 0, 'bakery': 0, 'airport': 0,
             'fire department': 0, 'gas station': 0, 'book store': 0, 'bowling alley': 0, 'church': 0, 'mosque': 0,
             'school building': 0, 'library': 0, 'temple': 0, 'restaurant': 0, 'museum': 0, 'cinema': 0, 'movie theater': 0,
             'house': 0, 'hospital': 0, 'bus terminal': 0, 'convenience store': 0, 'shopping mall': 0, 'office building': 0,
             'barber shop': 0, 'bank': 0, 'train station': 0, 'department store': 0, 'post office': 0}

clothes = {'belt': 0, 'jumper': 0, 'pajamas': 0, 'shoes': 0, 'pants': 0, 'coat': 0, 'jeans': 0, 'overalls': 0, 'trousers': 0,
           'overcoat': 0, 'underpants': 0, 'sweatshirt': 0, 'skirt': 0, 'blouse': 0, 'shorts': 0, 'slacks': 0, 'boots': 0,
           't-shirt': 0, 'hat': 0, 'sweater': 0, 'scarf': 0, 'stockings': 0, 'mini-skirt': 0, 'pantyhose': 0, 'cap': 0,
           'raincoat': 0, 'cardigan': 0, 'sweat-shirt': 0, 'socks': 0, 'tie': 0, 'underclothes': 0, 'gloves': 0, 'vest': 0,
           'shirt': 0, 'dress': 0, 'jacket': 0, 'slippers': 0, 'suit': 0, 'undershirt': 0}

fruit = {'banana': 0, 'blueberry': 0, 'prune': 0, 'blackberry': 0, 'persimmon': 0, 'cranberry': 0, 'melon': 0, 'peach': 0,
         'lemon': 0, 'nectarine': 0, 'pineapple': 0, 'strawberry': 0, 'lime': 0, 'apple': 0, 'fig': 0, 'grapes': 0,
         'cherry': 0, 'pear': 0, 'orange': 0, 'plum': 0, 'tangerine': 0, 'currant': 0, 'raspberry': 0, 'apricot': 0,
         'watermelon': 0, 'grape': 0, 'kiwi': 0, 'kumquat': 0, 'grapefruit': 0, 'pomegranate': 0}

vegetables = {'sweet potato': 0, 'carrot': 0, 'okra': 0, 'potato': 0, 'eggplant': 0, 'broccoli': 0, 'beet': 0, 'peas': 0,
              'kale': 0, 'lettuce': 0, 'Japanese radish': 0, 'pumpkins': 0, 'asparagus': 0, 'tomatoes': 0,
              'Brussels sprouts': 0, 'onion': 0, 'cauliflower': 0, 'radish': 0, 'spinach': 0, 'Chinese cabbage': 0, 'corn': 0,
              'cabbage': 0, 'green pepper': 0, 'cucumber': 0, 'beans': 0, 'celery': 0}

categories = {'animals:': animals, 'body parts': body_parts, 'buildings': buildings, 'clothes': clothes, 'fruit': fruit, 'vegetables': vegetables}

def setZero (cat):
    for thing in categories[cat]:
        categories[cat][thing] = 0