def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        print(word_count(file_contents))

def word_count(book):
    return len(book.split())

if __name__ == "__main__":
    main()