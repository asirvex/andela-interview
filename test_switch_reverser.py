import unittest
import switch_reverser as sr

class TestSwitchReverser(unittest.TestCase):
    def test_reverse_int_list(self):
        self.assertEqual(sr.reverse_int_list([15, 82, 10, 4]), [4, 10, 82, 15] )
        self.assertEqual(sr.reverse_int_list([75]), [75])
        self.assertEqual(sr.reverse_int_list([-15, -8, 7, 0]), [0, 7, -8, -15])

    def test_upper_str_list(self):
        self.assertEqual(sr.upper_str_list(["smallword", "CAPITALSWORD", "MixedWord"]), ["SMALLWORD", "CAPITALSWORD", "MIXEDWORD"])
        self.assertEqual(sr.upper_str_list(["small word", "CAPITALS WORD", "Mixed Word"]), ["SMALL WORD", "CAPITALS WORD", "MIXED WORD"])

    def test_switch_reverse(self):
        self.assertEqual(sr.switch_reverse(["smallword", "CAPITALSWORD", "MixedWord"]), ["SMALLWORD", "CAPITALSWORD", "MIXEDWORD"])
        self.assertEqual(sr.switch_reverse([15, 82, 10, 4]), [4, 10, 82, 15] )
        self.assertEqual(sr.switch_reverse(["small word", "CAPITALS WORD", "Mixed Word"]), ["SMALL WORD", "CAPITALS WORD", "MIXED WORD"])
        self.assertEqual(sr.switch_reverse([75]), [75])
        self.assertEqual(sr.switch_reverse(["smallword", "CAPITALSWORD", "MixedWord", 15, 82, 10, 4]), ["smallword", "CAPITALSWORD", "MixedWord", 15, 82, 10, 4] ) 


if __name__ == "__main__":
    unittest.main()