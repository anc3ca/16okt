#izdrukāt visus skaitļus no 15-89, kuri dalās ar 5, 3 un 2
for x in range(15,90):
    if x%2 == 0 or x%3 == 0 or x%5 == 0:
        print(x)