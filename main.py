from stats import get_num_words, char_count, sorted_list

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
    sortd_list = sorted_list(character_count)
    for item in sortd_list:
        char = item["char"]
        count = item["num"]
        if char.isalpha():# only print if char.isalpha()
            print(f"{char}: {count}")
        else:
            continue
    print("============= END ===============\n")

if __name__ == "__main__":
    main()



#case number 21693998