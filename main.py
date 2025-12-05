from stats import get_num_words, char_count

def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string"""
    with open(filepath, "r") as f:
        return f.read()

character_count = char_count(get_book_text("books/frankenstein.txt"))

def main():
    """main function"""
    print(get_num_words(get_book_text("books/frankenstein.txt"))) 
    print(char_count(get_book_text("books/frankenstein.txt")))

main()
