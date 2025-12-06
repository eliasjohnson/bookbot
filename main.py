from pprint import PrettyPrinter
from stats import get_num_words, char_count

def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string"""
    with open(filepath, "r") as f:
        return f.read()

character_count = char_count(get_book_text("books/frankenstein.txt"))

def main():
    """main function"""
    filepath = "books/frankenstein.txt"
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath} ")
    print("----------- Word Count ----------")
    print(get_num_words(get_book_text(filepath)))
    print("--------- Character Count -------")
    print(char_count(get_book_text(filepath)))
    print("============= END ===============\n")

main()

#case number 21693998