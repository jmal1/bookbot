def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    sorted_list = sort_dict(letter_count)


    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("\n")
    print_letter_report(sorted_list)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    letters_dict = dict()
    for letter in text:
        letter = letter.lower()
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    letters = []
    for letter in dict:
        if letter.isalpha():
            letter_dict = {'letter': letter, 'num': dict[letter]}
            letters.append(letter_dict)
        letters.sort(reverse=True, key=sort_on)
    return letters

def print_letter_report(dict):
    for letterDict in dict:
        print(f"The '{letterDict["letter"]}' character was found {letterDict["num"]} times")

main()