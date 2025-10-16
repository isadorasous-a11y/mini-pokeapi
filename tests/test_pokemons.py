from fastapi.testclient import TestClient
from app.main import app

c = TestClient(app)

def test_crud_happy_path():
    # CREATE
    payload = {
        "name": "charmander",
        "height": 6,
        "weight": 85,
        "types": ["fire"],
        "sprite": None,
        "external_id": 4
    }
    r = c.post("/pokemons", json=payload)
    assert r.status_code == 201
    data = r.json()
    pid = data["id"]

    # LIST
    r = c.get("/pokemons?limit=10&offset=0")
    assert r.status_code == 200
    assert any(x["id"] == pid for x in r.json()["results"])

    # GET
    r = c.get(f"/pokemons/{pid}")
    assert r.status_code == 200
    assert r.json()["name"] == "charmander"

    # UPDATE
    payload["height"] = 7
    r = c.put(f"/pokemons/{pid}", json=payload)
    assert r.status_code == 200
    assert r.json()["height"] == 7

    # DELETE
    r = c.delete(f"/pokemons/{pid}")
    assert r.status_code == 204

    # 404 após DELETE
    r = c.get(f"/pokemons/{pid}")
    assert r.status_code == 404
