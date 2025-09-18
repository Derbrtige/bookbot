from stats import get_book_text,count_words, how_many
def main():
    book = "/books/frankenstein.txt"
    text = get_book_text(book)
    words = count_words(text)
    characters = how_many(text)
    print(words)
    print(characters)