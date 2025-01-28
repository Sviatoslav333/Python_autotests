import requests

url = 'https://api.pokemonbattle.ru/v2'
token = '970c7b088b383562a31ab9909ef500cd'
header = {'Content-Type' :'application/json', 'trainer_token': token}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_change = {
    "pokemon_id": "204588",
    "name": "Winner"
}

body_catch = {
    "pokemon_id": "204588"
}

'''response_create = requests.post(url= f'{url}/pokemons', headers=header,json=body_create)
message  = response_create.json()['message']
print(message)'''


'''response_change = requests.patch(url= f'{url}/pokemons', headers=header,json=body_change)
message  = response_change.json()['message']
print(message)'''


response_catch = requests.post(url= f'{url}/trainers/add_pokeball', headers=header,json=body_catch)
message  = response_catch.json()['message']
print(message)
