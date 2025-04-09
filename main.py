from stats import number_of_words
from stats import number_of_letters
from stats import get_book_text
from stats import chars_dict_to_sorted_list
import sys

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    text = get_book_text(sys.argv[1])

    num_words = number_of_words()
    
    char_counts = number_of_letters(text)
    
    sorted_chars = chars_dict_to_sorted_list(char_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")    
   

main()

