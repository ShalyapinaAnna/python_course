import unittest


def nmbrs1(a, b):
    c = a + b
    return c


def lists1(a, b):
    c = a + b
    return c


def nmbrs2(a):
    b = a//2
    return b


def lists2(a):
    b = a[::-1]
    return b


class TestTask51(unittest.TestCase):
    def test_nmbrs1(self):
        self.assertTrue(nmbrs1(10, 5) != 12)
        self.assertFalse(nmbrs1(10, 5) == 12)
        return

    def test_lists1(self):
        self.assertIn('a', lists1('aaa', 'b'))
        self.assertNotIn('c', lists1('aaa', 'b'))
        return

    def test_nmbrs2(self):
        self.assertGreater(10, nmbrs2(10))
        self.assertLess(nmbrs2(10), 10)
        return

    def test_lists2(self):
        self.assertCountEqual(lists2('word'), 'word')
        return


if __name__ == '__main__':
    unittest.main()
