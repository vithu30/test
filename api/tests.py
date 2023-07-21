from fastapi.testclient import TestClient
from api import app


def test_api():
    with TestClient(app) as client:
        response = client.get("/test")
        print(response)
        assert response.status_code == 200
