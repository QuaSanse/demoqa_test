from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import Base_page


class TextBoxPage(Base_page):
    locator = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locator.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locator.EMAIL).send_keys(email)
        self.element_is_visible(self.locator.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locator.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locator.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_is_present(self.locator.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locator.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locator.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locator.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address