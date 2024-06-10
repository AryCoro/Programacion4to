a= 1
while a != 0:
    a= int (input("pon dos numeros"))
    if a==0:
        break
    else:    
        for i in range (1,11):
            print(f"{i}/{a} =")
            print(i/a)