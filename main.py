import sys
from stats import split_words, get_char_count, sort_chars

def main():
    if len(sys.argv) != 2:
        print( "Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = len(split_words(book_text))
    char_dict = get_char_count(book_text)
    sorted_chars = sort_chars(char_dict)

    print_report(book_path, word_count, sorted_chars)


def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()


def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")







    

main()