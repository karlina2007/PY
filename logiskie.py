# print(3 > 4)
# print(2 == 2)
# print(2 * 2 == 4) 
# print(2 * 2 != 5) 
# a = 50
# b = 4
# c = 4
# print(a > b, b != c, c == a)
# print(a >= b, b < c, c <= a)

# print(True and True)
# a = 5
# b = 10
# print(a > 5 and b > 20)
# print(a >= 5 and b > 9)
# print(a >= 5 or b > 20)
# print(a >= 5 or b > 9)
# print(not a > 5)
# print(a > 4 or b > a or b > 10)


# new_list = ['a', 'e', 'x', 'b', 'c', '4','1']
# new_list.sort()
# new_list.reverse()
# print(new_list)

# piemēri
augli = ["banāns", "zemene", "apelsīns"]
print(augli[1])

#izņemt zemeni
augli.pop(1)
print(augli)
#pievieno sarakstā augli
augli.append("ābols")
print(augli)

#pievieno elementu konkrētā vietā
augli.insert(1, "citrons")
print(augli)
#aizstāj esošu elementa vērtību
augli[0] = "bumbieris"
print(augli)
#sakārto pēc alfabēta
augli.sort()
print(augli)

#izdrukā pilnu teikumu, cik augļi ir sarakstā
print(f"Šajā sarakstā ir {len(augli)} augļi.")

#izveido sarakstu ar pāra skaitļiem no 20 līdz 30, izmantojot ciklu
skaitli = []
i = 0
while i <= 30:
 skaitli.append(i)
 i += 2
print(skaitli)



