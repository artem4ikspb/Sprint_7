import allure
import pytest
from data.data import orders

@allure.feature('Тесты заказов')
class TestOrders:

    @allure.title('Тест создания заказа')
    @pytest.mark.parametrize(
        'order',
        [
            (orders[0]), 
            (orders[1]), 
            (orders[2])
        ],
        ids=[
            "color: DARK", 
            "color: GRAY", 
            "color: DARK+GRAY"
        ]
    )
    def test_create_order(self, order_client_w_data, order):
        resp = order_client_w_data[0].create_order(order)
        assert resp[0] == 201 and 'track' in resp[1], f'Ответ не совпадает с ожидаемым (code: {resp[0]}, body:{resp[1]})'

    @allure.title('Тест получения заказов курьера')
    def test_get_orders(self, order_client_w_data):
        resp = order_client_w_data[0].get_orders(order_client_w_data[1])
        assert resp[0] == 200 and 'orders' in resp[1], f'Ответ не совпадает с ожидаемым (code: {resp[0]}, body:{resp[1]})'

