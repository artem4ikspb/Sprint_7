import allure
from data.data import exist_courier_for_del as ec_4_del

@allure.feature('Тесты на удаление курьера')
class TestCreateCourier:

    @allure.title('Положительный тест удаления курьера')
    def test_delete_courier(self, courier_client_w_data):
        resp = courier_client_w_data.courier_delete_by_login(ec_4_del["login"],ec_4_del["password"])
        assert resp[0] == 200 and resp[1] == {'ok': True}