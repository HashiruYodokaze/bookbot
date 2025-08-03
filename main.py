def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count = len(word_split(book_text))
    
    print(f"{word_count} words found in the document")


def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()

def word_split(book_text):
    return book_text.split()








    

main()