import pytest
from api_clients.couriers_client import CourierClient
from api_clients.orders_client import OrdersClient
from data.data import exist_courier as ec, exist_courier_w_orders as ecwo, exist_courier_for_del as ec_4_del
from data.data import orders
from data.url_endpoints import BASE_URL

@pytest.fixture(scope="session")
def courier_client():
    client = CourierClient(BASE_URL)
    yield client
    client.close()


@pytest.fixture(scope="session")
def courier_client_w_data():
    client = CourierClient(BASE_URL)
    client.register_new_courier(ec["login"],ec["password"],ec["first_name"])
    client.register_new_courier(ec_4_del["login"],ec_4_del["password"],ec_4_del["first_name"])
    yield client
    CourierClient.delete_courier_by_login_passwd(ec["login"],ec["password"])
    client.close()


@pytest.fixture(scope="session")
def order_client_w_data():
    order_client = OrdersClient(BASE_URL)
    courier_id = CourierClient.create_courier_and_return_id(ecwo["login"],ecwo["password"],ecwo["first_name"])
    resp = order_client.create_order(orders[0])
    order_id = resp[1].get("track")
    order_client.accept_order_to_courier(order_id,courier_id)
    yield order_client, courier_id, order_id
    CourierClient.delete_courier_by_login_passwd(ecwo["login"],ecwo["password"])
    order_client.close()