row = int(input("行数を入力してください:"))
column = int(input("列数を入力してください:"))

for j in range(1, row + 1):
    for i in range(1, column + 1):
        formula = f"{j} x {i} = "
        result = j * i
        output = f"{j * i} | "
        if result < 10:
            output = f" {j * i} | "
        else:
            output = f"{j * i} | "
        print(formula + output, end=" ")
    print()
