import unittest
from Config import *

class BinaryBitwiseOperations(unittest.TestCase):

    def test_bitwise_or(self):
        self.assertEqual(0b0 | 0b0, TODO)
        self.assertEqual(0b1 | 0b0, TODO)
        self.assertEqual(0b0 | 0b1, TODO)
        self.assertEqual(0b1 | 0b1, TODO)
        
        if not IN_A_HURRY:
            self.assertEqual(0b0010 | 0b0101, TODO)
            self.assertEqual(0b0101 | 0b0010, TODO)

    def test_bitwise_and(self):
        self.assertEqual(0b0 & 0b0, TODO)
        self.assertEqual(0b1 & 0b0, TODO)
        self.assertEqual(0b0 & 0b1, TODO)
        self.assertEqual(0b1 & 0b1, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0b0010 & 0b0101, TODO)
            self.assertEqual(0b0101 & 0b0010, TODO)

    def test_bitwise_xor(self):
        self.assertEqual(0b0 ^ 0b0, TODO)
        self.assertEqual(0b1 ^ 0b0, TODO)
        self.assertEqual(0b0 ^ 0b1, TODO)
        self.assertEqual(0b1 ^ 0b1, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0b0010 ^ 0b0101, TODO)
            self.assertEqual(0b0101 ^ 0b0010, TODO)

    def test_bitwise_left_shift(self):
        self.assertEqual(0b0 << 0, TODO)
        self.assertEqual(0b1 << 0, TODO)
        self.assertEqual(0b0 << 1, TODO)
        self.assertEqual(0b1 << 1, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0b0010 << 3, TODO)
            self.assertEqual(0b0101 << 2, TODO)

    def test_bitwise_right_shift(self):
        self.assertEqual(0b0 >> 0, TODO)
        self.assertEqual(0b1 >> 0, TODO)
        self.assertEqual(0b0 >> 1, TODO)
        self.assertEqual(0b1 >> 1, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0b0010 >> 3, TODO)
            self.assertEqual(0b0110 >> 2, TODO)