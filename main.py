import string
from stats import get_num_words, get_ch_dict

#Takes a string as the path to a text and returns the text as a string
def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)

    num_words = get_num_words(book)
    print(f"Found {num_words} total words")

    ch_dict = get_ch_dict(book)
    print(ch_dict)

main()