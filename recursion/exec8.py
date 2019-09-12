def isPalindromo(word):
  if len(word) == 0:
    return True
  elif word[0] == word[len(word)-1]:
    aux = len(word) - 1
    return isPalindromo(word[1:aux])

print('Eh palindromo' if isPalindromo('asdf') else 'Nao eh palindromo')