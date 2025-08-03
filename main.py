from stats import split_words, get_char_count, sort_chars

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = len(split_words(book_text))
    char_dict = get_char_count(book_text)
    sorted_chars = sort_chars(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()









    

main()