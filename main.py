import string
import sys
from stats import get_num_words, get_ch_dict, sort_dict, chars_dict_to_sorted_list

#Takes a string as the path to a text and returns the text as a string
def get_book_text(filepath: str) -> str:
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
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        num_words = get_num_words(book)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        ch_dict = get_ch_dict(book)
        sorted_ch = sort_dict(ch_dict)
        sorted_list = chars_dict_to_sorted_list(ch_dict)

        for i in sorted_ch:
            if i[0].isalpha():
                print(f"{i[0]}: {i[1]}")
        
        print(sorted_list)

        print("============= END ===============")

main()