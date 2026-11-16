from utils import Utils
import allure

@allure.suite('Проверка получения списка заказов')
class TestOrdersList: 
    @allure.title('Проверка получения всех активных\\завершённых заказов')    
    def test_get_order_list(self):
        response = Utils.get_order_list()

        assert response.status_code == 200 #Ответ преподавателя: Можно просто проверить статус код ответа и то что в теле есть список заказов
        assert isinstance(response.json()["orders"], list)