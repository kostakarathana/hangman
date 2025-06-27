from hangman_game import Hangman
from collections import defaultdict
import time





from tqdm import tqdm


# Global: Read the word list once
with open('text_files/words.txt', 'r') as f:
    WORD_LIST = [line.strip().lower() for line in f if line.strip()]

WORDS_BY_LENGTH: defaultdict[list[str], int] = defaultdict(list)
for i in range(1,46):
    WORDS_BY_LENGTH[f"{i}"] = [word for word in WORD_LIST if len(word) == i]



class AlgorithmicSolution:
    def __init__(self, force_word: str|None = None):
        self.game: Hangman = Hangman(force_word)
        self.word_length: int = self.game.get_length()
        self.letters_guessed: set[str] = set()
        self.filtered_words: list[str] = WORDS_BY_LENGTH[f"{self.word_length}"]
        self.words_seen: set[str] = set()

    def _cheat_and_see_word(self): # NEVER to be used except in testing!
        return self.game._get_word()
    
    def see_progress(self): 
        return self.game.get_status()

    def find_letter_to_guess(self) -> str | None: # Huge bottleneck #1 (use counter maybe, need caching of some kind)

        freq: defaultdict[str,int] = defaultdict(int)
        for word in self.filtered_words:
            for char in word:
                if char not in self.letters_guessed:
                    freq[char] += 1
        if not freq:
            return None  
        

        maximum: str = max(freq, key=freq.get)
        self.letters_guessed.add(maximum)
        return maximum

    def take_guess(self):
        letter = self.find_letter_to_guess()
        if not letter:
            return


        positions = self.game.guess_letter(letter) # 0% of runtime time

        
        self.optimise_sol_space(letter, positions)
   


    def optimise_sol_space(self, letter: str, positions: list[int]): # Huge bottleneck #2

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

    iterator = tqdm(enumerate(WORD_LIST), total=total_words)
    

    for i, word in iterator:
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
