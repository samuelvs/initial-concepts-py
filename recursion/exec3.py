def countLetter(word, letter):
  result = 0
  if len(word) == 0:
    return result
  else:
    if word[0] == letter:
      result = 1  
    return result + countLetter(word[1:], letter)

print(countLetter('bgca', 'a'))