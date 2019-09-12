def invert(word):
  if len(word) == 1:
    return word
  else:
    return invert(word[1:]) + word[0]

print(invert('Python'))