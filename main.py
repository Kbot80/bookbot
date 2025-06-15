path = ""
words = []
def get_book_text(path):
    count = 0
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        for word in words:
            if word in words:
                count += 1

    print(f"{count} words found in the document")
def main():
   get_book_text("./books/frankenstein.txt")

main()