path = ""
words = []
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)


def count_words(path):
    count = 0
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            if word in words:
                count += 1
    print(f"{count} words found in the document")


def count_letters(path):
    character_counter = {}
    with open(path) as f:
        file_contents = f.read()
        screening_text = file_contents.lower()
        for letter in screening_text:
            if letter not in character_counter:
                character_counter[letter] = 1
            else:
                character_counter[letter] += 1

        print(character_counter)


def main():
    # get_book_text("./books/frankenstein.txt")
    count_words("./books/frankenstein.txt")
    count_letters("./books/frankenstein.txt")

main()