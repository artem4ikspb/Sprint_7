import allure
import requests as re
from api_clients.base_client import BaseClient
from data.url_endpoints import BASE_URL
from data.url_endpoints import REGISTER_COURIER_ENDPOINT as reg_url
from data.url_endpoints import COURIER_LOGIN_ENDPOINT as login_url
from data.url_endpoints import DELETE_COURIER_ENDPOINT as del_url
from json.decoder import JSONDecodeError
from utils.helpers import format_string


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

    @allure.step('Логин курьера в систему')
    def courier_login(self, login, password):
        login_data = {
            "login": login,
            "password": password
        }
        resp = self._post(login_url, data=login_data)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text
        
    @allure.step('Удаляем курьера по id')
    def courier_delete_by_id(self, id):
        endpoint = format_string(del_url, id)
        resp = self._delete(endpoint)
        try:
            return resp.status_code, resp.json()
        except JSONDecodeError:
            return resp.status_code, resp.text
        
    @allure.step('Получаем id курьера по его логину и паролю')
    def get_courier_id_by_login(self, login, password):
        resp_code, resp_body = self.courier_login(login, password)
        if resp_code < 300:
            assert resp_body.get('id') is not None, f'Учетная запись не найдена: {login} - {password}   id: {id}'
            return resp_body.get('id')
        return None
        
    @allure.step('Удаляем курьера по его логину и паролю')
    def courier_delete_by_login(self, login, password):
        id = self.get_courier_id_by_login(login, password)
        resp_code, resp_body = self.courier_delete_by_id(id)
        assert resp_code < 300, f'Удалить курьра не удалось, логин {login}, код ответа {resp_code}: {resp_body}'
        return resp_code, resp_body

    
    @staticmethod 
    def delete_courier_by_login_passwd(login, password):
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
        }

        url = BASE_URL + login_url
        # Выясняем Id
        response = re.post(url, json=payload)
        courier_id = response.json().get('id')
    
        url = BASE_URL + format_string(del_url, courier_id)
        #Удаляем
        response = re.delete(url)
        return response.status_code, response.content, response.request.url
    
    @staticmethod
    def create_courier_and_return_id(login, password, first_name) -> int:
        url = BASE_URL + reg_url
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = re.post(url, data=payload)
        
        # Выясняем Id
        url = BASE_URL + login_url
        courier_id = None
        response = re.post(url, json=payload)
        if response.status_code < 300:
            courier_id = response.json().get('id')
        return courier_id
    
