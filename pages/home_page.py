from __future__ import annotations

import allure

from pages.base_page import BasePage
from utils.locators import BasePageLocator, YaScooterHomePageLocator as Loc


class YaScooterHomePage(BasePage):
    @allure.step("Нажать на кнопку заказа вверху страницы")
    def click_top_order_button(self):

        self.scroll_to_top()
        self.safe_click(Loc.TOP_ORDER_BUTTON)

    @allure.step("Нажать на кнопку заказа внизу страницы")
    def click_bottom_order_button(self):
        self.safe_click(Loc.BOTTOM_ORDER_BUTTON)

    @allure.step("Нажать на вопрос №{question_number} в FAQ")
    def click_faq_question(self, question_number: int):

        self.wait_visible(Loc.FAQ_SECTION)
        buttons = self.find_elements(Loc.FAQ_BUTTONS, timeout=10)
        btn = buttons[question_number]
        self.safe_click_webelement(btn)

        self.wait_visible(Loc.FAQ_ANSWER(answer_number=question_number), timeout=10)

    @allure.step("Переключиться на вкладку браузера")
    def switch_window(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step("Перейти на страницу Яндекса (клик по лого)")
    def click_yandex_button(self):
        self.scroll_to_top()
        self.safe_click(BasePageLocator.YANDEX_SITE_BUTTON)

    @allure.step("Принять куки (если баннер есть)")
    def click_cookie_accept(self):
        try:
            self.safe_click(BasePageLocator.COOKIE_ACCEPT_BUTTON)
        except Exception:
            pass
