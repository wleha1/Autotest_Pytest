import pytest
import requests

TOKEN = "e93fb9d1e1fbf0301acaa4089c1086ab"

BASE_URL = "https://api.pokemonbattle.ru/v2"
HEADERS = {"trainer_token": TOKEN, "Content-type": "application/json"}
TRAINER_ID = "22850"

def test_status_code():
    response = requests.get(f"{BASE_URL}/trainers", headers=HEADERS)
    assert response.status_code == 200, f"Некорректный статус код: {response.status_code}"

def test_trainer_name():
    response = requests.get(f"{BASE_URL}/trainers", params={"trainer_id": TRAINER_ID}, headers=HEADERS)
    data = response.json().get("data", [])
    
    assert data and isinstance(data, list), "Ответ API некорректен или пуст"
    
    trainer_name = data[0].get("trainer_name")
    assert trainer_name, "Имя тренера отсутствует или пустое"

    print("Имя тренера:", trainer_name)
