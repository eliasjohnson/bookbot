def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string"""
    with open(filepath, "r") as f:
        return f.read()

def count_words():
    """counts number of words as string"""
    text = get_book_text("books/frankenstein.txt")
    result = len(text.split())
    return f"Found {result} total words"

def main():
    """main function"""
    print(count_words())


main()
