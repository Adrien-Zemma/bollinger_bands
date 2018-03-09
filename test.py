import random
import unittest

import os.path
import sys

from calc import readfile

class UnitTests(unittest.TestCase):
	def test_not_exist_file(self):
		self.assertFalse(os.path.isfile("some file"))

	def test_exist_file(self):
		self.assertTrue(os.path.isfile("files/bollinger_test.txt"))

	def test_wrong_file(self):
		self.assertIsNone(readfile("some file", 0, 10))

	def test_wrong_index(self):
		self.assertIsNone(readfile("files/bollinger_test.txt", -1, 10))
	
	def test_to_much_index(self):
		self.assertIsNone(readfile("files/bollinger_test.txt", 5000, 10))

	def test_wrong_period(self):
		self.assertIsNone(readfile("files/bollinger_test.txt", 0, -1))
	
	def test_to_much_period(self):
		self.assertIsNone(readfile("files/bollinger_test.txt", 0, 5000))

	def test_right_index(self):
		self.assertIsNotNone(readfile("files/bollinger_bitcoin_dec2017.txt", 32, 32))
	
	def test_right_period(self):
		self.assertIsNotNone(readfile("files/bollinger_bitcoin_dec2017.txt", 20, 5))