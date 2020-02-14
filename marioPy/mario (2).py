from cs50 import get_int
c = get_int("Height:")

while c < 1 or c > 8:
    c = get_int("Height:")

for i in range(c):
    for j in range(c-1, i, -1):
        print(" ", end="")
    for o in range(i+1, 0, -1):
        print("#", end="")
    print()

