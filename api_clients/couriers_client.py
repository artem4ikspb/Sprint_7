import allure
import requests
from api_clients.base_client import BaseClient
from data.url_endpoints import REGISTER_COURIER_ENDPOINT as reg_url
from json.decoder import JSONDecodeError
from utils.helpers import generate_random_string


class CourierClient(BaseClient):

    @allure.step('Создаем курьера')
    def register_new_courier(self, login, password, first_name):
        login_data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        resp = self._post(reg_url, data=login_data)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text



    @staticmethod
    def register_new_courier_and_return_login_password():
        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass