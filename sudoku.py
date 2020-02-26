import numpy as np
import random
import pdb


class Sudoku:
    def __init__(self):
        self.feld = np.zeros(shape=(9, 9), dtype=int)
        self.check_list = []
        self.elements_to_fill = []

    def set_value(self, x, y, value=0):
        self.feld[x][y] = value

    def check_rows(self):
        for row in self.feld:
            self.check_list = [x for x in row]
            if self.check_duplicates():
                self.check_list.clear()
                return False
            self.check_list.clear()
        return True

    def check_colums(self):
        for i in range(0, len(self.feld)):
            self.check_list = [x[i] for x in self.feld]
            if self.check_duplicates():
                self.check_list.clear()
                return False
            self.check_list.clear()
        return True

    def check_all_squares(self):
        for square_colum in range(0, 3):
            for square_row in range(0, 3):
                self.check_list.clear()
                for i in range(0, 3):
                    for k in range(0, 3):
                        self.check_list.append(
                            self.feld[i + (square_colum * 3)][k + (square_row * 3)])
                if self.check_duplicates():
                    self.check_list.clear()
                    return False
        self.check_list.clear()
        return True

    def check_specific_square(self, x, y):
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for k in range(y // 3 * 3, y // 3 * 3 + 3):
                self.check_list.append(self.feld[i][k])
        if self.check_duplicates():
            self.check_list.clear()
            return False
        self.check_list.clear()

        return True

    def check_duplicates(self):
        self.check_list = [x for x in self.check_list if x != 0]
        if len(self.check_list) == 0:
            return False
        elif len(self.check_list) == len(set(self.check_list)):
            return False
        else:
            return True

    def backtracking(self, feld):
        values = list(range(1, len(feld) + 1))
        for x in range(len(feld)):
            for y in range(len(feld)):
                if 0 == feld[x][y]:
                    while len(values) != 0:
                        wert = random.choice(values)
                        feld[x][y] = wert
                        if not self.check_colums() or not self.check_rows() or not self.check_specific_square(x, y):
                            feld[x][y] = 0
                            values.remove(wert)
                        else:
                            if not self.backtracking(feld):
                                feld[x][y] = 0
                                values.remove(wert)
                            else:
                                return True
                    if len(values) == 0:
                        return False
                else:
                    pass
        return True

    def create_missing_element_list(self):
        for x in range(len(self.feld)):
            for y in range(len(self.feld)):
                if 0 == self.feld[x][y]:
                    self.elements_to_fill.append((x, y))
        return self.elements_to_fill

    def backtrack_solver(self, feld):
        values = list(range(1, len(feld) + 1))
        for element in self.elements_to_fill:
            if 0 == feld[element[0]][element[1]]:
                while len(values) != 0:
                    wert = random.choice(values)
                    feld[element[0]][element[1]] = wert
                    if not self.check_colums() or not self.check_rows() or not self.check_specific_square(element[0], element[1]):
                        feld[element[0]][element[1]] = 0
                        values.remove(wert)
                    else:
                        if not self.backtracking(feld):
                            feld[element[0]][element[1]] = 0
                            values.remove(wert)
                        else:
                            return True
                if len(values) == 0:
                    return False
            else:
                pass
        return True


doku = Sudoku()
# doku.backtracking(doku.feld)

# print(doku.feld)

#doku.feld[2][3] = 0
#doku.feld[5][6] = 0
#doku.feld[1][8] = 0

doku.create_missing_element_list()
doku.backtrack_solver(doku.feld)


print(doku.feld)

print("Success")
