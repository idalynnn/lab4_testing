from pages.contact_page import ContactPage

def test_contact_positive(driver):
    page = ContactPage(driver)
    page.open()

    page.fill_name("Лиза")
    page.fill_email("liza@123.com")
    page.fill_message("шалом")
    page.toggle_agree()
    page.submit()

    page.wait_visible(ContactPage.SUCCESS)
