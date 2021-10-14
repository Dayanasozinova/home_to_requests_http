import requests 
import json

data = {}
r = requests.get(' https://superheroapi.com/api/2619421814940190/search/Thanos')
print(r.text)

Hulk = requests.get(' https://superheroapi.com/api/2619421814940190/332/powerstats')
Captain_America = requests.get(' https://superheroapi.com/api/2619421814940190/149/powerstats')
Thanos = requests.get(' https://superheroapi.com/api/2619421814940190/655/powerstats')
# print(Captain_America.json()['intelligence'])
data["Hulk"] = Hulk.json()['intelligence']
data["Captain_America"] = Captain_America.json()['intelligence']
data["Thanos"] = Thanos.json()['intelligence']
print(data)



if int(data['Captain_America']) > int(data['Hulk']) > int(data['Thanos']):
    print('Капитан Америка самый умный')

elif int(data['Captain_America']) < int(data['Hulk']) < int(data['Thanos']):
    print('Танос самый умный')

elif int(data['Captain_America']) < int(data['Hulk']) > int(data['Thanos']) :
    print('Халк самый умный')

