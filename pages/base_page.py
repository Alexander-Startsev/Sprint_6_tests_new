from __future__ import annotations

import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from utils.urls import Urls


class BasePage:
    """Базовый объект страницы: ожидания, скролл, безопасные клики, навигация."""

    def __init__(self, driver):
        self.driver = driver

    def _wait(self, timeout: int = 10) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator, timeout: int = 10):
        return self._wait(timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    @allure.step("Найти элементы: {locator}")
    def find_elements(self, locator, timeout: int = 10):
        return self._wait(timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    @allure.step("Дождаться видимости: {locator}")
    def wait_visible(self, locator, timeout: int = 10):
        return self._wait(timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Element not visible: {locator}",
        )

    @allure.step("Дождаться кликабельности: {locator}")
    def wait_clickable(self, locator, timeout: int = 10):
        return self._wait(timeout).until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable: {locator}",
        )

    def _scroll_into_view(self, element) -> None:
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center', inline:'center'});",
            element,
        )

    def _js_click(self, element) -> None:
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Безопасный клик: {locator}")
    def safe_click(self, locator, timeout: int = 10) -> None:
        elem = self.wait_clickable(locator, timeout)
        self._scroll_into_view(elem)
        try:
            elem.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            elem = self.find_element(locator, timeout)
            self._scroll_into_view(elem)
            self._js_click(elem)

    @allure.step("Безопасный клик по WebElement")
    def safe_click_webelement(self, element) -> None:
        self._scroll_into_view(element)
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self._scroll_into_view(element)
            self._js_click(element)

    @allure.step("Прокрутить страницу к началу")
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo({top:0, behavior:'instant'});")

    @allure.step("Дождаться, что URL не равен: {url}")
    def wait_url_until_not(self, url: str, timeout: int = 10):
        return self._wait(timeout).until_not(EC.url_to_be(url))

    @allure.step("Перейти по адресу")
    def go_to_site(self, url: str | None = None) -> None:
        self.driver.get(url or Urls.MAIN_PAGE)

    @allure.step("Текущий URL")
    def current_url(self) -> str:
        return self.driver.current_url
