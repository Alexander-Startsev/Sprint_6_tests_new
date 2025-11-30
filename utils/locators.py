from selenium.webdriver.common.by import By


class BasePageLocator:
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[normalize-space(text())='да все привыкли']")
    YANDEX_SITE_BUTTON = (By.XPATH, "//a[.//img[@alt='Yandex']]")


class YaScooterHomePageLocator:
    FAQ_SECTION = (By.XPATH, "//div[contains(@class,'Home_FourPart__')]")
    FAQ_BUTTONS = (By.XPATH, "//div[@class='accordion__button']")
    TOP_ORDER_BUTTON = (By.XPATH, "//div[starts-with(@class,'Header')]/button[normalize-space(text())='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//div[starts-with(@class,'Home')]/button[normalize-space(text())='Заказать']")

    @staticmethod
    def FAQ_ANSWER(answer_number: int):
        return (By.XPATH, f"//div[@id='accordion__panel-{answer_number}']/p")


class YaScooterOrderPageLocator:
    FIRST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Имя')]")
    INCORRECT_FIRST_NAME_MESSAGE = (By.XPATH, "//input[contains(@placeholder,'Имя')]/parent::div/div")

    LAST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]")
    INCORRECT_LAST_NAME_MESSAGE = (By.XPATH, "//input[contains(@placeholder,'Фамилия')]/parent::div/div")

    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder,'Адрес')]")
    INCORRECT_ADDRESS_MESSAGE = (By.XPATH, "//input[contains(@placeholder,'Адрес')]/parent::div/div")

    SUBWAY_FIELD = (By.XPATH, "//input[contains(@placeholder,'метро')]")
    INCORRECT_SUBWAY_MESSAGE = (
        By.XPATH,
        "//input[contains(@placeholder,'метро')]/ancestor::div[contains(@class,'Order_Text__')]/div[@class!='select-search']"
    )

    @staticmethod
    def SUBWAY_HINT_BUTTON(subway_name: str):
        return (By.XPATH, f"//div[text()='{subway_name}']/parent::button")

    TELEPHONE_NUMBER_FIELD = (By.XPATH, "//input[contains(@placeholder,'Телефон')]")
    INCORRECT_TELEPHONE_NUMBER_MESSAGE = (By.XPATH, "//input[contains(@placeholder,'Телефон')]/parent::div/div")

    NEXT_BUTTON = (By.XPATH, "//button[normalize-space(text())='Далее']")
    BACK_BUTTON = (By.XPATH, "//button[normalize-space(text())='Назад']")

    DATE_FIELD = (By.XPATH, "//input[contains(@placeholder,'Когда')]")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//span[contains(@class,'Dropdown-arrow')]")
    RENTAL_PERIOD_LIST = (By.XPATH, "//div[contains(@class,'Dropdown-option')]")

    COLOR_CHECKBOXES = (By.XPATH, "//div[contains(text(),'Цвет')]/parent::div//input")
    COMMENT_FOR_COURIER_FIELD = (By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]")

    ORDER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Заказать' and not(@disabled)]")
    ACCEPT_ORDER_BUTTON = (By.XPATH, "//button[normalize-space(text())='Да']")
    ORDER_COMPLETED_INFO = (By.XPATH, "//div[contains(text(),'Номер заказа')]")
    SHOW_STATUS_BUTTON = (By.XPATH, "//button[normalize-space(text())='Посмотреть статус']")
