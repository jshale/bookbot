import sys

from stats import get_num_words, count_characters, sort_characters


def get_book_text(path):
    with open(path, 'r') as book:
        bookContent = book.read()

    return bookContent


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book> ")
        sys.exit(1)

    path = sys.argv[1]

    bookContent = get_book_text(path)

    num_words = get_num_words(bookContent)

    print(f"Found {num_words} total words")

    character_dictionay = count_characters(bookContent)

    character_dictionay_list = sort_characters(character_dictionay)

    for item in character_dictionay_list:
        print(f"{item["letter"]}: {item["count"]}")


main()
