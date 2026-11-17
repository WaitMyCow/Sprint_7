import random
import string
from utils import Utils
from datetime import datetime, timedelta


class Generators:
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
    def generate_order(color):
        firstName = Generators.generate_random_string_10_length()
        lastName = Generators.generate_random_string_10_length()
        address = Generators.generate_random_string_10_length()
        metroStation = random.randint(1, 30)
        phone = Generators.generate_random_phone()
        rentTime = random.randint(1, 30)
        deliveryDate = Generators.generate_random_date()
        comment = Generators.generate_random_string_10_length()

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