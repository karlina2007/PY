#map
# izveidot funkciju kas aprēķina skaitļu kvadrātus
def kvadrati(sk):
    return sk**2

print(kvadrati(5))

skaitli = [1,2,3,4,5,6,36]
print(map(kvadrati, skaitli))# nedarbojas nepieciešamā iterācija

#1.variants
for i in map(kvadrati,skaitli):
    print(i, end="")
print()

#2.variants
print(list(map(kvadrati,skaitli)))

#izveido funkciju kas nosaka vai vārda garums ir pāra vai nepāra skaitlis
kautkascits =["Ieva","Jānis","Katrīna"]

def garums(vards):
    if len(vards) % 2 == 0:
        return 'Pāra skaits'
    else:
        return "Nepāra skaits"
    
print(garums('Anastasija'))
print(list(map(garums,kautkascits)))

#Izveido funkciju kas nosaka un izdrukā vārda garumu
def varda_garums(vards):
    return len(vards)
print(list(map(varda_garums,kautkascits)))


#filter
#uzraksti funkciju kas nosaka vai dotais ir pāra vai nepāra skaitlis
def paris(skiatlis):
    return skiatlis % 2 ==0


print(paris(2))
skaitli=[25,36,52,45,87,14]
print(list(filter(paris,skaitli)))

for i in filter(paris,skaitli):
    print(i, end="")
print()
#aprēķināt riņķa laukumu
#3.14*r*r
def r_lauk(r):
    return 3.14* r**2>50

print(r_lauk(5))
radiusi=[1,6,0.25,14]

print(list(filter(r_lauk, radiusi)))

#### Labada expression (jeb anonīmā funkcija)
# uzraksti funkciju kas aprēķina skaitļu kvadrātus
def kvadratiL(sk):
    rez = sk**2
    return rez

# saisināta funkcija
def kvadratiL(sk):
    return sk**2

print(kvadratiL(5))
#noņem funkcijas definīciju un aizstāj ar labda
kvadr=lambda sk: sk**2
print(kvadr(6))

#sakombinā ar map
skaitli=[25,36,52,45,84,17]
print(list(map(lambda sk: sk**2, skaitli )))

#sakombinē ar filter
print(list(filter(lambda sk: sk % 2==0,skaitli)))