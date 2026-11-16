
import requests
import random
import string
from datetime import datetime, timedelta


class Utils:
    @staticmethod
    def generate_random_string_10_length():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(10))

    @staticmethod
    def generate_random_phone():
        return "+7" + ''.join(random.choices('0123456789', k=10))

    @staticmethod
    def generate_random_date():
        start_date = datetime.now()
        random_days = random.randint(1, 30)
        date = start_date + timedelta(days=random_days)
        return date.strftime("%Y-%m-%d")


    @staticmethod
    def send_create_courier_request(payload):
        return requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier',
            json=payload
        )
    
    @staticmethod
    def send_login_courier_request(payload):
        return requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            json=payload
        )
    
    @staticmethod
    def register_new_courier_and_return_login_password():
        login = Utils.generate_random_string_10_length()
        password = Utils.generate_random_string_10_length()
        first_name = Utils.generate_random_string_10_length()
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = Utils.send_create_courier_request(payload)

        return [login, password, first_name], response


    @staticmethod
    def send_create_order(payload):
        return requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/orders',
            json=payload
        )

    @staticmethod
    def get_order_list(**kwargs): #kwargs нужен для ввода необязательных параметров. Например courierId, nearestStation, limit или page
        return requests.get(
            'https://qa-scooter.praktikum-services.ru/api/v1/orders',
            params=kwargs

        )
    @staticmethod
    def create_order(color):
        firstName = Utils.generate_random_string_10_length()
        lastName = Utils.generate_random_string_10_length()
        address = Utils.generate_random_string_10_length()
        metroStation = random.randint(1, 30)
        phone = Utils.generate_random_phone()
        rentTime = random.randint(1, 30)
        deliveryDate = Utils.generate_random_date()
        comment = Utils.generate_random_string_10_length()

        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment,
            "color": color
        }
        response = Utils.send_create_order(payload)
        return response

    def order_accept(id):
        return requests.get(
            f'https://qa-scooter.praktikum-services.ru/api/v1/orders/accept/1?courierId={id}'
        )