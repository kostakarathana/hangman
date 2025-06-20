import time

def sort_words_by_length(input_file, output_file):
    with open(input_file, 'r') as f:
        words = [line.strip() for line in f if line.strip()]
    words.sort(key=len)
    with open(output_file, 'w') as f:
        for word in words:
            f.write(word + '\n')


if __name__ == "__main__":
    sort_words_by_length("text_files/words.txt", "text_files/words_by_length")
