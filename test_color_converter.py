import unittest
from color_converter import rgb_to_hex

class TestColorConverter(unittest.TestCase):
    def test_white(self):
        self.assertEqual(rgb_to_hex(255, 255, 255), "#ffffff")

    def test_black(self):
        #added three 0s to ensure leading zeros are included
        self.assertEqual(rgb_to_hex(0, 0, 0), "#000000") 

if __name__ == '__main__':
    unittest.main()
