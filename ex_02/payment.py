
from ctypes.wintypes import CHAR


def payment(hours, rate):
  if(hours < 0 or rate < 0):
    print("Can't calculate negative")
    return
  pay = float(hours) * float(rate)
  print('Pay:', "$",pay)

