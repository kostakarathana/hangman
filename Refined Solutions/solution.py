from hangman_game import Hangman
from collections import defaultdict
import numpy as np
import time



class HangmanSolver:
    def __init__(self) -> None:
        pass

    def setup(self) -> None:
        WORDS_BY_LENGTH: defaultdict[str,list[str]] = defaultdict(list[str])

        with open('text_files/words.txt', 'r') as f:
            WORD_LIST: np.ndarray = np.array([line.strip().lower() for line in f if line.strip()])
        for i in range(1,46):
            WORDS_BY_LENGTH[f"{i}"] = np.array([word for word in WORD_LIST if len(word) == i]) # type: ignore
    
    def solve(self) -> None:
        


