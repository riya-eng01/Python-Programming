# print(1)
# print(2)
# print(3)

# For loops
for i in range(1, 6): # range function goes from 1 to (6-1) ie 5 in this case
    print(i)

# print the table of 5
num = 5
for i in range(1, 11):
    print(num, "X", i, "=", (num*i))

# Print even Nums
for i in range(1, 11):
    if (i % 2 == 0):
        print(i)

# Print Odd nums
for i in range(1, 11):
    if (i % 2 != 0):
        print(i)


# print numbers from 1 to 100
for i in range(1, 101):
    print(i, end=",")