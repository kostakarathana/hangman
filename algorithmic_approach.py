from hangman_game import Hangman
from collections import defaultdict
import numpy as np
import pandas as pd
import time

try:
    from tqdm import tqdm
    use_tqdm = True
except ImportError:
    use_tqdm = False

# Global: Read the word list once
with open('text_files/words.txt', 'r') as f:
    WORD_LIST = [line.strip().lower() for line in f if line.strip()]

class AlgorithmicSolution:
    def __init__(self, force_word=None):
        self.game = Hangman(force_word)
        self.word_length = self.game.get_length()
        self.letters_guessed = set()
        self.filtered_words = [word for word in WORD_LIST if len(word) == self.word_length]

    def _cheat_and_see_word(self): # NEVER to be used except in testing!
        return self.game._get_word()
    
    def see_progress(self): 
        return self.game.get_status()

    def find_letter_to_guess(self):
        freq = defaultdict(int)
        for word in self.filtered_words:
            for char in word:
                if char not in self.letters_guessed:
                    freq[char] += 1
        if not freq:
            return None
        maximum = max(freq, key=freq.get)
        self.letters_guessed.add(maximum)

        return maximum

    def take_guess(self):
        letter = self.find_letter_to_guess()
        if not letter:
            return
        positions = self.game.guess_letter(letter)
        self.optimise_sol_space(letter, positions)


    def optimise_sol_space(self, letter: str, positions: list):
        if not positions:
            self.filtered_words = [word for word in self.filtered_words if letter not in word]
        else:
            self.filtered_words = [
                word for word in self.filtered_words
                if all(word[pos] == letter for pos in positions)
            ]



if __name__ == "__main__":
    successes = 0
    trials = 0
    total_words = len(WORD_LIST)
    start = time.time()

    iterator = tqdm(enumerate(WORD_LIST), total=total_words) if use_tqdm else enumerate(WORD_LIST)
    

    for i, word in iterator:
        if i % 500 != 0:
            continue
        trials += 1
        sol = AlgorithmicSolution(force_word=word)
        while sol.see_progress() == "processing":
            sol.take_guess()

        if sol.see_progress() == "win":
            successes += 1

        if not use_tqdm and i % 1000 == 0:
            print(f"Checked {i}/{total_words} | Success rate: {100 * successes / trials:.2f}%")

    print("\n✅ DONE")
    print(f"Total Words Tested: {trials}")
    print(f"Successes: {successes}")
    print(f"Success Rate: {100 * successes / trials:.2f}%")
    print(f"Time taken: {time.time() - start:.2f} seconds")


