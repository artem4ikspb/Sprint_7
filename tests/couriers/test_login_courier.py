import allure
import pytest
from data import data
from data.data import exist_courier as ec
from utils.helpers import generate_random_string as grs


class TestLoginCourier:
    
    @allure.title('Тест успешный логин курьера')
    def test_courier_login_success(self, courier_client_w_data):
        result = data.RESP_LOGIN_COURIER_SUCCESS
        resp = courier_client_w_data.courier_login(ec['login'], ec['password'])
        assert resp[0] == result['code'] and 'id' in resp[1], f'Ответ не соответствует ожидаемому: code: {resp[0]}, body {resp[1]}'

    @allure.title('Тест неуспешный логин курьера')
    @pytest.mark.parametrize(
        'login, password, result',
        [
            (ec['login'], 'wrong_password', data.RESP_LOGIN_COURIER_UNSUCCESS),
            ('login', ec['password'], data.RESP_LOGIN_COURIER_UNSUCCESS),
            (None, ec['password'], data.RESP_LOGIN_COURIER_WO_LOGIN),
            (ec['login'], None, data.RESP_LOGIN_COURIER_WO_PASSWORD),
            (grs(25), ec['password'], data.RESP_LOGIN_COURIER_UNSUCCESS)
        ],
        ids=[
            'Exist login and wrong pass',
            'Exist but wrong login and good pass',
            'Login w/o login',
            'Login w/o password',
            'Not exist login with good password'
        ]
    )
    def test_courier_login_unsuccess(self, courier_client_w_data, login, password, result):
        resp = courier_client_w_data.courier_login(login, password)
        assert resp[0] == result['code'] and resp[1] == result['body'], f'Ответ не соответствует ожидаемому: code: {resp[0]}, body {resp[1]}'


