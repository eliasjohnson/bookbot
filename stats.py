def get_num_words(text):
    """counts number of words as string"""
    words = len(text.split())
    return f"Found {words} total words"

def char_count(text):
    """counts number of characters in text"""
    text = text.lower()
    char_dict = {
        'a': 0,
        'b':0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0
    }
    for i in text:
        if i in char_dict:
            char_dict[i] += 1
    return char_dict
