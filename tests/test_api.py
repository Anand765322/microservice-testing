import requests
from jsonschema import validate
import json

BASE_URL = "http://localhost:5000"

def test_hello():
    res = requests.get(f"{BASE_URL}/api/hello")
    assert res.status_code == 200
    assert res.json()["message"] == "Hello, World!"

def test_post_data():
    payload = {"name": "SDET", "role": "Tester"}
    res = requests.post(f"{BASE_URL}/api/data", json=payload)
    assert res.status_code == 201
    assert res.json()["received"] == payload

def test_post_data_schema():
    payload = {"name": "SDET", "role": "Tester"}
    res = requests.post(f"{BASE_URL}/api/data", json=payload)
    assert res.status_code == 201

    schema_path = "tests/schema/data_schema.json"
    with open(schema_path) as f:
        schema = json.load(f)

    validate(instance=res.json(), schema=schema)
