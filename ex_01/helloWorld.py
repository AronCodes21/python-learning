from ast import Num
from tokenize import Number


def helloName(name):
  if(type(name) != str):
    print("That's not a name")
  else:
    print("hello",name)
