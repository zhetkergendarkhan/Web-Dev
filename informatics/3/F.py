numb = int(input())
count_of_dividers = 0
for i in range(1,numb+1):
    if (numb % i == 0):
        count_of_dividers += 1
print(count_of_dividers)