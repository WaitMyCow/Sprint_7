from generators import Generators
import pytest
import allure

@allure.suite('Проверка создания заказа')
class TestOrderCreate:
    #можно указать один из цветов — BLACK или GREY, оба цвета, совсем не указывать цвет
    @allure.title('Проверка успешного создания заказа с выбором цвета {param_color}')
    @pytest.mark.parametrize('param_color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_order_create(self, param_color):
        response = Generators.generate_order(param_color)

        assert response.status_code == 201
        assert "track" in response.json() #тело ответа содержит track.
