from api_tests.client.api_client import client


def create_user(payload):
    return client.post("/user", payload)

def create_users_with_array(payload):
    return client.post("/user/createWithArray", payload)

def create_users_with_list(payload):
    return client.post("/user/createWithList", payload)

def get_user(username):
    return client.get(f"/user/{username}")

def login_user(username, password):
    return client.get(f"/user/login", params={
        "username": username, 
        "password": password
        })

def logout_user():
    return client.get("/user/logout")

def update_user(username, payload):
    return client.put(f"/user/{username}", payload)

def delete_user(username):   
    return client.delete(f"/user/{username}")