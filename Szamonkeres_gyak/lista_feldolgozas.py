import requests

url = "https://jsonplaceholder.typicode.com/users" 
# Az a cím, ahonnan az adatokat le szeretnénk kérni

# ------Első lépés  A lista lekérése

valasz = requests.get(url, timeout=10) 
# A requests.get() függvény lekéri az adatokat a megadott URL-ről, és a timeout paraméterrel megadhatjuk, hogy mennyi ideig várjon a válaszra (másodpercben).

print("Státuszkód:", valasz.status_code) 
# A státuszkódot kiírja a képernyőre, ami azt jelzi, hogy a kérés sikeres volt-e (200) vagy sem (pl. 404, 500).

# ------Második lépés  A típus és a darabszám vizsgálata

if valasz.status_code == 200:
# Ha a státuszkód 200, az azt jelenti, hogy a kérés sikeres volt, és folytathatjuk az adatok feldolgozását.
    
    felhasznalok = valasz.json()
    # A válasz JSON formátumú adatát Python objektummá alakítja
    
    print("Adat típus:", type(felhasznalok))
    # A típus kiírása a képernyőre, ami listát jelez (list)
    
    print("Felhasználók száma:", len(felhasznalok))
    # A felhasználók számát kiírja a képernyőre, ami a lista hosszát jelzi.

# ------Harmadik lépés  Az első elem megvizsgálása    

felhasznalok = valasz.json()
elso = felhasznalok[0]
# Az első elem (indexe [0]) [kiválasztása a listából, ami egy szótár (dictionary) formátumú adatot tartalmaz. Ezért az utána következő sorokban a szótár kulcsaihoz férünk hozzá.

print("Az első teljes rekord vagyis felhasználó adatai:")
print(elso)
print("Az első felhasználó neve:", elso["name"])
# A szótár kulcsaihoz való hozzáférés példája, ahol a "name" kulcs értékét írja ki a képernyőre.

#-------------------------------------------------------------------------------------------
# Hierarhikusan szemléltetve a JSON objektum kulcsait és azok belső kulcsait, ha vannak:
print("A JSON objektum kulcsai:")
for kulcs, ertek in elso.items():
    print(kulcs)
    if isinstance(ertek, dict):
        for belso_kulcs in ertek.keys():
            print("--->", belso_kulcs)
            if isinstance(ertek[belso_kulcs], dict):
                for belso_belso_kulcs in ertek[belso_kulcs].keys():
                    print("------>", belso_belso_kulcs)

#-------------------------------------------------------------------------------------------
# ---------Negyedik lépés: A lista bejárása for ciklussal
    #Nem szeretnénk minden indexet külön leírni. A for ciklus sorban beleteszi a lista minden elemét a felhasznalo változóba. A behúzott utasítás minden rekordnál egyszer lefut.

for felhasznalo in felhasznalok:
    print("Felhasználó neve:", felhasznalo["name"])

# -----Ötödik lépés: Több mező és adatok kiírása a felhasználókról

    print("Azonosító:", felhasznalo["id"])
    print("Felhasználó e-mail címe:", felhasznalo["email"])
    print("Felhasználó városa:", felhasznalo["address"]["city"])
    print("Gég:", felhasznalo["company"]["name"])

    # Mit jelent a beágyazott elérés:
    #   felhasznalo["address"]["city"]
        #1.	A felhasznalo egy szótár.
        #2.	A ["address"] kiválasztja a címhez tartozó belső szótárat.
        #3.	A ["city"] ebből a belső szótárból választja ki a várost.

# ------Hatodik lépés  Rendezett sorszámozott kiírás
    
for sorszam, felhasznalo in enumerate(felhasznalok, start=1):
    print(sorszam, "-", felhasznalo['name'])
     


            