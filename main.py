def num_words(contents):
    split_contents = contents.split()
    return len(split_contents)

def character_count(contents):  
    char_count = {}
    l_contents = contents.lower()
    for key in l_contents:
        if key in char_count:
            char_count[key] += 1
        else:
            char_count[key] = 1
    
    return char_count

def sort_character_count(dict):
    return dict["value"]

def print_char_count(char_count):

    list_characters = []

    for key in char_count:
        if key.isalpha():
            list_characters.append({"char" : key , "value" : char_count[key]})
    list_characters.sort(reverse = True, key=sort_character_count)
    
    for entry in list_characters:
        char = entry["char"]
        value = entry["value"]
        print(f"The '{char}' character was found {value} times")
    print("--- End Report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_count = character_count(file_contents)
        print_char_count(char_count)

main()