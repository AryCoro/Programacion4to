a = 1
while a != 0:
    a= int (input("Dame el valor y te devuelvo la tabla de multiplicar"))
    if a==0:
        break
    else:    
        for i in range (1,11):
            print(f"{i}X {a} =")
            print(i*a)