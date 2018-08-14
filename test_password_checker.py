import unittest
import password_checker as pc

class TestPasswordChecker(unittest.TestCase):
    def test_min_length(self):
        self.assertTrue(pc.min_length("ABd1234@1"))
        self.assertFalse(pc.min_length("a F1#"))
        self.assertTrue(pc.min_length("lkSb2k"))
        self.assertTrue(pc.min_length("sd2woMkdi##jf"))

    def test_max_length(self):
        self.assertTrue(pc.max_length("ABd1234@1"))
        self.assertTrue(pc.max_length("e1jkvQpetid3"))
        self.assertFalse(pc.max_length("sd2woMkdi##jf"))

    def test_has_lower(self):
        self.assertTrue(pc.has_lower("ABd1234@1"))
        self.assertTrue(pc.has_lower("a F1#"))
        self.assertTrue(pc.has_lower("2We3345"))
        self.assertFalse(pc.has_lower("1243434"))
        self.assertFalse(pc.has_lower("SEU#IR1"))

    def test_has_upper(self):
        self.assertTrue(pc.has_upper("ABd1234@1"))
        self.assertFalse(pc.has_upper("aud1#"))
        self.assertTrue(pc.has_upper("2We3345"))
        self.assertFalse(pc.has_upper("1243434"))
        self.assertTrue(pc.has_upper("SEU#IR1"))

    def test_has_digit(self):
        self.assertTrue(pc.has_digit("ABd1234@1"))
        self.assertFalse(pc.has_digit("aud#"))
        self.assertTrue(pc.has_digit("2We3345"))
        self.assertTrue(pc.has_digit("1243434"))
        self.assertFalse(pc.has_digit("SEU#IR"))

    def test_has_char(self):
        self.assertTrue(pc.has_char("ABd1234@1"))
        self.assertTrue(pc.has_char("aud#"))
        self.assertFalse(pc.has_char("2We3345"))
        self.assertFalse(pc.has_char("1243434"))
        self.assertTrue(pc.has_char("SEU#IR"))

        
if __name__ == "__main__":
    unittest.main()
