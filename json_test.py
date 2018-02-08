import requests

r = requests.get(url='https://www.abcmouse.com/apis/abc/0.1/json/Shopping/GetCategoryItems/init')
print(r.json())