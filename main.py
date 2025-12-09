import sys
from stats import get_num_words, char_count, sorted_list

def get_book_text(filepath):
    """takes a filepath as input and returns the contents of the file as a string"""
    with open(filepath, "r") as f:
        return f.read()


def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    print("\n============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath} ")
    print("----------- Word Count ----------")
    print(get_num_words(get_book_text(filepath)))
    print("--------- Character Count -------")
    character_count = char_count(get_book_text(filepath))
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