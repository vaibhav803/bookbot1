from stats import count_word, num_of_characters,count_on,sorted
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

num_characters = num_of_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    content = get_book_text(sys.argv[1]).lower()
    value_stored = num_of_characters(content)
    # my_dict = value_stored
    num_words = count_word(content)
    print(f"Found {num_words} total words")
    final_answer = sorted(value_stored)
    for i in final_answer:
        print(f"{i["char"]}: {i["num"]}")


    






main()
