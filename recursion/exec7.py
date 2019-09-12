def double_fat(n):
  if n < 1:
    return 1
  else:
    return n * double_fat(n-2)

print(double_fat(11))