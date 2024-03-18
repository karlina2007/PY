#Ir dota avlsts un tev jāieraksta tās galvaspilsēta - izglītojošā spēle, bet arī ar minēšanas principu

from random import randint
valstis = {
    "Francija": "Parīze",
    "Itālija": "Roma",
    "Grieķija": "Atēnas",
    "Lietuva": "Viļņa",
    "Igaunija": "Tallina",
    "Somija": "Helsinki",
    "Norvēģija": "Oslo",
    "Zviedrija": "Stokholma",
    "Vācija": "Berlīne",
    "Dānija": "Kopenhāgena",
    "Latvija": "Rīga",
    "Polija": "Varšava"
}



valstis_saraksts = ["Francija", "Itālija", "Grieķija", "Lietuva", "Igaunija", "Somija", "Norvēģija", "Zviedrija", "Vācija", "Dānija", "Latvija", "Polija"]
atslegas = list(valstis.keys())

skaits=0
pareizas_atbildes=0

while True:
    gadijums= randint(0, len(atslegas)-1)
    galvaspilsēta = input(f"Kas ir {atslegas[gadijums]}s galvaspilsēta?")
    if galvaspilsēta.lower() == "quit":
        print("Paldies par spēli!")
        break
    elif galvaspilsēta.capitalize() ==valstis[atslegas[gadijums]]:
        print('Pareizi!')
        pareizas_atbildes+=1
    else:
        print(f"Nepareizi! Pareizā atbilde:{valstis[atslegas[gadijums]]}")
    skaits+=1

print(f"Tu pareizi atbildēji uz {pareizas_atbildes} no {skaits} jautājumiem")


