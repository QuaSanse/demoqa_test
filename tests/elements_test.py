import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


class TestElements:
    class TestTextBox:
        """ Проверки для страницы Text Box """

        def test_text_box(self, driver):
            url = 'https://demoqa.com/text-box'
            text_box_page = TextBoxPage(driver, url)
            text_box_page.open()
            in_full_name, in_email, in_cur_addr, in_per_addr = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            assert in_full_name == output_name, "Не совпадает полное имя"
            assert in_email == output_email, "Не совпадает email"
            assert in_cur_addr == output_cur_addr, "Не совпадает current address"
            assert in_per_addr == output_per_addr, "Не совпадает permanent address"

    class TestCheckBox:
        """ Проверки для страницы Check Box """

        def test_check_box(self, driver):
            url = 'https://demoqa.com/checkbox'
            check_box_page = CheckBoxPage(driver, url)
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()

            assert input_checkbox == output_result, 'Checkboxes have not selected'

    class TestRadioButton:
        """ Проверки для страницы Radio Box """

        def test_radio_button(self, driver):
            url = 'https://demoqa.com/radio-button'
            radio_box_page = RadioButtonPage(driver, url)
            radio_box_page.open()
            radio_box_page.click_on_the_radio_button('yes')
            output_yes = radio_box_page.get_output_result()
            radio_box_page.click_on_the_radio_button('impressive')
            output_impressive = radio_box_page.get_output_result()
            radio_box_page.click_on_the_radio_button('no')
            output_no = radio_box_page.get_output_result()

            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == "No", "'No' have not been selected"

    class TestWebTables:
        """ Проверки для страницы Web Tables """

        def test_web_table_add_person(self, driver):
            url = 'https://demoqa.com/webtables'
            web_tables_page = WebTablesPage(driver, url)
            web_tables_page.open()
            new_person = web_tables_page.add_new_person(2)
            table_result = web_tables_page.check_new_added_person()
            time.sleep(3)
            assert new_person in table_result, "the person was not found in the table"

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in the table"
