import pytest
import allure
from pages.home_page import YaScooterHomePage
from utils.test_data import YaScooterHomePageFAQ
from utils.locators import YaScooterHomePageLocator


@allure.epic("Главная: FAQ")
@allure.suite("Аккордеон с вопросами/ответами")
class TestYaScooterFAQPage:

    @allure.feature("FAQ")
    @allure.title("Клик по вопросу раскрывает корректный ответ")
    @pytest.mark.parametrize(
        "question,answer,expected_answer",
        [
            (0, 0, YaScooterHomePageFAQ.answer1),
            (1, 1, YaScooterHomePageFAQ.answer2),
            (2, 2, YaScooterHomePageFAQ.answer3),
            (3, 3, YaScooterHomePageFAQ.answer4),
            (4, 4, YaScooterHomePageFAQ.answer5),
            (5, 5, YaScooterHomePageFAQ.answer6),
            (6, 6, YaScooterHomePageFAQ.answer7),
            (7, 7, YaScooterHomePageFAQ.answer8),
        ]
    )
    def test_faq_click_first_question_show_answer(self, driver, question, answer, expected_answer):
        page = YaScooterHomePage(driver)
        page.go_to_site()
        page.click_cookie_accept()
        page.click_faq_question(question_number=question)
        ans = page.find_element(YaScooterHomePageLocator.FAQ_ANSWER(answer_number=answer))

        assert ans.is_displayed() and ans.text == expected_answer, \
            "Текст ответа не соответствует ожидаемому"
