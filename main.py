def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    char_dict = get_char_dict(text)
    char_dict_sorted = char_dict_to_sorted_dict(char_dict)

    print( f"--- report on {book_path} ---")
    print(f"{num_words} words found in this document.")
    print()

    for item in char_dict_sorted:
        if not item['char'].isalpha():
            continue
        print(f"the '{item['char']} character appeared {item['num']} times.")

    print()
    print(" --- End Report ---")

    
def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_char_dict(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_on(d):
    return d["num"]

def char_dict_to_sorted_dict(nums_char_dict):
    sorted_chars = []
    for ch in nums_char_dict:
        sorted_chars.append({"char": ch, "num": nums_char_dict[ch]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars

main()