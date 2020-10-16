


# Get n amount of money to return change
n = int(input())

# Count of bills and coins
count = 0

# The kinds of money in won
# 50000, 10000, 5000 1000 500 100 50 10

while n >= 50000:
    count += 1
    n -= 50000
while n >= 10000:
    count += 1
    n -= 10000
while n >= 5000:
    count += 1
    n -= 5000
while n >= 1000:
    count += 1
    n -= 1000
while n >= 500:
    count += 1
    n -= 500
while n >= 100:
    count += 1
    n -= 100
while n >= 50:
    count += 1
    n -= 50
while n >= 10:
    count += 1
    n -= 10

# Output the result
print (count)
