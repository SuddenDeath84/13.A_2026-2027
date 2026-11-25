import requests

url = "https://jsonplaceholder.typicode.com/users"
valasz = requests.get(url, timeout=10)

if valasz.status_code == 200:
    felhasznalok = valasz.json()
    print("Találatok száma:", len(felhasznalok))

    for sorszam, felhasznalo in enumerate(felhasznalok, start=1):
        print(sorszam, felhasznalo["name"],
              "-", felhasznalo["address"]["city"])
else:
    print("Sikertelen kérés:", valasz.status_code)
