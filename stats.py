def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_char_dict(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def char_dict_to_sorted_dict(nums_char_dict):
    sorted_chars = []
    for ch in nums_char_dict:
        sorted_chars.append({"char": ch, "num": nums_char_dict[ch]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

def sort_on(d):
    return d["num"]