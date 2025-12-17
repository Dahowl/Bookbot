import sys

def get_book_text(book):
    with open(book) as f:
        return f.read()

from stats import get_num_words, count_letters, sort_list

def main(): 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")  
        sys.exit(1)  
    book_path = sys.argv[1]
    text = get_book_text(book_path)  
    total_words = get_num_words(text)  
    total_letters = count_letters(text)
    
    print(f'Found {total_words} total words')

    sorted_list = sort_list(total_letters)
    for symbol in sorted_list:
        if not symbol["char"].isalpha(): 
            continue
        else:
            print (f'{symbol["char"]}: {symbol["num"]}')



main()
