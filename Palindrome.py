import unittest

# Detector de Palindromo Común
def palindrome (Word):
    descendiente = len(Word) - 1
    ascendiente = 0
    palindromo = True
    for letra in Word:
       if Word[ascendiente].lower() != Word[descendiente].lower():
           palindromo = False 
       descendiente -= 1
       ascendiente += 1
       return palindromo 

# Detector de Palindromo recursivo
def palindrome_r (word):
    word = word.replace(' ','').lower()
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        return palindrome_r (word[1:-1])
    else:
        return False

if __name__ == '__main__':
    unittest.main()