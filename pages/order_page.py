from __future__ import annotations

import re
import allure

from pages.base_page import BasePage
from utils.locators import YaScooterOrderPageLocator as Loc


class YaScooterOrderPage(BasePage):
    """Страница оформления заказа самоката."""

    @allure.step("Дождаться загрузки страницы заказа")
    def wait_loaded(self) -> None:
        self.wait_visible(Loc.FIRST_NAME_INPUT)

    # --- Этап 1: Для кого самокат ---
    @allure.step("Заполнить поле 'Фамилия'")
    def set_last_name(self, last_name: str) -> None:
        self.find_element(Loc.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Заполнить поле 'Имя'")
    def set_first_name(self, first_name: str) -> None:
        self.find_element(Loc.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step("Заполнить поле 'Адрес'")
    def set_address(self, address: str) -> None:
        self.find_element(Loc.ADDRESS_INPUT).send_keys(address)

    @allure.step("Выбрать метро: {station}")
    def select_subway(self, station: str) -> None:
        self.find_element(Loc.SUBWAY_FIELD).click()
        self.find_element(Loc.SUBWAY_HINT_BUTTON(station)).click()

    @allure.step("Ввести номер телефона")
    def set_phone(self, phone: str) -> None:
        self.find_element(Loc.TELEPHONE_NUMBER_FIELD).send_keys(phone)

    @allure.step("Проверить сообщение об ошибке в поле 'Имя'")
    def is_first_name_error_displayed(self) -> bool:
        return self.find_element(Loc.INCORRECT_FIRST_NAME_MESSAGE).is_displayed()

    @allure.step("Проверить сообщение об ошибке в поле 'Фамилия'")
    def is_last_name_error_displayed(self) -> bool:
        return self.find_element(Loc.INCORRECT_LAST_NAME_MESSAGE).is_displayed()

    @allure.step("Проверить сообщение об ошибке в поле 'Адрес'")
    def is_address_error_displayed(self) -> bool:
        return self.find_element(Loc.INCORRECT_ADDRESS_MESSAGE).is_displayed()

    @allure.step("Проверить сообщение об ошибке в поле 'Метро'")
    def is_subway_error_displayed(self) -> bool:
        return self.find_element(Loc.INCORRECT_SUBWAY_MESSAGE).is_displayed()

    @allure.step("Проверить сообщение об ошибке в поле 'Телефон'")
    def is_phone_error_displayed(self) -> bool:
        return self.find_element(Loc.INCORRECT_TELEPHONE_NUMBER_MESSAGE).is_displayed()

    @allure.step("Перейти к следующему шагу")
    def next_step(self) -> None:
        self.safe_click(Loc.NEXT_BUTTON)

    # --- Этап 2: Про аренду ---
    @allure.step("Указать дату аренды: {date}")
    def set_date(self, date: str) -> None:
        self.find_element(Loc.DATE_FIELD).send_keys(date)

    @allure.step("Выбрать срок аренды (индекс {index})")
    def set_rental_period(self, index: int) -> None:
        self.find_element(Loc.RENTAL_PERIOD_FIELD).click()
        self.find_elements(Loc.RENTAL_PERIOD_LIST)[index].click()

    @allure.step("Отметить цвет по индексу {index}")
    def choose_color(self, index: int) -> None:
        self.find_elements(Loc.COLOR_CHECKBOXES)[index].click()

    @allure.step("Добавить комментарий для курьера")
    def set_comment(self, comment: str) -> None:
        self.find_element(Loc.COMMENT_FOR_COURIER_FIELD).send_keys(comment)

    # --- Завершение заказа ---
    @allure.step("Кликнуть 'Заказать'")
    def submit_order(self) -> None:
        self.safe_click(Loc.ORDER_BUTTON)

    @allure.step("Шаг аренды доступен")
    def is_rent_step_ready(self) -> bool:
        return self.wait_visible(Loc.ORDER_BUTTON).is_displayed()

    @allure.step("Подтвердить заказ")
    def confirm_order(self) -> None:
        self.safe_click(Loc.ACCEPT_ORDER_BUTTON)

    @allure.step("Прочитать номер заказа")
    def fetch_order_number(self) -> str:
        text = self.find_element(Loc.ORDER_COMPLETED_INFO).text
        return "".join(re.findall(r"\d", text))

    @allure.step("Перейти к статусу заказа")
    def go_to_status(self) -> None:
        self.safe_click(Loc.SHOW_STATUS_BUTTON)

    @allure.step("Проверить отображение итоговой информации о заказе")
    def is_order_completed_info_displayed(self) -> bool:
        return self.wait_visible(Loc.ORDER_COMPLETED_INFO).is_displayed()

    # --- Групповые шаги ---
    @allure.step("Заполнить форму 'Для кого самокат'")
    def fill_customer_info(self, data: dict) -> None:
        self.set_first_name(data["first_name"])
        self.set_last_name(data["last_name"])
        self.set_address(data["address"])
        self.select_subway(data["subway_name"])
        # ключ оставлен как в тестовых данных
        self.set_phone(data["telepthone_number"])

    @allure.step("Заполнить форму 'Про аренду'")
    def fill_rent_info(self, data: dict) -> None:
        self.set_date(data["date"])
        self.set_rental_period(data["rental_period"])
        for idx in data["color"]:
            self.choose_color(idx)
        self.set_comment(data["comment_for_courier"])
