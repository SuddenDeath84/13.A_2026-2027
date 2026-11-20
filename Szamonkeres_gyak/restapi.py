import json
# 1. feladat (kiiratás json-ból)

json_szoveg = '''
{
    "termek": "Arduino Uno",
    "ar": 9500,
    "keszleten": true,
    "darabszam": 8
}
'''

adat = json.loads(json_szoveg)
# Megoldás
print("Termék:", adat["termek"])
print("Ár:", adat["ar"], "Ft")
print("Készleten van:", adat["keszleten"])
print("Darabszám:", adat["darabszam"], "db")

# 2. feladat kiiratás for ciklussal

json_szoveg = '''
[
    {"eszkoz": "Arduino Uno", "darabszam": 8},
    {"eszkoz": "Hőmérséklet-érzékelő", "darabszam": 12},
    {"eszkoz": "LED", "darabszam": 30},
    {"eszkoz": "Ellenállás", "darabszam": 50}
]
'''

eszkozok = json.loads(json_szoveg)
# Megoldás
for eszkoz in eszkozok:
    print(f'{eszkoz["eszkoz"]}: {eszkoz["darabszam"]} db')

# 3. feladat Feltételes feldolgozás
#Az előző adatokból csak azokat az eszközöket írd ki, amelyekből legalább 20 darab van!

#Megoldás
for eszkoz in eszkozok:
    if eszkoz["darabszam"] >= 20:
        print(f'{eszkoz["eszkoz"]}: {eszkoz["darabszam"]} db')

#4. Feladat Beágyazott objektum
# Az alábbi JSON szöveg egy beágyazott objektumot tartalmaz. Írd ki a termék nevét, árát, készleten van-e, darabszámát és a gyártó nevét!

import json

json_szoveg = '''
{
    "eszkoz": "Arduino Uno",
    "azonosito": 101,
    "halozat": {
        "ip_cim": "192.168.1.20",
        "port": 8080
    }
}
'''

adat2 = json.loads(json_szoveg)  

print("Eszköz:", adat2["eszkoz"])
print("Azonosító:", adat2["azonosito"])
print("IP-cím:", adat2["halozat"]["ip_cim"])
print("Port:", adat2["halozat"]["port"])

# GET kérés
# Gyakorló API	https://jsonplaceholder.typicode.com

