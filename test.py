import unittest, morse

# Morse translator: http://www.unit-conversion.info/texttools/morse-code/

class MorseTest(unittest.TestCase):
    def test_alpha_to_morse(self):
        self.assertEqual(morse.alphaInput('A'), '.-')
        self.assertEqual(morse.alphaInput('SOS'), '... --- ...')
        self.assertEqual(morse.alphaInput('this is a test'), '- .... .. ...\n.. ...\n.-\n- . ... -')
        self.assertEqual(morse.alphaInput('Cats are awesome'), '-.-. .- - ...\n.- .-. .\n.- .-- . ... --- -- .')
        self.assertEqual(morse.alphaInput('Hello, World!'), '.... . .-.. .-.. ---\n.-- --- .-. .-.. -..')

    def test_morse_to_alpha(self):
        self.assertEqual(morse.morseInput('... --- ...'), 'sos')
        self.assertEqual(morse.morseInput('- .... .. ...\n.. ...\n.-\n- . ... -'), 'this\nis\na\ntest')
        self.assertEqual(morse.morseInput('-.-. .- - ...\n.- .-. .\n.- .-- . ... --- -- .'), 'cats\nare\nawesome')
        self.assertEqual(morse.morseInput('.... . .-.. .-.. ---\n.-- --- .-. .-.. -..'), 'hello\nworld')
