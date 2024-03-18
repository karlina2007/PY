# i = 1 
# while i <= 5:
#     print("labi")
#     i += 1 
# print("i tagad ir", i) 

# j = 0 #tipisks cikla mainīgais
# while j < 5:
#     print("Nr.", j)
#     j += 1

# i = 5
# while i > 0:
#     print("Skaita atpakaļ", i)
#     i -= 1 # i=i-1

# i = 20
# while True: # cikls darbosies, kamēr nosacījums būs patiess
#     if i > 26:
#         break # pārtrauc ciklu, ja nosacījums nepatiess
# print("i ir", i)
# i += 2

# i = 1
# while i<=100:
#     if i%5==0 and i%7==0:
#         print("fizzbuzz", end=" ")
#     elif i%5==0:
#         print("fizz", end=" ")
#     elif i%7==0:
#         print("buzz", end=" ")
#     else:
#         print(i, end=" ")
#     i+=1

    

# x= int(input("Ievadi stāvus:"))
# i=0
# while i<x:
#     print("*"*x)
#     i+=1


# for skaitlis in range(15): #intervāls [0;15)
#     print(skaitlis)

# for skaitlis in range(4, 15): #intervāls [4;15)
#     print(skaitlis)

# for skaitlis in range(4, 15, 3): #intervāls (no; līdz; solis) 
#     print(skaitlis)

# mainigais = [1,2,3,4]
# for elements in mainigais:
#     print(elements)


# mylist = [1,2,3,4,5,6,7,8,9,10,11]
# for x in mylist:
#     print(x)

# for _ in mylist:
#     print("Sveiki")

# for skaitlis in mylist:
#     if skaitlis % 2 == 0:
#         print(skaitlis)
#     else:
#         print(f"Nepāra skaitlis:{skaitlis}")

mylist = [1,2,3,4,5,6,7,8,9,10,11]
summa = 0
for sk in mylist:
    summa =summa + sk 
    (f"Pēc{sk} skaitļu saskaitīšanas summa ir {summa}")
print(summa)

mystring ='Sveika, pasaule'