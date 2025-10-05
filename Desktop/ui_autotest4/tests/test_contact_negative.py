from pages.contact_page import ContactPage

def test_contact_empty_email(driver):
    page = ContactPage(driver)
    page.open()

    page.fill_name("Лиза")
    page.fill_message("привет")
    page.toggle_agree()
    page.submit()

    assert "Некорректный email" in page.get_result_message()
