import numpy as np

words: list[str] = ["cat", "car", "cap"]
char_array: np.ndarray = np.array([list(word) for word in words])


if __name__ == "__main__":
    print(char_array)