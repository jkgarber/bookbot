from stats import get_word_count
from stats import get_char_counts
from stats import get_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    path_to_book = sys.argv[1]
    content = get_book_text(path_to_book)
    word_count = get_word_count(content)
    char_counts = get_char_counts(content)
    sorted_list = get_sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")


def get_book_text(path):
    with open(path) as f:
        content = f.read()
        return content


main()
