import pytest
from fastapi.testclient import TestClient

from prefix_infix_calculator.app import create_app

app = create_app()


@pytest.mark.integration
def test_health_check():
    with TestClient(app) as client:
        response = client.get("/healthcheck")
        assert response.status_code == 200
        assert response.text == '"OK"'

