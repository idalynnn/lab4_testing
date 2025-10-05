from pathlib import Path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=5):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_local(self, filename: str):
        page = Path(__file__).resolve().parents[1] / filename
        self.driver.get(page.as_uri())

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def get_result_message(self):
        return self.find(*self.RESULT).text
