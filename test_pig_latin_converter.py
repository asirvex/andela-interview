import unittest
import pig_latin_converter as pic


class TestPigLatinConverter(unittest.TestCase):
    def test_vowel_position(self):
        self.assertEqual(pic.vowel_position("apple"), 0)
        self.assertEqual(pic.vowel_position("will"), 1)
        self.assertEqual(pic.vowel_position("chatter"), 2)
        self.assertEqual(pic.vowel_position("gpd"), "no_vowel")

    def test_add_suffix(self):
        self.assertEqual(pic.add_suffix("apple"), "appleway")
        self.assertEqual(pic.add_suffix("will"), "illway")
        self.assertEqual(pic.add_suffix("chatter"), "atterchay")
        self.assertEqual(pic.add_suffix("dog"), "ogday")
        self.assertEqual(pic.add_suffix("andela"), "andelaway")
        self.assertEqual(pic.add_suffix("trash"), "ashtray")


if __name__ == "__main__":
    unittest.main()