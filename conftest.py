import pytest
from utils import Utils
from generators import Generators

@pytest.fixture
def register_new_courier_and_return_login_password():
    login = Generators.generate_random_string_10_length()
    password = Generators.generate_random_string_10_length()
    first_name = Generators.generate_random_string_10_length()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = Utils.send_create_courier_request(payload)

    yield [login, password, first_name], response
