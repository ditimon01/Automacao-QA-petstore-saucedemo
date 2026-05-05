import requests
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

class APIClient:
    
    def __init__(self,timeout=10):
        self.headers = {
            "Content-Type": "application/json"
            }
        self.timeout = timeout
    
    def get(self, endpoint,params=None):
        return requests.get(f"{BASE_URL}{endpoint}",params=params, headers=self.headers, timeout=self.timeout)

    def post(self, endpoint, data):
        return requests.post(f"{BASE_URL}{endpoint}", json=data, headers=self.headers, timeout=self.timeout)

    def put(self, endpoint, data):
        return requests.put(f"{BASE_URL}{endpoint}", json=data, headers=self.headers, timeout=self.timeout)

    def delete(self, endpoint):
        return requests.delete(f"{BASE_URL}{endpoint}", headers=self.headers, timeout=self.timeout)
    
    
client = APIClient()