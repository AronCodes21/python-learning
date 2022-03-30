import unittest

import helloWorld


class testName(unittest.TestCase):

  def test_adam(self):
    print("Name set to: Adam")
    result = helloWorld.helloName("Adam")

  def test_eve(self):
    print("Name set to: Eve")
    result = helloWorld.helloName("Eve")

  def test_Joan(self):
    print("Name set to: Joan")
    result = helloWorld.helloName("Joan")

  def test_Number(self):
    print("Name set to: 15")
    result = helloWorld.helloName(15)

  def test_Float(self):
    print("Name set to: 10.3")
    result = helloWorld.helloName(10.3)


if __name__ == '__main__':
  unittest.main()
