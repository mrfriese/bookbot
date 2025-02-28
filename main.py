from stats import get_number_of_words, get_char_dict, char_dict_to_sorted_dict, sort_on
import sys

def main():
    if not len(sys.argv) == 2:
         displayHelp()
    book_path = getPath()
    text = get_book_text(book_path)
    num_words = get_number_of_words(text)
    char_dict = get_char_dict(text)
    char_dict_sorted = char_dict_to_sorted_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in char_dict_sorted:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print()
    print("============= END ===============")
    print()
    

def displayHelp(): 
	"""Prints to command line how to use the program"""
	print("Usages: python3 main.py <path_to_book>")
	sys.exit(1)
     
     
def getPath(): 
	"""returns path to book (relative)"""
	return sys.argv[1]# gets books/input.txt 


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()