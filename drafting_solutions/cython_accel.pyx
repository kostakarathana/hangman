# cython: boundscheck=False, wraparound=False
from libc.string cimport strchr
from collections import defaultdict
from cpython cimport array
import cython

@cython.boundscheck(False)
@cython.wraparound(False)
def compute_frequencies(list words, set guessed_letters):
    cdef dict freq = {}
    cdef str word
    cdef str char
    for word in words:
        for char in word:
            if char not in guessed_letters:
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
    return freq


@cython.boundscheck(False)
@cython.wraparound(False)
def filter_words(list words, str letter, list positions):
    cdef list filtered = []
    cdef str word
    cdef int match, i, pos
    cdef char_ltr = letter[0]

    if not positions:
        for word in words:
            if char_ltr not in word:
                filtered.append(word)
    else:
        for word in words:
            match = 1
            for pos in positions:
                if word[pos] != char_ltr:
                    match = 0
                    break
            if match:
                filtered.append(word)
    return filtered