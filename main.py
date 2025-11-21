from stats import number_of_words
from stats import number_of_char
from stats import sorted_char
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    
    sys.exit(1)    


    

def get_book_text(filepath):
    
    file_contents = ''
    
    with open(filepath) as f:
        file_contents = f.read()
    
        
    return f"{file_contents}"


        


def main():
    
    file_path = sys.argv[1]
    
    # get_book_text(file_path)
    
    # number_of_char(get_book_text(file_path))
    
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    
    print('----------- Word Count ----------')
    number_of_words(get_book_text(file_path))
    
    print('--------- Character Count -------')
    sorted_char(number_of_char(get_book_text(file_path)))
    
    print('============= END ===============')
    

    




main()