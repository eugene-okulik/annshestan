dictionary = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def copying(pairs):
    for word, quantity in pairs.items():
        print(word * quantity)


copying(dictionary)
