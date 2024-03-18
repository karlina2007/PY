#vienkārši piepildīt list ar elementiem
saraksts=list(range(0,11,2))
print(saraksts)

#enumerate- parāda indeksus tuple formā-izdrukā indeksus un burtus kopā
vards="pasaule"
for i in enumerate(vards):
    print(i)
#atpakot tuples-izdrukā tikai indeksus vai burtus ar atstarpi(\n)
for index, burts in enumerate(vards):
    print(index)
    print(burts)
    print('\n')
#izmanto zip- sapako vairākus list kā tupe- strādā tikai ar pāra skaitli
my_list =[1,2,3]
my_list2=['a',"b","c"]
my_list3=['12',3,"t"]
for i in zip(my_list,my_list2,my_list3):
    print(i)

#saliek visu vienā list
    print(list(zip(my_list,my_list2,my_list3)))

#izmanto in lai noskaidrotu vai objektā atrodams meklētais elements(True,False)
    print("x" in [1,2,3])
    print(2 in [1,2,3])
    print('a' in 'pasaule')
    print("atslega1" in {'atslega1':256})
    d={"atslega1":256}
    print(256 in d.keys())
    print(256 in d.values())

# min un max
my_list =[10,20,15,3.9,45]
print(min(my_list))

