import string
import sys
from stats import get_num_words, get_ch_dict, sort_dict

#Takes a string as the path to a text and returns the text as a string
def get_book_text(filepath: str):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else:
        book_path = sys.argv[1]
        book = get_book_text(book_path)

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        num_words = get_num_words(book)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        ch_dict = get_ch_dict(book)
        sorted_ch = sort_dict(ch_dict)

        for i in sorted_ch:
            if i[0].isalpha():
                print(f"{i[0]}: {i[1]}")
        
        print("============= END ===============")
        
main()