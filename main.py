import requests

TOKEN = "e93fb9d1e1fbf0301acaa4089c1086ab"

BASE_URL = "https://api.pokemonbattle.ru/v2"
HEADERS = {"trainer_token": TOKEN, "Content-type": "application/json" }

create_pokemon_response = requests.post(
    f"{BASE_URL}/pokemons",
    headers=HEADERS,
    json={"name": "Новеньки", "photo_id": -1}
)
print("Создание покемона:", create_pokemon_response.json())

pokemon_id = create_pokemon_response.json().get("id")

change_pokemon_name = requests.put(
    f"{BASE_URL}/pokemons",
    headers=HEADERS,
    json={
    "pokemon_id": pokemon_id,
    "name": "Новый новеньки",
    "photo_id": 2
    }
)
print("Изменение покемона:", change_pokemon_name.json())

add_pokemon_pokeball = requests.post(
    f"{BASE_URL}/trainers/add_pokeball",
    headers=HEADERS,
    json={
    "pokemon_id": pokemon_id
    }
)
print("Покемон пойман в покебол:", add_pokemon_pokeball.json())