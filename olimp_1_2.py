N = int(input())

# Initialize sums for even and odd numbers
sum_1 = 0
sum_2 = 0

# Process each number
for _ in range(N):
    num = int(input())
    if num % 3 == 0:
        sum_1 += num  # Add to even sum
    else:
        sum_2 += num   # Add to odd sum

# Process the even sum
if sum_1 > sum_2:
    sum_1 *= 2  # Double if divisible by 3
else:
    sum_1 *= 3  # Triple if not divisible by 3

# Process the odd sum
if sum_2 > sum_1:
    sum_2 *= 2  # Double if divisible by 3
else:
    sum_2 *= 3  # Triple if not divisible by 3

# Calculate the final result
result = sum_1 + sum_2

# Output the result
print(result)