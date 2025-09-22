from stats import get_book_text,count_words, how_many, char_list, sorted_list
import sys 



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        text = get_book_text(book)

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