import random

surface = int(input("サイコロの面の数は?:"))
times = int(input("何回振りますか?:"))
dice = list(range(1, surface + 1))

print(dice)

for i in range(1, times + 1):
    result = random.choice(dice)
    print(result, end=", ")

