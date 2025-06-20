def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        if word in words:
            count += 1
    return f"Found {count} total words"


character_counter = {}
def count_letters(file_contents):
    screening_text = file_contents.lower()
    for letter in screening_text:
        if letter not in character_counter:
            character_counter[letter] = 1
        else:
            character_counter[letter] += 1
    return character_counter

# I don't understand the code below this
def sort_key(a):
    return a["num"]


def sorted_characters(character_counter):
    sorted = []
    for character in character_counter:
        sorted.append({"ch":character, "num": character_counter[character]})
    sorted.sort(reverse = True, key = sort_key)
    return sorted