from tkinter import E
import unittest
from Config import *

class ShortsToBinaryAndBack(unittest.TestCase):
    
    def test_ushort_to_binary(self):
        self.assertEqual(1, TODO)
        self.assertEqual(16, TODO)

        if not IN_A_HURRY:
            self.assertEqual(24, TODO)
            self.assertEqual(65535, TODO)
            self.assertEqual(65536, TODO)

    def test_binary_to_ushort(self):
        self.assertEqual(0b0000000000000101, TODO) # 0000 0000 0000 0101
        self.assertEqual(0b0000000000001011, TODO) # 0000 0000 0000 1011

        if not IN_A_HURRY:
            self.assertEqual(0b0000000010101111, TODO) # 0000 0000 1010 1011
            self.assertEqual(0b0000000011011110, TODO) # 0000 0000 1101 1110

    def test_short_to_binary(self):
        self.assertEqual(1, TODO)
        self.assertEqual(-1, TODO)
        self.assertEqual(16, TODO)
        self.assertEqual(-16, TODO)

        if not IN_A_HURRY:
            self.assertEqual(24, TODO)
            self.assertEqual(32767, TODO)
            self.assertEqual(32768, TODO)
            self.assertEqual(-24, TODO)
            self.assertEqual(-32767, TODO)
            self.assertEqual(-32768, TODO)

    def test_binary_to_short(self):
        self.assertEqual(0b0000000000000101, TODO) # 0000 0000 0000 0101
        self.assertEqual(0b0000000000001011, TODO) # 0000 0000 0000 1011
        self.assertEqual(0b1000000000001101, TODO) # 1000 0000 0000 1101
        self.assertEqual(0b1000000000001110, TODO) # 1000 0000 0000 1110

        if not IN_A_HURRY:
            self.assertEqual(0b0000000010101111, TODO) # 0000 0000 1010 1011
            self.assertEqual(0b0000000011011110, TODO) # 0000 0000 1101 1110
            self.assertEqual(0b1000000011011111, TODO) # 1000 0000 1101 1111
            self.assertEqual(0b1000000011101110, TODO) # 1000 0000 1101 1110

