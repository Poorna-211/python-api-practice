import requests
url ="https://wae-iota.vercel.app/api/users/19"
update_user = { 
    "name" : "poorna",
    "email" : "poorna.jp12@gmail.com",
    "age" : 25
}

response = requests.delete(url, auth = ("testuser", "test123"))
print(response.status_code)
print(response.json())

