import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '70edf50ece83adabf56b9808ff8d48b5'
HEADER = {'Content-Type : application/json', 'trainer_token':TOKEN}
TRAINER_ID = '9843'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Вячеслав'