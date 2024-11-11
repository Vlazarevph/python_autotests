import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '70edf50ece83adabf56b9808ff8d48b5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}


body_confirmation = {
    "trainer_token": TOKEN
 }

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
 }

body_change_name = {
    "pokemon_id": "3756",
    "name": "Абсолют",
    "photo_id": 566
}

body_catch = {
    "pokemon_id": "3756"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create) #Создание покемона
print(response_create.text)

message1 = response_create.json()['message']
print(message1)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name) #Смена имени и фото
print(response_change_name.text)

message2 = response_change_name.json()['message']
print(message2)


response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch) #Поймать в покебол
print(response_catch.text)

message3 = response_catch.json()['message']
print(message3)