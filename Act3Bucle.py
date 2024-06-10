
a=int(input("numero entero positivo"))
for i in range(1, a):
    if i%2 != 0:
        print(i, end=",")
    else:
        continue
