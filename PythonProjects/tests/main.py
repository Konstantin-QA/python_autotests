import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = '8b9214177f4faae41972f011b86a1ce7'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
body_craete = {
    "name": "generate",
    "photo_id": -1
}
body_update = {
    "pokemon_id": "188727",
    "name": "bobr",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "188727"
}

response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_craete )
print(response_create.json())

response_update = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_update )
print(response_update.json())

response_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(response_pokeball.json())

