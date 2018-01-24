#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# Morse code tranlsator: because someone sent me a message in Morse code, and writing a script seemed like a good idea at the time. -jmf.

# cypher
morseCode = { "a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".",
            "f" : "..-.", "g" : "--.", "h" : "....", "i": "..", "j" : ".---",
            "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---",
            "p" : ".--.", "q" : "--.-", "r" : ".-.", "s" : "..." , "t" : "-",
            "u" : "..-", "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--",
            "z" : "--..", "one" : ".----", "two" : "..---", "three" : "...--",
            "four" : "....-", "five" : ".....", "six" : "-....", "seven" : "--...",
            "eight" : "---..", "nine" : "----.", "zero" : "-----", " " : " " }

# alphanum-to-morse conversion
# returns one word per line
def alphaInput(secretMsg):
    translatedWords = []
    words = secretMsg.lower().split(' ')
    for word in words:
        tempChars = []
        for c in word:
            if c.isalnum():
                m = morseCode.get(c)
                tempChars.append(m)
        tempWord = ' '.join(tempChars)
        translatedWords.append(tempWord)
    return '\n'.join(translatedWords)

# morse-to-alphanum conversion
# requires one space between Morse glyphs, two spaces between letters, and \n between words.
# returns one word per line
def morseInput(secretMsg):
    translatedWords = []
    morseWordList = secretMsg.split('\n')
    # Look up Morse-word line by line; one row = one word
    for word in morseWordList:
        letters = word.split(' ') # splits each Morse-word-row into Morse-characters (letters)
        translatedLetters=[]
        for letter in letters:
            chardict = { k:v for k,v in morseCode.items() if v == letter }
            if chardict:
                char = list(chardict.keys())[0]
                translatedLetters.append(char)
        word = ''.join(translatedLetters)
        translatedWords.append(word)
    translatedMsg = '\n'.join(translatedWords)
    return translatedMsg

secretMsg = "... --- -- . --- -. .\n-.- -. --- .-- ...\n-- --- .-. ... .\n-.-. --- -.. ."

if ((secretMsg[0] in '.-') or (secretMsg[0:3] == 'dot') or (secretMsg[0:4] == 'dash')):
    translated = morseInput(secretMsg)
else:
    translated = alphaInput(secretMsg)
print(translated)
