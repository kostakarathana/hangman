from hangman_game import Hangman, WORD_LIST
from collections import defaultdict
import time

class AlgorithmicSolution:
    def __init__(self, force_word=None):
        self.game = Hangman(force_word)
        self.word_length = self.game.get_length()
        self.letters_guessed = []
        self.filtered_words = [word for word in WORD_LIST if len(word) == self.word_length]

    

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
        self.letters_guessed.append(maximum)

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

    for i,word in enumerate(WORD_LIST):
    
        trials += 1
        sol = AlgorithmicSolution(force_word=word)

        while sol.see_progress() == "processing":
            sol.take_guess()

        if sol.see_progress() == "win":
            successes += 1
        success_rate = successes / trials

        print(f"SUCCESS RATE: {100*(success_rate):.1f}%")
        print(f"percentage complete approx:  {100*i/466550}%")


