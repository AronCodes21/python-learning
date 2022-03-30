import unittest

import helloWorld


class testName(unittest.TestCase):
  def test_adam(self):
    result = helloWorld.helloName("Adam")
  def test_eve(self):
    result = helloWorld.helloName("Eve")
  def test_Joan(self):
    result = helloWorld.helloName("Joan")
