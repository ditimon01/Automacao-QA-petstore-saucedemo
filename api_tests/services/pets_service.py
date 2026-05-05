from api_tests.client.api_client import client

def add_pet(payload):
    return client.post("/pet", payload)


def update_pet(payload):
    return client.put("/pet", payload)


def get_pet_by_id(pet_id):
    return client.get(f"/pet/{pet_id}")


def delete_pet(pet_id):
    return client.delete(f"/pet/{pet_id}")


def find_pet_by_status(status):
    return client.get(f"/pet/findByStatus?status={status}")