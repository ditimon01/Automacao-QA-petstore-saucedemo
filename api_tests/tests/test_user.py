import pytest
import random
import string
from api_tests.services.user_service import (
    create_user,
    create_users_with_array,
    create_users_with_list,
    get_user,
    login_user,
    logout_user,
    update_user,
    delete_user
)

def generate_username():
    return "user_" + ''.join(random.choices(string.ascii_lowercase, k=6))


@pytest.fixture
def user_payload():
    username = generate_username()
    return {
        "id": random.randint(1000, 9999),
        "username": username,
        "firstName": "Test",
        "lastName": "User",
        "email": f"{username}@test.com",
        "password": "123456",
        "phone": "999999999",
        "userStatus": 1
    }


def test_create_user(user_payload):
    response = create_user(user_payload)
    assert response.status_code == 200


def test_create_users_with_array():
    users = []
    
    for _ in range(2):
        username = generate_username()
        users.append({
            "id": random.randint(1000, 9999),
            "username": username,
            "firstName": "Test",
            "lastName": "User",
            "email": f"{username}@test.com",
            "password": "123456",
            "phone": "999999999",
            "userStatus": 1
        })
        
    response = create_users_with_array(users)
    assert response.status_code == 200
    
    for user in users:
        get_response = get_user(user["username"])
        assert get_response.status_code == 200
        assert get_response.json()["username"] == user["username"]


def test_create_multiple_users_with_list():
    users = []

    for _ in range(2):
        username = generate_username()
        users.append({
            "id": random.randint(1000, 9999),
            "username": username,
            "firstName": "Test",
            "lastName": "User",
            "email": f"{username}@test.com",
            "password": "123456",
            "phone": "999999999",
            "userStatus": 1
        })

    response = create_users_with_list(users)
    assert response.status_code == 200
    
    for user in users:
        get_response = get_user(user["username"])
        assert get_response.status_code == 200
        assert get_response.json()["username"] == user["username"]


def test_get_user(user_payload):
    create_user(user_payload)

    response = get_user(user_payload["username"])
    assert response.status_code == 200
    assert response.json()["username"] == user_payload["username"]


def test_login_user(user_payload):
    create_user(user_payload)

    response = login_user(user_payload["username"], user_payload["password"])
    assert response.status_code == 200
    assert "logged in user session" in response.text


def test_logout_user():
    response = logout_user()
    assert response.status_code == 200


def test_update_user(user_payload):
    create_user(user_payload)

    updated_data = user_payload.copy()
    updated_data["firstName"] = "Updated"

    response = update_user(user_payload["username"], updated_data)
    assert response.status_code == 200

    response_get = get_user(user_payload["username"])
    assert response_get.json()["firstName"] == "Updated"


def test_delete_user(user_payload):
    create_user(user_payload)

    response = delete_user(user_payload["username"])
    assert response.status_code == 200

    response_get = get_user(user_payload["username"])
    assert response_get.status_code == 404
    
def test_delete_nonexistent_user():
    username = "nonexistent_" + generate_username()
    response = delete_user(username)
    assert response.status_code == 404
    
def test_get_nonexistent_user():
    username = "nonexistent_" + generate_username()
    response = get_user(username)
    assert response.status_code == 404
    
def test_login_nonexistent_user():
    username = "nonexistent_" + generate_username()
    response = login_user(username, "wrongpassword")
    #api não valida corretamente, não existe validação de autenticação do login real
    assert response.status_code == 200
    
def test_login_wrong_password(user_payload):
    create_user(user_payload)

    response = login_user(user_payload["username"], "wrongpassword")
    #api não valida corretamente, não existe validação de autenticação do login real
    assert response.status_code == 200
    
def test_update_nonexistent_user():
    username = "nonexistent_" + generate_username()
    updated_data = {
        "firstName": "Updated"
    }
    response = update_user(username, updated_data)
    #api não valida corretamente, retorna 200 em erro
    assert response.status_code == 200

    
def test_update_user_invalid_data(user_payload):
    create_user(user_payload)

    updated_data = {
        "firstName": 123  
    }
    response = update_user(user_payload["username"], updated_data)
    #api não valida corretamente, retorna 200 em erro
    assert response.status_code == 200
    
def test_create_user_invalid_payload():
    payload = {
        "id": "invalid_id",
        "username": 12345,
        "firstName": "Test",
        "lastName": "User",
        "email": "invalid_email",
        "password": "123456",
        "phone": "999999999",
        "userStatus": 1
    }
    response = create_user(payload)
    assert response.status_code in [400,500]
    