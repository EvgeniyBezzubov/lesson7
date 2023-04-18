def print_operation_table(operation, num_rows=6, num_columns=6):
    for x in range(1, num_rows + 1):
        nums = []
        for y in range(1, num_columns + 1):
            num = operation(x, y)
            num = str(num) + " "
            print(num, end='')
        print("", end='\n')
def operation(x,y):
        return x*y

print_operation_table(operation)