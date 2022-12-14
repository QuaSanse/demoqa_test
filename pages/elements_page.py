import time
import random

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import Base_page


class TextBoxPage(Base_page):
    """ Класс для страницы Text Box """
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        """ Функция заполнения полей формы Text Box """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        """ Функция возвращает результат заполнения полей формы Text Box """
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(Base_page):
    """ Класс для страницы Check Box """
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        """ Функция раскрытия всех CheckBox для формы Check Box """
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        """ Функция случайных кликов по CheckBox для формы Check Box """
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        """ Функция возвращает массив (List) с текстом выбранных элементов """
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            # .find_element_by_xpath(). В обновлении Selenium до version 4.3.0 метод удалили, теперь надо использовать .find_element("xpath", locator)
            title_item = box.find_element("xpath", self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        """ Функция возвращает массив (List) с результатом текстов для выбранных элементов """
        output_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in output_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(Base_page):
    """ Класс для страницы Radio Button """
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        """ Функция кликов на каждый Radio Button """
        choices = {
            'yes': self.locators.YES_RADIOBUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIOBUTTON,
            'no': self.locators.NO_RADIOBUTTON
        }
        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        """ Функция возвращает текст результата на нажатый Radio Button """
        return self.element_is_present(self.locators.OUTPUT_RESULT).text
