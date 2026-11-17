import requests
import allure
from urls import Urls

class Utils:
    @staticmethod
    @allure.step('Отправка запроса на создание курьера')
    def send_create_courier_request(payload):
        return requests.post(
            Urls.COURIER_URL,
            json=payload
        )
    
    @staticmethod
    @allure.step('Отправка запроса на авторизацию курьера')
    def send_login_courier_request(payload):
        return requests.post(
            Urls.LOGIN_COURIER_URL,
            json=payload
        )
    
    @staticmethod
    @allure.step('Отправка запроса на создание заказа')
    def send_create_order(payload):
        return requests.post(
            Urls.ORDERS_URL,
            json=payload
        )

    @staticmethod
    @allure.step('Отправка запроса на получение списка заказов')
    def get_order_list(**kwargs): #kwargs нужен для ввода необязательных параметров. Например courierId, nearestStation, limit или page
        return requests.get(
            Urls.ORDERS_URL,
            params=kwargs
        )