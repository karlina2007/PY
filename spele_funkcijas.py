#importē bibliotēkas
from random import randint, shuffle

#print(randint(1,100))
#saraksts = [1, 2, 3, 4, 5]
#shuffle(saraksts)
#print(saraksts)


#metode "try - except" - pārbauda vai tiek ievadīts prasītais

#while True:
 #   x = input("Ievadi veselu skaitli: ")
 #   try:
 #       if int(x):
 #           break
  #  except:
  #      print(f"{x} nav vesels skaitlis!")

#print(f"Tu ievadīji {x}")


#pārbauda, vai tiek ievadīts prasītais

#y = input("Ievadi 1, 2 vai 3: ")
#while y not in ["1", "2", "3"]:
  #  y = input("Ievadi 1, 2 vai 3: ")



#----------------------------- Sāk spēli 
    
#Sajauc glāzītes
glazites = ["✨", "✨", "🎈"]
print(*glazites)

def sajauc(glazites):
    shuffle(glazites)
    return glazites

#print(sajauc(glazites))

#Pajautā minējumu
def mans_minejums():
    minejums = ""
    while minejums not in ["1", "2", "3"]:
        minejums = input("Kurā glāzītē ir bumbiņa (Ievadi 1, 2 vai 3)?:")
    return int(minejums)

#print(mans_minejums())

#pārbauda vai minējums ir pareizs

def parbaudi_minejumu(glazites, minejums):
    if glazites[minejums-1] =="🎈":  #Lai sanāktu pareizais, tad ir jāpieliek -1, jo, ja tu rakstīsi 3 un nebūsi šeit ielicis -1, tad nestrādās, jo listā neeksistē 3. indekss, bet eksistē 0., 1. un 2.
        print("Tu uzvarēji! 🎉")
    else:
        print("Ne šoreiz, draudziņ...😧 Nākamreiz sanāks")
        print(glazites)


#Pa soļiem izsauc visas funkcijas
    #1. Sajauc glāzītes
sajauktais = sajauc(glazites)

    #2. Spēlētāja minējums
speletaja_minejums = mans_minejums()

    #3. Minējuma pārbaude
parbaudi_minejumu(sajauktais, speletaja_minejums)