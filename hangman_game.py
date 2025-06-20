import random as r

class Hangman:
    def __init__(self,force_word = None) -> None:
        self._word = ""
        self._generate_word(force_word)
        self.points = 10
        self.display_word = ['_' for i in range(self.get_length())]
        self.progress = "processing"

    
    def _generate_word(self, force_word = None) -> None:
        """
        Selects and assigns a random word from 'text_files/words.txt' to self.word.
        force_word should only ever be used in testing

        Reads the file line by line, chooses a word at random, and stores it in lowercase.
        Assumes the file exists and contains one word per line.
        """
        if force_word:
            self._word = force_word
        else:    
            with open('text_files/words.txt', 'r') as f:
                self._word = r.choice(f.read().splitlines()).lower()

    def get_length(self) -> int:
        """
        Returns the number of characters in the current word.

        This method provides the length of the word to be guessed in the Hangman game.
        Knowing the word length is permitted as part of standard Hangman gameplay.

        Returns:
            int: The length of the word.

        Example:
            >>> game.word = "python"
            >>> game.get_length()
            6
        """
        '''
        Returns the length of the word. This is allowed to be used
        by a solution, since you are allowed to know the length of the 
        word in Hangman.
        '''
        return len(self._word)
    
    def _get_word(self) -> str:
        """
        Returns the current word to be guessed in the Hangman game.
        Cannot be called by a solution, this is a private method.

        Returns:
            str: The word selected for the current game session.
        """
        return self._word
    
    def get_status(self) -> bool:
        """
        Checks if the word has been correctly guessed.
        Returns:
            bool: True if the word has been found, False otherwise.
        """
        return self.progress
    
    def get_display_word(self) -> str:
        """
        Public method to return the display word.
        Returns:
            str: the display word
        """
        return ' '.join(self.display_word)

    def guess_letter(self,letter:str) -> list:
        """
        Processes a guessed letter for the current Hangman game state.
        Args:
            letter (str): The letter being guessed. Must be a single character.
        Returns:
            list: the positions (if any) of guessed letters
        Raises:
            ValueError: If the input is not a single character or if no points remain after an incorrect guess.
        Side Effects:
            - Updates the player's points and the display word.
            - Prints feedback about the guess and game state.
            - Sets `self.word_found` to True if the word is fully guessed.
        """

        positions = []
    
        if len(letter) != 1:
            raise ValueError("letter has to be one character!")
        
        letter = letter.lower()

        if letter not in self._word:
            self.points -= 1
            print(f"you just lost a point! {letter} wasn't in the word. Points = {self.points}")
            if self.points <= 0:
                self.progress = "fail"
            print(self.get_display_word())    

        else:
            positions = [i for i in range(0, len(self._word)) if self._word[i] == letter]
            for i in positions:
                self.display_word[i] = letter
            print(f"correct guess, {letter} is the in the indices {positions} of the letter")

            print(self.get_display_word())
            if ''.join(self.display_word) == self._word:
                self.progress = "win"
                print("word found, congrats!")
        return positions




    

if __name__ == "__main__":
    with open('text_files/words.txt', 'r') as f:
        words = [line.strip().lower() for line in f]

    with open('text_files/words.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')

