import numpy as np
import random
import pdb


class Sudoku:
    def __init__(self):
        self.size = 9
        self.field = np.zeros(shape=(self.size, self.size), dtype=int)
        self.check_list = []
        self.elements_to_fill = []

    def set_value(self, x, y, value=0):
        self.field[x][y] = value

    def check_rows(self):
        for row in self.field:
            self.check_list = [x for x in row]
            if self.check_duplicates():
                self.check_list.clear()
                return False
            self.check_list.clear()
        return True

    def check_colums(self):
        for i in range(0, len(self.field)):
            self.check_list = [x[i] for x in self.field]
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
                            self.field[i + (square_colum * 3)][k + (square_row * 3)])
                if self.check_duplicates():
                    self.check_list.clear()
                    return False
        self.check_list.clear()
        return True

    def check_specific_square(self, x, y):
        for i in range(x // 3 * 3, x // 3 * 3 + 3):
            for k in range(y // 3 * 3, y // 3 * 3 + 3):
                self.check_list.append(self.field[i][k])
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

    def backtracking(self, field):
        values = list(range(1, len(field) + 1))
        for x in range(len(field)):
            for y in range(len(field)):
                if 0 == field[x][y]:
                    while len(values) != 0:
                        list_value = random.choice(values)
                        field[x][y] = list_value
                        if not self.check_colums() or not self.check_rows()or not self.check_specific_square(x, y):
                            field[x][y] = 0
                            values.remove(list_value)
                        else:
                            if not self.backtracking(field):
                                field[x][y] = 0
                                values.remove(list_value)
                            else:
                                return True
                    if len(values) == 0:
                        return False
                else:
                    pass
        return True

    def create_missing_element_list(self):
        for x in range(len(self.field)):
            for y in range(len(self.field)):
                if 0 == self.field[x][y]:
                    self.elements_to_fill.append((x, y))
        return self.elements_to_fill

    def backtrack_solver(self, field):
        values = list(range(1, len(field) + 1))
        for element in self.elements_to_fill:
            if 0 == field[element[0]][element[1]]:
                while len(values) != 0:
                    list_value = random.choice(values)
                    field[element[0]][element[1]] = list_value
                    if not self.check_colums() or not self.check_rows() or not self.check_specific_square(element[0], element[1]):
                        field[element[0]][element[1]] = 0
                        values.remove(list_value)
                    else:
                        if not self.backtracking(field):
                            field[element[0]][element[1]] = 0
                            values.remove(list_value)
                        else:
                            return True
                if len(values) == 0:
                    return False
            else:
                pass
        return True


doku = Sudoku()
doku.backtracking(doku.field)
print(doku.field)
