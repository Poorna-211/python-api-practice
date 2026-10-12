import requests
url = ("https://jsonplaceholder.typicode.com/posts")
student = {
    "name":"poorna",
    "course":"python API",
    "partner":"ganesh"
}
response=requests.post(url,json=student)
print(response.status_code)
print(response.json())
