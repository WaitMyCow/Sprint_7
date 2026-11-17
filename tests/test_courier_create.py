from utils import Utils
from generators import Generators
from data import *
import allure

@allure.suite('Проверка создания курьера')
class TestCourierCreate:
    #Курьера можно создать
    @allure.title('Проверка успешного создания курьера')
    def test_new_courier_create(self, register_new_courier_and_return_login_password):
        data, response = register_new_courier_and_return_login_password
        assert response.status_code == Codes.CREATED_CODE
        assert response.json() == {
            "ok": True
        }

    #Нельзя создать двух одинаковых курьеров
    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_two_couriers_with_same_login(self, register_new_courier_and_return_login_password):
        data, response = register_new_courier_and_return_login_password
        payload = {
            "login": data[0],
            "password": data[1],
            "firstName": data[2]
        }
        response = Utils.send_create_courier_request(payload)

        assert response.status_code == Codes.LOGIN_ALREADY_TAKEN_CODE
        assert response.json() == {
            "code": Codes.LOGIN_ALREADY_TAKEN_CODE,
            "message": JsonResponses.LOGIN_ALREADY_TAKEN_RESPONSE
        }

    #Нельзя создать курьера без логина
    @allure.title('Проверка курьера без логина')
    def test_create_courier_without_login(self):
        payload = {
            "login": "",
            "password": Generators.generate_random_string_10_length(),
            "firstName": Generators.generate_random_string_10_length()
        }
        response = Utils.send_create_courier_request(payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": Codes.INSUFFICIENT_DATA_CODE,
            "message": JsonResponses.INSUFFICIENT_DATA_CREATE_RESPONSE
        }

    #Нельзя создать курьера без пароля
    @allure.title('Проверка курьера без пароля')
    def test_create_courier_without_password(self):
        payload = {
            "login": Generators.generate_random_string_10_length(),
            "password": "",
            "firstName": Generators.generate_random_string_10_length()
        }
        response = Utils.send_create_courier_request(payload)

        assert response.status_code == Codes.INSUFFICIENT_DATA_CODE
        assert response.json() == {
            "code": Codes.INSUFFICIENT_DATA_CODE,
            "message": JsonResponses.INSUFFICIENT_DATA_CREATE_RESPONSE
        }