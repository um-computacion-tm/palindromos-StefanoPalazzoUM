import unittest
from Palindrome import palindrome, palindrome_r

class TestPalindrome(unittest.TestCase):
    def test_palindrome_1(self):
        result = palindrome('neuquen')
        self.assertEqual(result, True)

    def test_palindrome_2(self):
        result = palindrome('Mendoza')
        self.assertEqual(result, False)

    def test_palindrome_3(self):
        result = palindrome('RadAr')
        self.assertEqual(result, True)

    def test_palindrome_4(self):
        result = palindrome('NoEsUnPalindromo')
        self.assertEqual(result, False)

    def test_palindrome_5(self):
        result = palindrome('Agita falsos usos la fatiga')
        self.assertEqual(result, True)



    def test_rpalindrome_1(self):
        result = palindrome_r('neuquen')
        self.assertEqual(result, True)

    def test_rpalindrome_2(self):
        result = palindrome_r('Mendoza')
        self.assertEqual(result, False)

    def test_rpalindrome_3(self):
        result = palindrome_r('RadAr')
        self.assertEqual(result, True)

    def test_rpalindrome_4(self):
        result = palindrome_r('NoEsUnPalindromo')
        self.assertEqual(result, False)

    def test_rpalindrome_5(self):
        result = palindrome_r('Agita falsos usos la fatiga')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()