# tel = {
#     "direktors": "67947253",
#     "vietnieks": "65674720",
#     "sekretāre": "65826974"
# }
# print(tel["vietnieks"]) #norādot atslēgu, izdrukā vērtību

# cenas = {'piens': 1.12, 'āboli': 0.95, 'apelsīni': 
# 1.89}
# print("piena cena ir:",cenas["piens"]) #izdrukā piena cenu
# print(cenas["apelsīni"]) #izdrukā apelsīnu cenu

# d = {
#     "k1": 123,
#     "k2": [10, 11, 12], 
#     "k3": {"atsl1": 100, "atsl2": 200}#vārdnīcās var uzglabāt arī lists un citas vārdnīcas
# }
# print(d["k3"]["atsl2"]) #izdrukā iekšējās vārdnīcas vērtību
# print(d["k2"][2]) #izdrukā saraksta elementu

# my_dict = {'key1': ['a','b', 'c']}
# my_list = my_dict['key1']
# burts = my_list[2]
# print(burts.upper()) #izdrukā lielo C, kas atrodas vārdnīcas vērtībā

# new_dict = {"k1": 100, "k2": 200}
# print(new_dict)
# new_dict["k3"] = 300
# print(new_dict)
# new_dict["k1"] = "simts"
# print(new_dict)

# print(new_dict.keys()) #izdrukā atslēgas
# print(new_dict.values()) #izdrukā vērtības
# print(new_dict.items()) #izdrukā visus pārus
# vertibu_list = list(new_dict.values()) #pārveido vērtības par list
# print(vertibu_list)
# print(new_dict.get("k2")) #get() - izdod norādītās atslēgas vērtību
# print(new_dict)

# print(new_dict.pop("k1")) #pop() - izņem elementu ar norādīto atslēgu
# print(new_dict)
# new_dict.update({"k4": 9}) #update() - pievieno jaunu elementu pāri 
# print(new_dict)
# new_dict.clear() #clear() - nodzēš/notīra saturu
# print(new_dict)

d={"k1": 11,"k2": 12,"k3": 13,}
for elements in d:
    print(elements)

for elements in d.items():
    print(elements)

for atslega, vertiba in d.items():
    print(vertiba)

