# coding: utf-8

# This file is written by Mike Giarlo @mjgiarlo - https://github.com/mjgiarlo
# Thanks, Mike!

from random import randint, choice

def zalgo(text, intensity=50):
    zalgo_threshold = intensity
    zalgo_chars = [unichr(i) for i in range(0x0300, 0x036F + 1)]
    zalgo_chars.extend([u'\u0488', u'\u0489'])
    source = text.decode('utf8')
    if not _is_narrow_build:
        source = _insert_randoms(source)
    zalgoized = []
    for letter in source:
        zalgoized.append(letter)
        zalgo_num = randint(0, zalgo_threshold) + 1
        for _ in range(zalgo_num):
            zalgoized.append(choice(zalgo_chars))
    response = choice(zalgo_chars).join(zalgoized)
    return response.encode('utf8', 'ignore')


def _insert_randoms(text):
    random_extras = [unichr(i) for i in range(0x1D023, 0x1D045 + 1)]
    newtext = []
    for char in text:
        newtext.append(char)
        if randint(1, 5) == 1:
            newtext.append(choice(random_extras))
    return u''.join(newtext)


def _is_narrow_build():
    try:
        unichr(0x10000)
    except ValueError:
        return True
    return False
