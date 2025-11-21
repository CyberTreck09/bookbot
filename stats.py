def number_of_words(booktext):
    
    word_count = len(booktext.split())
    
    print(f"Found {word_count} total words")
    
    
def number_of_char(booktext):
    char_count = {}
    for char in booktext:
        
        all_char = char.lower()
        if all_char in char_count:
            char_count[all_char] += 1
            
        else: 
            char_count[all_char] = 1
        
    return char_count

def sort_on(items):
    return items["num"]


def sorted_char(dict):
    
    char_list = []
    
    for key in dict:
        
        num = dict[key]
        
        char_list.append({
            "char": key,
            "num": num
        })
        

    reversed_list = sorted(char_list, key=lambda x: x["num"], reverse=True)
    
    for i in range(len(reversed_list)):
        char = reversed_list[i]["char"]
        if(char.isalpha() == False):
            continue
        print(f"{reversed_list[i]["char"]}: {reversed_list[i]["num"]}")