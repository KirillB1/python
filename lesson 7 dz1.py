class Matrix:
    def __init__(self, l_1, l_2):
        # self.matr = [list_1, list_2]
        self.l_1 = l_1
        self.l_2 = l_2

    def __add__(self):
        m = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.l_1)):

            for j in range(len(self.l_2[i])):
                m[i][j] = self.l_1[i][j] + self.l_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))



my_matrix = Matrix([[5, 18, 11],
                    [6, 17, 23],
                    [41, 50, 9]],
                   [[45, 8, 2],
                    [6, 7, 93],
                    [24, 5, 97]])
# result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


print(my_matrix.__add__())
