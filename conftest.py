import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(scope="session", autouse=True)
def _clean_before_session():
    for path in (".pytest_cache", "allure_results"):
        if os.path.isdir(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    try:
                        os.remove(os.path.join(root, name))
                    except Exception:
                        pass
                for name in dirs:
                    try:
                        os.rmdir(os.path.join(root, name))
                    except Exception:
                        pass
            try:
                os.rmdir(path)
            except Exception:
                pass


@pytest.fixture()
def driver():
    options = FirefoxOptions()
    options.add_argument("--headless")         
    options.set_preference("dom.webnotifications.enabled", False)
    options.page_load_strategy = "normal"

    service = FirefoxService() 

    drv = webdriver.Firefox(options=options, service=service)
    drv.set_window_size(1400, 1000)
    yield drv
    drv.quit()
