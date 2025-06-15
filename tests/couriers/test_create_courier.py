import allure
import pytest
from data import data
from utils.helpers import generate_random_string

@allure.feature('Тесты на создание курьера')
class TestCreateCourier:

    @allure.title('Тесты создания курьера')
    @pytest.mark.parametrize(
        'login, password, first_name, result',
        [
            (generate_random_string(8), generate_random_string(8), 'John', data.RESP_CREATE_COURIER_SUCCESS),
            (data.exist_courier['login'], data.exist_courier['password'], data.exist_courier['first_name'], data.RESP_CREATE_COURIER_TWICE),
            (None, generate_random_string(8),'John', data.RESP_CREATE_COURIER_UNSUCCESS),
            (generate_random_string(8), None, 'John', data.RESP_CREATE_COURIER_UNSUCCESS),
            (generate_random_string(8), generate_random_string(8), None, data.RESP_CREATE_COURIER_SUCCESS)
        ],
        ids=[
            'Create courier success',
            'Create courier with exist login',
            'Create courier w/o login',
            'Create courier w/o password',
            'Create courier w/o first name'
        ]
    )
    def test_create_courier(self, courier_client, login, password, first_name, result):
        resp = courier_client.register_new_courier(login, password, first_name)
        assert resp[0] == result['code'] and resp[1] == result['content']