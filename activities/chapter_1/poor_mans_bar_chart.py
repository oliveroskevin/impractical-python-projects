from collections import defaultdict
import pprint

SENTENCE = 'Vulpes celeris fusca canem pigrum supersilit'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

d = defaultdict(list)

for letter in list(ALPHABET):
    d[letter.lower()]

for letter in list(SENTENCE):
    if letter != ' ':
        d[letter.lower()].append(letter.lower())

pprint.pprint(d)
