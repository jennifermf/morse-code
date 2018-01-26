#!/usr/bin/env python
# # -*- coding: utf-8 -*-
# Morse code tranlsator: because someone sent me a message in Morse code, and writing a script seemed like a good idea at the time. -jmf.
# version 0.2: EXTREME LIST COMPREHENSION EDITION!

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
    return '\n'.join([' '.join([morseCode.get(c) for c in word if c.isalnum()]) for word in secretMsg.lower().split(' ')])

def morseChars(c): # returns Morse letter
    return list({ k:v for k,v in morseCode.items() if v == c }.keys())[0]

# morse-to-alphanum conversion
# requires one space between Morse glyphs, two spaces between letters, and \n between words.
def morseInput(secretMsg):
    translatedWords = []
    morseWordList = secretMsg.split('\n')
    for word in morseWordList:
        translatedChars = [morseChars(c) for c in word.split(' ')]
        translatedWords.append(''.join(translatedChars))
    return ' '.join(translatedWords)

secretMsg = "... --- -- . --- -. .\n-.- -. --- .-- ...\n-- --- .-. ... .\n-.-. --- -.. ."

if ((secretMsg[0] in '.-') or (secretMsg[0:3] == 'dot') or (secretMsg[0:4] == 'dash')):
    translated = morseInput(secretMsg)
else:
    translated = alphaInput(secretMsg)
print(translated)
