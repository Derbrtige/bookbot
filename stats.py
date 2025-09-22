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

def char_list (text):
    counts = how_many(text)
    character = []
    for c,n in counts.items():
        entry = {"char": c, "num": n}
        character.append(entry)

    return character

def sorted_list (text):
    filtered = []
    chars = char_list(text)
    chars.sort(reverse=True, key=lambda item: item["num"])
    filtered = [entry for entry in chars if entry["char"].isalpha()]
    return filtered

