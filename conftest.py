import pytest
from api_clients.couriers_client import CourierClient
from data.url_endpoints import BASE_URL

@pytest.fixture(scope="session")
def courier_client():
    client = CourierClient(BASE_URL)
    yield client
    client.close()