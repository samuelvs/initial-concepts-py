def cresc(n):
  if n < 0:
    return 0
  else:
    print(cresc(n-1))
    return n+1

cresc(10)