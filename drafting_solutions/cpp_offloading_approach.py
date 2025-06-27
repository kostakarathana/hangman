from hangman_game import Hangman
import time
import cython_accel
from tqdm import tqdm
from collections import defaultdict

with open('../text_files/words.txt', 'r') as f:
    WORD_LIST = [line.strip().lower() for line in f if line.strip()]

WORDS_BY_LENGTH = defaultdict(list)
for i in range(1,46):
    WORDS_BY_LENGTH[f"{i}"] = [word for word in WORD_LIST if len(word) == i]

class AlgorithmicSolution:
    def __init__(self, force_word=None):
        self.game = Hangman(force_word)
        self.word_length = self.game.get_length()
        self.letters_guessed: set[str] = set()
        self.filtered_words = WORDS_BY_LENGTH[f"{self.word_length}"]

    def see_progress(self):
        return self.game.get_status()

    def find_letter_to_guess(self):
        freq = cython_accel.compute_frequencies(self.filtered_words, self.letters_guessed)
        if not freq:
            return None
        best = max(freq.items(), key=lambda x: x[1])[0]
        self.letters_guessed.add(best)
        return best

    def take_guess(self):
        letter = self.find_letter_to_guess()
        if not letter:
            return
        positions = self.game.guess_letter(letter)
        self.filtered_words = cython_accel.filter_words(self.filtered_words, letter, positions)

if __name__ == "__main__":

 
    successes = 0
    trials = 0
    start = time.time()

    for i, word in tqdm(enumerate(WORD_LIST), total=len(WORD_LIST)):

        if i % 1000 != 0:
            continue
        trials += 1
        sol = AlgorithmicSolution(force_word=word)
        while sol.see_progress() == "processing":
            sol.take_guess()
        if sol.see_progress() == "win":
            successes += 1

    print("\n✅ DONE")
    print(f"Total Words Tested: {trials}")
    print(f"Successes: {successes}")
    print(f"Success Rate: {100 * successes / trials:.2f}%")
    print(f"Time taken: {time.time() - start:.2f} seconds")