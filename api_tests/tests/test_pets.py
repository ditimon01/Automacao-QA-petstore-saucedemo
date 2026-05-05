import pytest
import random
from api_tests.services.pets_service import (
    add_pet,
    update_pet,
    get_pet_by_id,
    delete_pet,
    find_pet_by_status
)


@pytest.fixture
def pet_payload():
    return {
        "id": random.randint(1000, 9999),
        "name": "doggie",
        "photoUrls": ["string"],
        "status": "available"
    }


def test_add_pet(pet_payload):
    response = add_pet(pet_payload)

    assert response.status_code == 200
    assert response.json()["id"] == pet_payload["id"]


def test_get_pet_by_id(pet_payload):
    add_pet(pet_payload)

    response = get_pet_by_id(pet_payload["id"])

    assert response.status_code == 200
    assert response.json()["id"] == pet_payload["id"]


def test_update_pet(pet_payload):
    add_pet(pet_payload)

    pet_payload["name"] = "updated-dog"

    response = update_pet(pet_payload)

    assert response.status_code == 200
    assert response.json()["name"] == "updated-dog"


def test_delete_pet(pet_payload):
    add_pet(pet_payload)

    response = delete_pet(pet_payload["id"])

    assert response.status_code == 200


def test_get_deleted_pet(pet_payload):
    add_pet(pet_payload)
    delete_pet(pet_payload["id"])

    response = get_pet_by_id(pet_payload["id"])

    assert response.status_code == 404


def test_find_pet_by_status():
    response = find_pet_by_status("available")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_pet_invalid_id():
    response = get_pet_by_id("abc")

    assert response.status_code in [400, 404]


def test_get_nonexistent_pet():
    response = get_pet_by_id(999999999)

    assert response.status_code == 404


def test_delete_nonexistent_pet():
    response = delete_pet(999999999)

    assert response.status_code in [404, 400]


def test_add_pet_invalid_payload():
    payload = {
        "id": "errado", 
        "name": 123,  
    }

    response = add_pet(payload)

    assert response.status_code in [400, 405, 500]


#teste desativado devido a lógica da api, caso o pet não exista para ser atualizado, ele é criado.


# def test_update_nonexistent_pet():
#     payload = {
#         "id": 999999999,
#         "name": "ghost",
#         "photoUrls": ["string"],
#         "status": "available"
#     }

#     response = update_pet(payload)

#     assert response.status_code == 404


def test_find_pet_invalid_status():
    response = find_pet_by_status("invalid_status")

#   retorna 200 e retorna os pets sem filtro.
    assert response.status_code == 200
    assert isinstance(response.json(), list)

