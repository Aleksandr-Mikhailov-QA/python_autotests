import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'da5ed79fa0250d1815eed941aa51fd8c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
POKEMON_ID = '66559'

body_create = {
    "name": "Python",
    "photo_id": 500
}

change_name = {
    "pokemon_id": "66731",
    "name": "Nohtyp",
    "photo_id": 500
}

catch_pokemon = {
    "pokemon_id": "58220"
}

'''response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = change_name)
print(response_change.text)'''

'''response_catch = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = catch_pokemon)
print(response_catch.text)'''