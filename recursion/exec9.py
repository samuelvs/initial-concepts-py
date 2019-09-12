def mdc(a, b):
  if b == 0:
    return a
  else:
    r = a % b
    a = b
    b = r
    return mdc(a,b)

print(mdc(6,12))