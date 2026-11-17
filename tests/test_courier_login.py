from utils import Utils
from data import *
from generators import Generators
import allure

@allure.suite('Проверка авторизации курьера')
class TestCourierLogin:
    #курьер может авторизоваться;
    @allure.title('Проверка успешной авторизации курьера')
    def test_courier_login(self, register_new_courier_and_return_login_password):
        data, response = register_new_courier_and_return_login_password
        payload = {
            "login": data[0],
            "password": data[1]
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == Codes.SUCCESS_CODE
        assert "id" in response.json() #успешный запрос возвращает id

    #авторизация без логина
    @allure.title('Проверка авторизации курьера без логина')
    def test_courier_login_without_login(self, register_new_courier_and_return_login_password):
        data, response = register_new_courier_and_return_login_password
        payload = {
            "login": '',
            "password": data[1]
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == Codes.INSUFFICIENT_DATA_CODE
        assert response.json() == {
            "code": Codes.INSUFFICIENT_DATA_CODE,
            "message": JsonResponses.INSUFFICIENT_DATA_LOGIN_RESPONSE
        }
    #авторизация без пароля

    @allure.title('Проверка авторизации курьера без пароля')
    def test_courier_login_without_password(self, register_new_courier_and_return_login_password):
        data, response = register_new_courier_and_return_login_password
        payload = {
            "login": data[0],
            "password": ''
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == Codes.INSUFFICIENT_DATA_CODE
        assert response.json() == {
            "code": Codes.INSUFFICIENT_DATA_CODE,
            "message": JsonResponses.INSUFFICIENT_DATA_LOGIN_RESPONSE
        }

    #авторизация с неверным логином
    @allure.title('Проверка авторизации курьера с неверным логином')
    def test_courier_login_with_wrong_login(self, register_new_courier_and_return_login_password):
        data, response = register_new_courier_and_return_login_password
        payload = {
            "login": Generators.generate_random_string_10_length(),
            "password": data[1]
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == Codes.NOT_FOUND_CODE
        assert response.json() == { 
            "code": Codes.NOT_FOUND_CODE,
            "message": JsonResponses.NOT_FOUND_RESPONSE
        }

    #авторизация с неверным паролем
    @allure.title('Проверка авторизации курьера с неверным паролем')
    def test_courier_login_with_wrong_password(self, register_new_courier_and_return_login_password):
        data, response = register_new_courier_and_return_login_password
        payload = {
            "login": data[0],
            "password": Generators.generate_random_string_10_length()
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == Codes.NOT_FOUND_CODE
        assert response.json() == { 
            "code": Codes.NOT_FOUND_CODE,
            "message": JsonResponses.NOT_FOUND_RESPONSE
        }