# добавляем корень проекта в PYTHONPATH
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope="session")   # один браузер на всю сессию
def driver():
    opts = Options()
    # если нужно без окна: раскомментируй
    # opts.add_argument("--headless")

    # если Firefox установлен нестандартно, пропиши путь:
    # opts.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    d = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                          options=opts)
    d.maximize_window()
    yield d
    d.quit()
