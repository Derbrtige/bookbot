def get_book_text (book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def count_words (book):
    with open(book) as f:
        words = f.read()
        word = words.split()
        num_words = len(word)
    return num_words

def how_many (text):
    characters = {}
    lower_contents = text.lower()
    for character in lower_contents:
        characters[character] = characters.get(character,0)+1

    return characters

def main ():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
#    print(f"{count_words(book)} words found in the document")
    print(how_many(text))
main()