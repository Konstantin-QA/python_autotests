import requests
import pytest 
URL = 'https://api.pokemonbattle.ru'
TOKEN = '8b9214177f4faae41972f011b86a1ce7'
HEADER = {'Content-type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '12761'

def test_status_code():
    response = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert response.status_code  == 200

def test_name_trainer():
    response = requests.get(url = f'{URL}/v2/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.json() ["data"][0]["trainer_name"] == 'Karter'