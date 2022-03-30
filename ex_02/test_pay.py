import unittest

import ex_03


class testPayment(unittest.TestCase):
  def test_1(self):
    result = ex_03.payment(10, 20)

  def test_2(self):
    result = ex_03.payment(100, 202)

  def test_3(self):
    result = ex_03.payment(6.5, 25.4)

  def test_4(self):
    result = ex_03.payment(-10, -25)

if __name__ == "__main__":
  unittest.main()
