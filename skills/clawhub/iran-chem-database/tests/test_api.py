"""API smoke tests using FastAPI TestClient (no DB required for /health)."""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    # Import after monkeypatching DB to avoid touching a real database.
    from src.api.app import app
    return TestClient(app)


def test_health(client):
    resp = client.get("/api/v1/health")
    assert resp.status_code == 200
    assert resp.json()["ok"] is True
