from stats import count_word, num_of_characters


num_characters = num_of_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    content = get_book_text("books/frankenstein.txt").lower()
    value_stored = num_characters(content)
    my_dict = value_stored
    print(my_dict)
    # num_words = count_word(content)
    # print(f"Found {len(num_words)} total words")






main()
