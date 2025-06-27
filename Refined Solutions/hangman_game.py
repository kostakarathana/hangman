import random as r

# Global: Read the word list once
with open('text_files/words.txt', 'r') as f:
    WORD_LIST = [line.strip().lower() for line in f if line.strip()]

class Hangman:
    def __init__(self, force_word: str = "") -> None:
        self._word: str = ""
        self._generate_word(force_word) #type
        self.points: int = 7
        self.display_word = ['_' for _ in range(self.get_length())]
        self.progress = "processing"

    def _generate_word(self, force_word: str = "") -> None:
        if force_word != "":
            self._word = force_word.lower()
        else:
            self._word = r.choice(WORD_LIST)

    def get_length(self) -> int:
        return len(self._word)
    
    def _get_word(self) -> str:
        return self._word
    
    def get_status(self) -> str:
        return self.progress
    
    def get_display_word(self) -> str:
        return ' '.join(self.display_word)

    def guess_letter(self, letter: str) -> list[int]:
        positions = []
        if len(letter) != 1:
            raise ValueError("letter has to be one character!")
        letter = letter.lower()

        if letter not in self._word:
            self.points -= 1
            if self.points <= 0:
                self.progress = "fail"
        else:
            positions = [i for i, c in enumerate(self._word) if c == letter]
            for i in positions:
                self.display_word[i] = letter
            if ''.join(self.display_word) == self._word:
                self.progress = "win"
        return positions
    

if __name__ == "__main__":
    pass
