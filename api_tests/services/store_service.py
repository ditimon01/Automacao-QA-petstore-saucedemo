from api_tests.client.api_client import client

def get_inventory():
    return client.get("/store/inventory")


def place_order(payload):
    return client.post("/store/order", payload)


def get_order_by_id(order_id):
    return client.get(f"/store/order/{order_id}")


def delete_order(order_id):
    return client.delete(f"/store/order/{order_id}")