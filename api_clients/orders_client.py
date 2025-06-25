import allure
from api_clients.base_client import BaseClient
from data.url_endpoints import GET_ORDERS_ENDPOINT, CREATE_ORDER, ACCEPT_ORDER
from json.decoder import JSONDecodeError
from utils.helpers import format_string


class OrdersClient(BaseClient):

    @allure.step('Получить список заказов курьера')
    def get_orders(self, courier_id=None):
        endpoint = GET_ORDERS_ENDPOINT
        if courier_id is not None:
            endpoint = f'{endpoint}?courierId={courier_id}'

        resp = self._get(endpoint)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text
        
    @allure.step('Создать заказ')
    def create_order(self, order_data):
        resp = self._post(endpoint= CREATE_ORDER,
                          json = order_data
                          )
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text

    @allure.step('Принять заказ')
    def accept_order_to_courier(self, order_id, courier_id):
        endpoint = format_string(ACCEPT_ORDER, order_id)
        # data = {"courierId": courier_id}
        endpoint = f'{endpoint}?courierId={courier_id}'
        resp = self._put(endpoint)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text
        