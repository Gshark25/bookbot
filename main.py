letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    char_dict = get_char_dict(text)
    print("-- Begin Report: Frankenstein --")
    print("")
    print(f"{num_words} words were found in the book")
    print("")
    for i in letters:
        char_count = char_dict[i]
        print(f"The {i} character was found {char_count}")
    print("")
    print("-- End Report --")

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    char = {}
    for c in text:
        lowered = c.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1
    return char

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
