N = int(input())

sum_1 = 0
sum_2 = 0

for _ in range(N):
    num = int(input())
    if num % 3 == 0:
        sum_1 += num
    else:
        sum_2 += num

if sum_1 > sum_2:
    sum_1 *= 2
else:
    sum_1 *= 3

if sum_2 > sum_1:
    sum_2 *= 2
else:
    sum_2 *= 3

result = sum_1 + sum_2

print(result)
