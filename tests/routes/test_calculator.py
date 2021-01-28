import pytest
from fastapi.testclient import TestClient

from prefix_infix_calculator.app import create_app

app = create_app()


@pytest.mark.integration
def test_infix():
    with TestClient(app) as client:
        response = client.post("/infix", json = {"expression": "( 1 + 2 )"})
        assert response.status_code == 200


@pytest.mark.integration
def test_prefix():
    with TestClient(app) as client:
        response = client.post("/prefix", json = {"expression": "+ 1  2"})
        assert response.status_code == 200