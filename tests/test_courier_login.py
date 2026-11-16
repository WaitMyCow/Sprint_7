from utils import Utils
import allure

@allure.suite('Проверка авторизации курьера')
class TestCourierLogin:
    #курьер может авторизоваться;
    @allure.title('Проверка успешной авторизации курьера')
    def test_courier_login(self):
        data, response = Utils.register_new_courier_and_return_login_password()
        payload = {
            "login": data[0],
            "password": data[1]
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == 200
        assert "id" in response.json() #успешный запрос возвращает id

    #авторизация без логина
    @allure.title('Проверка авторизации курьера без логина')
    def test_courier_login_without_login(self):
        data, response = Utils.register_new_courier_and_return_login_password()
        payload = {
            "login": '',
            "password": data[1]
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для входа"
        }
    #авторизация без пароля

    @allure.title('Проверка авторизации курьера без пароля')
    def test_courier_login_without_password(self):
        data, response = Utils.register_new_courier_and_return_login_password()
        payload = {
            "login": data[0],
            "password": ''
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для входа"
        }

    #авторизация с неверным логином
    @allure.title('Проверка авторизации курьера с неверным логином')
    def test_courier_login_with_wrong_login(self):
        data, response = Utils.register_new_courier_and_return_login_password()
        payload = {
            "login": 'ivanov',
            "password": data[1]
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == 404
        assert response.json() == { 
            "code": 404,
            "message": "Учетная запись не найдена"
        }

    #авторизация с неверным паролем
    @allure.title('Проверка авторизации курьера с неверным паролем')
    def test_courier_login_with_wrong_password(self):
        data, response = Utils.register_new_courier_and_return_login_password()
        payload = {
            "login": data[0],
            "password": '12345Q#'
        }
        response = Utils.send_login_courier_request(payload)

        assert response.status_code == 404
        assert response.json() == { 
            "code": 404,
            "message": "Учетная запись не найдена"
        }