import requests

url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.get(url)
print(response.status_code)
print(response.json())
data = response.json()
print("email")
print("name")
print("phone number")