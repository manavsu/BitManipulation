import unittest
from Config import *

class HexadecimalBitwiseOperations(unittest.TestCase):
    '''
    Hexadecimal to binary conversion:
    0x0 = 0000
    0x1 = 0001
    0x2 = 0010
    0x3 = 0011
    0x4 = 0100
    0x5 = 0101
    0x6 = 0110
    0x7 = 0111
    0x8 = 1000
    0x9 = 1001
    0xA = 1010
    0xB = 1011
    0xC = 1100
    0xD = 1101
    0xE = 1110
    0xF = 1111
    '''

    def test_bitwise_or(self):
        self.assertEqual(0x1 | 0x0, TODO)
        self.assertEqual(0x1A | 0x1B, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0x3791 | 0x3BF2, TODO)

    def test_bitwise_and(self):
        self.assertEqual(0x1 & 0x0, TODO)
        self.assertEqual(0x10 & 0x9B, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0x3391 & 0x3BFA, TODO)

    def test_bitwise_xor(self):
        self.assertEqual(0x1 ^ 0x0, TODO)
        self.assertEqual(0x1A ^ 0x1B, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0x3791 ^ 0x3BF2, TODO)

    def test_bitwise_left_shift(self):
        self.assertEqual(0x1 << 1, TODO)
        self.assertEqual(0x1C << 3, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0x3791 << 10, TODO)

    def test_bitwise_right_shift(self):
        self.assertEqual(0x1 >> 1, TODO)
        self.assertEqual(0x1C >> 3, TODO)

        if not IN_A_HURRY:
            self.assertEqual(0x3791 >> 10, TODO)