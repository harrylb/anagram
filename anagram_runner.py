#!/usr/bin/env python3
"""
anagram_runner.py

This program uses a module "anagram.py" with a boolean function

    areAnagrams(word1, word2)

and times how long it takes that function to correctly identify
two words as anagrams.

A series of tests with increasingly long anagrams are performed,
with the word length and time to identify output to a file in the
same directory, anagram_results.csv, for easy import into a spreadsheet
or graphing program.

@author Richard White
@version 2017-02-20
"""

import random
import time
import anagram

def create_anagrams(word_length):
    """
    Creates a random collection of lowercase English letters, a-z, of a
    specified word_length, as well as a randomized rearranging of those
    same letters. The strings word1 and word2 are anagrams of each other,
    and returned by this function.
    """
    baseword = []
    for i in range(word_length):
        baseword.append(chr(int(random.random()*26) + 97)) # random letter
    word1 = ''.join(baseword)                     # Convert list to string
    # Now go through baseword and pop off random letters to create word2.
    word2 = ""
    while len(baseword) > 0:
        word2 += baseword.pop(int(random.random() * len(baseword)))
    return word1, word2


def main():
    """
    This main program includes some timed pauses and timed countdowns to
    give the user some sense of the time it takes to sort the words.
    """

    MAX_WORD_LENGTH = 10000
    print("ANAGRAM RUNNER")
    results = []
    for word_length in range(int(MAX_WORD_LENGTH/10), MAX_WORD_LENGTH, int(MAX_WORD_LENGTH/10)):
        word1,word2 = create_anagrams(word_length)
        print("Comparing",word1,"and",word2)
        print("Starting test")
        start = time.time()
        result = anagram.areAnagrams(word1,word2)
        stop = time.time()
        print("Stopping test")
        if result:
            print("The two words are anagrams")
        else:
            print("The two words are not anagrams")
        print("Time elapsed: {0:.4f} seconds".format(stop - start))
        results.append((word_length, stop-start))

    outfile = open("anagram_results.csv","w")
    outfile.write("Anagram length in letters,time to verify(seconds)\n")
    for result in results:
        outfile.write(str(result[0]) + "," + str(result[1]) + "\n")
    outfile.close()
    print("anagram_results.csv successfully written")

if __name__ == "__main__":
    main()
