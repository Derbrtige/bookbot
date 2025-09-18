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

def main ():
    book = "books/frankenstein.txt"
    print(f"{count_words(book)} words found in the document")
main()

