def get_num_words(text):  
    words = text.split()
    return len(words)

def count_letters(text):
    lower_letters = text.lower()
    list_letters = {}
    for char in lower_letters:
        if char in list_letters:        
            list_letters[char] +=1
        else:
            list_letters[char] = 1
    return list_letters

def sort_list(total_letters): 
    sorted_list = []
    for char, num in total_letters.items():
        keys = {"char": char, "num": num}
        sorted_list.append (keys)


    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(item):
    return item["num"]