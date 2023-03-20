from requests import get, post, delete

print(get('http://127.0.0.1:8080/api/v2/news/8').json())

