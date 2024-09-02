import requests
import pytest

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'da5ed79fa0250d1815eed941aa51fd8c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '5189'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200 

def test_my_name():
    response_get = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]["trainer_name"] == 'Михей'