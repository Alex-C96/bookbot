def main(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        print(file_contents)
        print(word_count(file_contents))
        print(get_letter_count(file_contents))
        generate_report(file_contents, book_path)

def word_count(book):
    return len(book.split())

def get_letter_count(book):
    letter_dict = {}
    lower_case_book = book.lower()
    for i in range(len(lower_case_book)):
        current_char = lower_case_book[i] 
        if current_char in letter_dict:
            letter_dict[current_char] += 1
        else:
            letter_dict[current_char] = 1
    return letter_dict

def generate_report(book, book_path):
    dict = get_letter_count(book)
    report_list = []
    for key, value in dict.items():
        if key.isalpha():
            report_list.append({"char": key, "num": value})
    report_list.sort(reverse=True, key=sort_on)
    print(f'--- Begin Report of {book_path} ---\n')
    print(f'{word_count(book)} words found in the document\n')
    print("\n\n")
    for item in report_list:
        print(f'The \'{item["char"]}\' character was found \'{item["num"]}\' times')
    print("--- End Report ---\n")
    
def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    main("books/frankenstein.txt")