import requests
import pytest

url = 'https://api.pokemonbattle.ru/v2'
token = '970c7b088b383562a31ab9909ef500cd'
header = {'Content-Type' :'application/json', 'trainer_token': token}
trainer_id = '18168'

def test_status_code():
    response = requests.get(url=f'{url}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url=f'{url}/pokemons', params= {'trainer_id': trainer_id})
    assert response_get.json()["data"][0]["name"] == 'lugia'


@pytest.mark.parametrize('key, value', [('name', 'lugia'), ('trainer_id', trainer_id), ('id', '204861')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{url}/pokemons', params= {'trainer_id': trainer_id})
    assert response_parametrize.json()["data"][0][key] == value 


def test_my_of_trainer():
    response_trainer = requests.get(url=f'{url}/trainers', params= {'trainer_id': trainer_id})
    assert response_trainer.json()["data"][0]["id"] == trainer_id