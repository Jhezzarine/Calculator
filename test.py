import unittest
from calclogic import press

class TestCalc(unittest.TestCase):

    def test_press(self):
        res = '1+2+3'
        self.assertIs(res, '1+2+3')

    def test_equal(self):
        values = '1+2+3+4'
        total = str(eval(values))
        self.assertEqual(total, '10')

    def test_clear(self):
        values = '10/5+2'
        values = ''
        self.assertIs(values, '')

    def test_ce(self):
        values = '19876'

        new = len(values)
        delete = values[:new-1]
        equation = delete
        values = delete
        self.assertEqual(equation, '1987')

if __name__ == '__main__':
    unittest.main()