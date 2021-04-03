import unittest
import random

nmbrs = []
for i in range(10):
    nmbrs.append(random.random())

for nmb in nmbrs:
    class TestTask52(unittest.TestCase):
        def test_task(self):
            self.assertGreaterEqual(nmb, 0.5)
            return


if __name__ == '__main__':
    unittest.main()
