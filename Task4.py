class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        string = ""
        for i in self.lst:
            string = string + str(i) + "\n"
        return string

    def __add__(self, other):
        some_matrix = self.lst
        pos_x = 0
        pos_y = 0
        for i in self.lst:
            pos_x = 0
            for y in i:

                some_matrix[pos_y][pos_x] = self.lst[pos_y][pos_x] + other.lst[pos_y][pos_x]
                pos_x+=1

            pos_y+=1

        return some_matrix


list1 = [[31, 22], [37, 43], [51, 86]]
list2 = [[20, 50], [100, 43], [55, 11]]
obj1 = Matrix(list1)
obj2 = Matrix(list2)
print(obj1, "результат вывода на печать 1го обьекта")
otvet = obj1 + obj2
obj3 = Matrix(otvet)
print(obj3 , 'результат сложения')

