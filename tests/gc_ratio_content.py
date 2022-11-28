import unittest
import gc_content

class RatioTest(unittest.TestCase):

    def test_gc_ratio(self):
        self.assertEqual(gc_content.gc_ratio("GTTGTAATGGCCTACATTA"), 0.3684210526315789*100)
        self.assertEqual(gc_content.gc_ratio("GCUAACUAAC"), 0.4*100)

if __name__ == "__main__":
    unittest.main()