# a=int(input())
# b=int(input())
# if a>b:
#     print(1)
# elif a<b:
#     print(2)
# elif a==b:
#     print(0)
a = int(input())
b = int(input())

while a < b:
    if a % 2 == 0:
        print(a)
    a += 1
