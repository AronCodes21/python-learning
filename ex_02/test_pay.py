import unittest

import payment


class testPayment(unittest.TestCase):
  def test_1(self):
    result = payment.payment(10, 20)

  def test_2(self):
    result = payment.payment(100, 202)

  def test_3(self):
    result = payment.payment(6.5, 25.4)

  def test_4(self):
    result = payment.payment(-10, -25)

if __name__ == "__main__":
  unittest.main()
