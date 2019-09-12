def decresc(n):
  if n < 0:
    return 0
  else:
    print(n)
    decresc(n-1)

decresc(10)