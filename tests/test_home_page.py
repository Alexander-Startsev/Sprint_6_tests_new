import allure
from utils.urls import Urls


@allure.epic("Главная страница: переходы")
@allure.suite("Header и основные кнопки")
class TestHomePageNavigation:

    @allure.feature("Кнопки заказа")
    @allure.title("Кнопка в шапке ведёт на страницу оформления заказа")
    def test_order_from_header_opens_order_page(self, home_page):
        home_page.click_top_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature("Кнопки заказа")
    @allure.title("Кнопка в блоке «Как это работает» ведёт на страницу оформления заказа")
    def test_order_from_bottom_opens_order_page(self, home_page):
        home_page.click_bottom_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.feature("Редиректы")
    @allure.title("Клик по лого ЯндексСамокат открывает Яндекс/Дзен/капчу")
    def test_logo_redirects_to_yandex(self, home_page):
        home_page.click_yandex_button()
        home_page.switch_window(1)
        home_page.wait_url_until_not_about_blank()
        current_url = home_page.current_url()
        assert any(part in current_url for part in (Urls.YANDEX_HOME_PAGE, Urls.DZEN_HOME_PAGE, Urls.YANDEX_CAPTCHA_PAGE))
