data = input("データを入力してください（スペース区切り）：")
s_data = data.split()
s_data_length = len(s_data)


# 合計値
def sum():
    total = 0
    for i in s_data:
        total += int(i)
    print(f"合計値 {str(total)}")


# 最大値
def max_data():
    s_data_int = [int(i) for i in s_data]
    max_data = max(s_data_int)
    print(f"最大値 {str(max_data)}")


# 最小値
def min_data():
    s_data_int = [int(i) for i in s_data]
    min_data = min(s_data_int)
    print(f"最小値 {str(min_data)}")


# 平均値
def ave_data():
    total = 0
    for i in s_data:
        total += int(i)
    ave_data = total / s_data_length
    print(f"平均値 {ave_data:.0f}")


sum()
max_data()
min_data()
ave_data()
