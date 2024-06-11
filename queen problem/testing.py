st = input("enter kannada string:")
ls = list(st)
print(ls)
print(st)
for i in range(9):
    print(i+1, end="")
print("\n"+st)
print(i for i in range(len(st)))
print(" ".join(i if i != "ಯ" else "" for i in ls))

