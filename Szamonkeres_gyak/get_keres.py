import requests

url = "https://jsonplaceholder.typicode.com/users/1"

valasz = requests.get(url, timeout=10)

print("Státuszkód:", valasz.status_code)
print("A válasz szövege:")
print(valasz.text)

