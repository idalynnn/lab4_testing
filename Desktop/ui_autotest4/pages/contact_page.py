from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    NAME      = (By.ID, "name")
    EMAIL     = (By.ID, "email")
    MESSAGE   = (By.ID, "message")
    AGREE     = (By.ID, "agree")
    SEND      = (By.ID, "send")
    SUCCESS   = (By.ID, "toast-success")
    RESULT = (By.ID, "result")

    ERR_NAME    = (By.ID, "err-name")
    ERR_EMAIL   = (By.ID, "err-email")
    ERR_MESSAGE = (By.ID, "err-message")
    ERR_AGREE   = (By.ID, "err-agree")

    def open(self):
        self.open_local("contact.html")

    def fill_name(self, text):    self.find(self.NAME).send_keys(text)
    def fill_email(self, text):   self.find(self.EMAIL).send_keys(text)
    def fill_message(self, text): self.find(self.MESSAGE).send_keys(text)
    def toggle_agree(self):       self.find(self.AGREE).click()
    def submit(self):             self.find(self.SEND).click()
