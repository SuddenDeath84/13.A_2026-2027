import os

filenev = "termekek.txt"                # A termékek fájlneve

print("A termékek listája:", filenev)   # Kiírja a fájl nevét


if os.path.exists(filenev):             # Ellenőrzi, hogy a fájl létezik

    print("A fájl létezik.")             # Kiírja, hogy a fájl létezik

else:                                   # Ha a fájl nem létezik, létrehozza
                                        # a fájlt és feltölti alapértelmezett 
                                        # termékekkel

    print("A fájl nem létezik, ezért létrehozom a fájlt.") 
                                        # Kiírja, hogy a fájl nem létezik,
                                        # ezért létrehozza 

    with open(filenev, "w", encoding="utf-8") as file: # Megnyitja a fájlt írásra,
                                                    # ha nem létezik, létrehozza
        file.write("Füzet;25\n")    # Add hozzá a termékeket a fájlhoz
        file.write("Toll;8\n")      # Add hozzá a termékeket a fájlhoz
        file.write("Ceruza;42\n")   # Add hozzá a termékeket a fájlhoz
        file.write("Vonalzó;15\n")  # Add hozzá a termékeket a fájlhoz
        file.write("Radír;6\n")     # Add hozzá a termékeket a fájlhoz

print("A termékek listája a fájlban:")

termeknev_lista = [] # Listába menti a termékek nevét
keszlet_lista = [] # Listába menti a termékek készletét

with open(filenev, "r", encoding="utf-8") as file: # Megnyitja a fájlt olvasásra

    for line in file:               # Beolvassa a fájl sorait és kiírja őket a képernyőre
            # ciklus futása közben a Python minden egyes lépésben beolvas egy újabb sort 
            # a fájlból, és azt belehelyezi a line nevű változóba.

        line = line.strip()          # Eltávolítja a sorvégi whitespace karaktereket
        if line != "":        # Csak a nem üres sorokat dolgozza fel
            termeknev, keszlet = line.split(";")  # A termék nevét és készletét elválasztja

            termeknev_lista.append(termeknev)  # Hozzáadja a termék nevét a lista végéhez
            keszlet_lista.append(int(keszlet))      # Hozzáadja a termék készletét a lista végéhez


print("\nKészletadatok:")  # Kiírja a készletadatok fejlécét
for i in range(len(termeknev_lista)):  # A termék nevét és készletét kiírja a képernyőre
    print(f"{termeknev_lista[i]}: {keszlet_lista[i]} db")  # Kiírja a termék nevét és készletét a képernyőre


atlag_keszlet = sum(keszlet_lista) / len(keszlet_lista)  # Kiszámítja az átlag készletet
legnagyobb_keszlet = max(keszlet_lista)  # Kiszámítja a legnagyobb készletet
legnagyobb_keszlet_index = keszlet_lista.index(legnagyobb_keszlet)  # Kiszámítja a legnagyobb készlet indexét


keves_keszlet = 0  # Számláló a kevés készletű termékekhez

for i in keszlet_lista:  # Végigmegy a készlet listán és megszámolja a kevés készletű termékeket
    if i < 10:  # Ha a készlet kevesebb, mint 10
        keves_keszlet += 1  # Növeli a számlálót

print(f"\nAz átlag készlet: {atlag_keszlet:.2f} db")
print(f"A legnagyobb készlet: {legnagyobb_keszlet} db")
print(f"A legnagyobb készletű termék: {termeknev_lista[legnagyobb_keszlet_index]}")
print(f"Kevés készletű termékek száma: {keves_keszlet}")

uj_termek = input("\nAdjon meg egy új terméket (név;készlet): ")  # Bekéri az új termék nevét és készletét
uj_keszlet = int(input("Adja meg az új termék készletét (0-100): "))  # Bekéri az új termék készletét 0 és 100 között

if 0 <= uj_keszlet <= 100:  # Ellenőrzi, hogy a készlet 0 és 100 között van-e
    with open(filenev, "a", encoding="utf-8") as file:  # Megnyitja a fájlt hozzáfűzésre
        file.write(f"{uj_termek};{uj_keszlet}\n")  # Hozzáadja az új terméket a fájlhoz

    print("Az új termék hozzáadva a fájlhoz.")
    
else:  # Ha a készlet nem 0 és 100 között van, kiírja a hibát
    print("Hiba: A készletnek 0 és 100 között kell lennie.")

















        

    
