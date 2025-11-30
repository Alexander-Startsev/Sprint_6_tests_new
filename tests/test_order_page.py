import pytest
import allure
from pages.order_page import YaScooterOrderPage
from utils.urls import Urls
from utils.test_data import YaScooterOrderPageData as order_data


@allure.epic("Создание заказа")
@allure.parent_suite("Домашняя страница → Заказ")
class TestOrderPage:

    @allure.feature("Этап 'Для кого самокат'")
    @allure.title("Некорректные значения показывают сообщения об ошибке")
    @pytest.mark.parametrize("fill, value, checker", [
        ("set_first_name", "Вqw", "is_first_name_error_displayed"),
        ("set_last_name", "Вqw", "is_last_name_error_displayed"),
        ("set_address", "Вqw", "is_address_error_displayed"),
        ("set_phone", "Вqw", "is_phone_error_displayed"),
    ])
    def test_incorrect_user_fields_show_error(self, order_page, fill, value, checker):
        getattr(order_page, fill)(value)
        order_page.next_step()
        assert getattr(order_page, checker)()

    @allure.feature("Этап 'Для кого самокат'")
    @allure.title("Пустое поле метро показывает ошибку")
    def test_empty_subway_shows_error(self, order_page):
        order_page.next_step()
        assert order_page.is_subway_error_displayed()

    @allure.feature("Этап 'Для кого самокат'")
    @allure.title("Корректные данные открывают шаг «Про аренду»")
    def test_correct_user_data_opens_rent_step(self, order_page):
        order_page.fill_customer_info(order_data.data_sets["data_set1"])
        order_page.next_step()
        assert order_page.is_rent_step_ready()

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
        assert order_page.is_order_completed_info_displayed()

    @allure.feature("Полный путь")
    @allure.title("После оформления можно перейти на страницу статуса заказа")
    @pytest.mark.parametrize("data_set, start_button", [
        ("data_set1", "top"),
        ("data_set2", "bottom"),
    ])
    def test_create_order_and_check_status(self, home_page, data_set, start_button):
        order_page = YaScooterOrderPage(home_page.driver)

        if start_button == "top":
            home_page.click_top_order_button()
        else:
            home_page.click_bottom_order_button()

        order_page.wait_loaded()
        data = order_data.data_sets[data_set]
        order_page.fill_customer_info(data)
        order_page.next_step()
        order_page.fill_rent_info(data)
        order_page.submit_order()
        order_page.confirm_order()
        order_number = order_page.fetch_order_number()
        order_page.go_to_status()
        assert Urls.ORDER_STATUS_PAGE in order_page.current_url() and order_number in order_page.current_url()
