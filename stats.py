def split_words(book_text):
    return book_text.split()


def get_char_count(book_text):
    char_dict = {}
    for char in book_text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_chars_sort(count):
    return count["num"]

def sort_chars(char_dict):
    sorted_chars = []
    for char in char_dict:
        temp = {"char": char, "num": char_dict[char]}
        sorted_chars.append(temp)
    sorted_chars.sort(reverse=True, key=sort_chars_sort)
    return sorted_chars