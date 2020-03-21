n = int(input())
min_divider = n

for i in range(n - 1, 1, -1):
    if (n % i == 0):
        if (min_divider > i):
            min_divider = i
        
print(min_divider)







