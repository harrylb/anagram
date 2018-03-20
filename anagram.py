#!/usr/bin/env python3

def areAnagrams(word1,word2): #Takes strings created in create_anagrams()
    list_word1 = list(word1)
    list_word1.sort() #Sorts first word
    list_word2 = list(word2)
    list_word2.sort() #Sorts second words
    if list_word1 == list_word2: #Sends boolean back to anagram_runner
        return True
    else:
        return False
