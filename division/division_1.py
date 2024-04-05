# https://stackoverflow.com/questions/249372/how-to-calculate-recurring-digits

def divide(a, b):
  '''Returns the decimal representation of the fraction a / b in three parts:
  integer part, non-recurring fractional part, and recurring part.'''
  assert b > 0
  integer = a // b
  remainder = a % b
  seen = {remainder: 0}  # Holds position where each remainder was first seen.
  digits = []
  while(True):  # Loop executed at most b times (as remainders must be distinct)
    remainder *= 10
    digits.append(remainder // b)
    remainder = remainder % b
    if remainder in seen:  # Digits have begun to recur.
      where = seen[remainder]
      return (integer, digits[:where], digits[where:])
    else:
      seen[remainder] = len(digits)

# Some examples.
for a, b in [(5,4), (1,6), (17,7), (22,11), (100,17), (1,243)]:
  (i, f, r) = divide(a, b)
  print("%d/%d = %d.%s(%s)" % (a, b, i, ''.join(map(str, f)),''.join(map(str,r))))
