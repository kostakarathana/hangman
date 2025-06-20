from hangman_game import Hangman
from collections import defaultdict
import os

class AlgorithmicSolution:
    def __init__(self, force_word = None):
        self.game = Hangman(force_word)
        self.word_length = self.game.get_length()
        self.letters_guessed = []
        self.get_length_based_words_file()
    
    def see_progress(self):
        return self.game.get_status()
    
    def get_length_based_words_file(self):
        words_file = "text_files/brute_force_words.txt"
        if os.path.exists(words_file):
            os.remove(words_file)
        if not os.path.exists(words_file):
            with open("text_files/words.txt", "r") as src, open(words_file, "w") as dst:
                for line in src:
                    if len(line.strip()) == self.word_length:
                        dst.write(line)
        return words_file
    
    def find_letter_to_guess(self):
        freq = defaultdict(int)
        with open("text_files/brute_force_words.txt","r") as f:
            for line in f:
                for char in line.strip():
                    if char not in self.letters_guessed:
                        freq[char] += 1
        maximum = max(freq,key=freq.get)
        self.letters_guessed.append(maximum)
        return maximum

    def take_guess(self):
        letter = self.find_letter_to_guess()
        filter = self.game.guess_letter(letter)
        self.optimise_sol_space(letter, filter)
    
    def optimise_sol_space(self, letter:str, filter:list):
        words_file = "text_files/brute_force_words_temp.txt"

        with open("text_files/brute_force_words.txt", "r") as src, open(words_file, "w") as dst:
            for line in src:
                if filter == []:
                    if letter not in line.strip():
                            dst.write(line)
                else:
                    for val in filter:
                        if line.strip()[val] == letter:
                                dst.write(line)
        
        os.remove("text_files/brute_force_words.txt")
        os.rename(words_file, "text_files/brute_force_words.txt")



    

if __name__ == "__main__":
    successes = 0
    trials = 0
    success_rate = 0

    with open("text_files/words.txt","r") as f:
        for line in f:
            print(f"CURRENT WORD: {line.strip()} ")
            trials += 1
            sol = AlgorithmicSolution(line.strip())

            while sol.see_progress() == "processing":
                sol.take_guess()
                sol.see_progress()
                
            if sol.see_progress() == "win":
                successes += 1
            success_rate = successes/trials
            print(f"SUCCESS: {success_rate} ")
        
        
    
        
    





    



    