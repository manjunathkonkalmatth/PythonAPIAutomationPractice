
import requests as req

# def test_PostRequest():
baseURL = 'https://reqres.in'
createUserURL = '/api/users'
userInfo = '/api/user/'
payload = {    "name": "morpheus",    "job": "leader"}
res = req.post(baseURL+createUserURL,data = payload)
print(res.url)
print(res.json())
id = res.json()['id']
print('status code is '+ str(res.status_code))
res = req.get(baseURL+userInfo+str(id))
print(res.url)
print(res.json())
print('status code is '+ str(res.status_code))
