import sys
from stats import (get_book_text, count_words, count_letters, sorted_characters)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]
    book = get_book_text(path)
    count = count_words(book)
    text_list = count_letters(book)
    sorted_list = sorted_characters(text_list)




def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    # print(book)
    print("----------- Word Count ----------")
    print(count)
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["ch"].isalpha():
            continue
        print(f"{item["ch"]}: {item["num"]}")
    print("============= END ===============")

main()