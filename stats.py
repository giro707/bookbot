import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def number_of_words():
    text = get_book_text(sys.argv[1])
    words = text.split()
    total_words = len(words)
    return total_words

def number_of_letters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
    
    
    

