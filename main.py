from stats import (get_book_text, count_words, count_letters, sorted_characters)
path = "books/frankenstein.txt"
book = get_book_text(path)
count = count_words(path)
text_list = count_letters(path)
sorted_list = sorted_characters(text_list)



def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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