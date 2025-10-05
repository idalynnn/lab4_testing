import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="session")
def driver():
    opts = Options()

    d = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                          options=opts)
    d.maximize_window()
    yield d
    d.quit()
