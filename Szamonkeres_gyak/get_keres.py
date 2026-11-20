import requests

url = "https://jsonplaceholder.typicode.com/users/1"

valasz = requests.get(url, timeout=10)

#print("Státuszkód:", valasz.status_code)
#print("A válasz szövege:")
#print(valasz.text)

#lekérdezzük a kulcsokat a JSON objektumból
print("A JSON objektum kulcsai:")
for kulcs, ertek in valasz.json().items():
    print(kulcs)
    if isinstance(ertek, dict):
        for belso_kulcs in ertek.keys():
            print("--->", belso_kulcs)
            if isinstance(ertek[belso_kulcs], dict):
                for belso_belso_kulcs in ertek[belso_kulcs].keys():
                    print("------>", belso_belso_kulcs)

# Szövegből Python adat

adat = valasz.json()
#adat = json.loads(json_valasz.text)  # Ez is működik, de a requests könyvtárnak van beépített json() metódusa
#A valasz.text csak szöveget ad. A valasz.json() a JSON-választ Python szótárrá vagy listává alakítja

print("Név:", adat["name"])
print("Felhasználónév:", adat["username"])
print("Felhasználó e-mail címe:", adat["email"])
print("Város:", adat["address"]["city"])





