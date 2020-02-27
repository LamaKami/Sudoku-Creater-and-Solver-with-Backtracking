import unittest
from sudoku import Sudoku


class TestStringMethods(unittest.TestCase):

    def test_colums_not_correct(self):
        test = Sudoku()
        test.set_value(0, 5, 2)
        test.set_value(8, 5, 2)
        self.assertFalse(test.check_colums())

    def test_row_not_correct(self):
        test = Sudoku()
        test.set_value(6, 7, 2)
        test.set_value(6, 5, 2)
        self.assertFalse(test.check_rows())

    def test_specific_square_not_correct(self):
        test = Sudoku()
        x = 1 // 3
        y = 5 // 3
        for i in range(x * 3, x * 3 + 3):
            for k in range(y * 3, y * 3 + 3):
                test.set_value(k, i, 3)
        self.assertFalse(test.check_specific_square(5, 1))

    def test_all_square_not_correct(self):
        test = Sudoku()
        for l in range(9):
            for m in range(9):
                counter = 1
                x = l // 3
                y = m // 3
                for i in range(x * 3, x * 3 + 3):
                    for k in range(y * 3, y * 3 + 3):
                        test.set_value(k, i, counter)
                        counter += 1
        test.set_value(5, 6, 2)
        self.assertFalse(test.check_all_squares())

    def test_colums_correct(self):
        test = Sudoku()
        for i in range(9):
            test.set_value(i - 1, i, 2)
        self.assertTrue(test.check_colums())

    def test_row_correct(self):
        test = Sudoku()
        for i in range(9):
            test.set_value(i, i - 1, 2)
        self.assertTrue(test.check_rows())

    def test_specific_square_correct(self):
        test = Sudoku()
        x, y = 4, 6
        counter = 1
        x = x // 3
        y = y // 3
        for i in range(x * 3, x * 3 + 3):
            for k in range(y * 3, y * 3 + 3):
                test.set_value(k, i, counter)
                counter += 1
        self.assertTrue(test.check_specific_square(5, 5))

    def test_all_square_correct(self):
        test = Sudoku()
        test.backtracking(test.field)
        self.assertTrue(test.check_all_squares())


if __name__ == '__main__':
    unittest.main()
