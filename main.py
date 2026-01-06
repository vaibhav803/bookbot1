from stats import count_word

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    content = get_book_text("books/frankenstein.txt")
    num_words = count_word(content)
    print(f"Found {len(num_words)} total words")



main()
