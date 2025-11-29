import pytest
import allure
from utils.urls import Urls
from utils.locators import YaScooterOrderPageLocator as Loc
from utils.test_data import YaScooterOrderPageData as order_data


@allure.epic("Создание заказа")
@allure.parent_suite("Домашняя страница → Заказ")
class TestOrderPage:

    @allure.feature("Этап 'Для кого самокат'")
    @allure.title("Некорректные значения показывают сообщения об ошибке")
    @pytest.mark.parametrize("fill, value, locator", [
        ("set_first_name", "Вqw", Loc.INCORRECT_FIRST_NAME_MESSAGE),
        ("set_last_name", "Вqw", Loc.INCORRECT_LAST_NAME_MESSAGE),
        ("set_address", "Вqw", Loc.INCORRECT_ADDRESS_MESSAGE),
        ("set_phone", "Вqw", Loc.INCORRECT_TELEPHONE_NUMBER_MESSAGE),
    ])
    def test_incorrect_user_fields_show_error(self, order_page, fill, value, locator):
        getattr(order_page, fill)(value)
        order_page.next_step()
        assert order_page.find_element(locator).is_displayed()

    @allure.feature("Этап 'Для кого самокат'")
    @allure.title("Пустое поле метро показывает ошибку")
    def test_empty_subway_shows_error(self, order_page):
        order_page.next_step()
        assert order_page.find_element(Loc.INCORRECT_SUBWAY_MESSAGE).is_displayed()

    @allure.feature("Этап 'Для кого самокат'")
    @allure.title("Корректные данные открывают шаг «Про аренду»")
    def test_correct_user_data_opens_rent_step(self, order_page):
        order_page.fill_customer_info(order_data.data_sets["data_set1"])
        order_page.next_step()
        assert order_page.find_elements(Loc.ORDER_BUTTON)

    @allure.feature("Этап 'Про аренду'")
    @allure.title("Заполнение аренды и подтверждение заказа — успех")
    @pytest.mark.parametrize("data_set", ["data_set1", "data_set2"])
    def test_fill_rent_and_order_success(self, order_page, data_set):
        data = order_data.data_sets[data_set]
        order_page.fill_customer_info(data)
        order_page.next_step()
        order_page.fill_rent_info(data)
        order_page.submit_order()
        order_page.confirm_order()
        assert order_page.find_elements(Loc.ORDER_COMPLETED_INFO)

    @allure.feature("Полный путь")
    @allure.title("После оформления можно перейти на страницу статуса заказа")
    @pytest.mark.parametrize("data_set", ["data_set1", "data_set2"])
    def test_create_order_and_check_status(self, order_page, data_set):
        data = order_data.data_sets[data_set]
        order_page.fill_customer_info(data)
        order_page.next_step()
        order_page.fill_rent_info(data)
        order_page.submit_order()
        order_page.confirm_order()
        order_number = order_page.fetch_order_number()
        order_page.go_to_status()
        assert Urls.ORDER_STATUS_PAGE in order_page.current_url() and order_number in order_page.current_url()
