from stats import get_book_text,count_words, how_many, char_list, sorted_list
def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    #words = count_words(book)
    #filtered = sorted_list(text)
    #print(words)
    #print(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")

    for entry in sorted_list(text):
        ch = entry["char"]
        if ch.isalpha():
            print(f"{ch}: {entry['num']}")


    print("============= END ===============")
main()