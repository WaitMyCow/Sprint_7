from utils import Utils
import allure

@allure.suite('Проверка создания курьера')
class TestCourierCreate:
    #Курьера можно создать
    @allure.title('Проверка успешного создания курьера')
    def test_new_courier_create(self):
        data, response = Utils.register_new_courier_and_return_login_password()
        assert response.status_code == 201
        assert response.json() == {
            "ok": True
        }

    #Нельзя создать двух одинаковых курьеров
    @allure.title('Проверка создания двух одинаковых курьеров')
    def test_create_two_couriers_with_same_login(self):
        data, response = Utils.register_new_courier_and_return_login_password()
        payload = {
            "login": data[0],
            "password": data[1],
            "firstName": data[2]
        }
        response = Utils.send_create_courier_request(payload)

        assert response.status_code == 409
        assert response.json() == {
            "code": 409,
            "message": "Этот логин уже используется. Попробуйте другой."
        }

    #Нельзя создать курьера без логина
    @allure.title('Проверка курьера без логина')
    def test_create_courier_without_login(self):
        payload = {
            "login": "",
            "password": Utils.generate_random_string_10_length(),
            "firstName": Utils.generate_random_string_10_length()
        }
        response = Utils.send_create_courier_request(payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }

    #Нельзя создать курьера без пароля
    @allure.title('Проверка курьера без пароля')
    def test_create_courier_without_password(self):
        payload = {
            "login": Utils.generate_random_string_10_length(),
            "password": "",
            "firstName": Utils.generate_random_string_10_length()
        }
        response = Utils.send_create_courier_request(payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи"
        }