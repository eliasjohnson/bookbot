def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string"""
    with open(filepath, "r") as f:
        return f.read()
def count_workds(text):
    """counts number of words as string"""
    pass 

def main():
    """main function"""
    print(get_book_text("books/frankenstein.txt"))


main()
