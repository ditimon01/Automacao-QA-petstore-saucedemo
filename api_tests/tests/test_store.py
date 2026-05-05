import pytest
import random
from api_tests.services.store_service import (
    place_order,
    get_inventory,
    get_order_by_id,
    delete_order
)


@pytest.fixture
def order_payload():
    return {
        "id": random.randint(1000, 9999),
        "petId": random.randint(1, 100),
        "quantity": 1,
        "shipDate": "2026-05-05T10:00:00.000Z",
        "status": "placed",
        "complete": True
    }


def test_post_store_order(order_payload):
    response = place_order(order_payload)

    assert response.status_code == 200
    assert response.json()["id"] == order_payload["id"]


def test_get_store_order_by_id(order_payload):
    place_order(order_payload)

    response = get_order_by_id(order_payload["id"])

    assert response.status_code == 200
    assert response.json()["id"] == order_payload["id"]


def test_delete_store_order(order_payload):
    place_order(order_payload)

    response = delete_order(order_payload["id"])

    assert response.status_code == 200


def test_get_deleted_order_returns_404(order_payload):
    place_order(order_payload)
    delete_order(order_payload["id"])

    response = get_order_by_id(order_payload["id"])

    assert response.status_code == 404


def test_get_store_inventory():
    response = get_inventory()

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_get_order_invalid_id():
    response = get_order_by_id("abc")

    assert response.status_code in [400, 404]


def test_get_nonexistent_order():
    response = get_order_by_id(999999999)

    assert response.status_code == 404


def test_place_order_invalid_payload():
    payload = {
        "id": "errado", 
        "petId": "x",
        "quantity": -1
    }

    response = place_order(payload)

    assert response.status_code in [400, 405, 500]

