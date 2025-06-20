import random as r

class Hangman:
    def __init__(self, points=7) -> None:
        self._generate_word()
        self.points = points
        self.display_word = ['_' for i in range(self.get_length())]
        self.word_found = False

        
    def _generate_word(self) -> None:
        with open('text_files/words.txt', 'r') as f:
            self.word = r.choice(f.read().splitlines()).lower()

    def get_length(self) -> int:
        return len(self.word)
    
    def _get_word(self) -> str:
        return self.word
    
    def get_display_word(self) -> str:
        return ' '.join(self.display_word)

    def guess_letter(self,letter:str) -> str:
        
        if len(letter) != 1:
            raise ValueError("letter has to be one character!")
        
        letter = letter.lower()

        if letter not in self.word:
            self.points -= 1
            print(f"you just lost a point! {letter} wasn't in the word. Points = {self.points}")
            if self.points <= 0:
                raise ValueError("no points left, you lose!")
            
            print(self.get_display_word())    

        else:
            positions = [i for i in range(0, len(self.word)) if self.word[i] == letter]
            for i in positions:
                self.display_word[i] = letter
            print(f"correct guess, {letter} is the in the indices {positions} of the letter")

            print(self.get_display_word())
            if ' '.join(self.display_word) == self.word:
                self.word_found = True
                print("word found, congrats!")
        return self.get_display_word()




    

if __name__ == "__main__":
    hangman = Hangman(7)
    hangman.guess_letter("a")
    hangman.guess_letter("e")
    

