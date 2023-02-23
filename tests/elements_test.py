import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage, ButtonsPage, LinksPage


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
            assert new_person in table_result, "the person was not found in the table"

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            print(key_word)
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has not been changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], \
                'The number of rows in the table has not been changed or has changed incorrectly'

    class TestButtonsPage:
        """ Проверки для страницы Buttons """

    def test_different_click_on_the_buttons(self, driver):
        button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        button_page.open()
        result = button_page.click_on_different_button()
        assert result['double_click'] == "You have done a double click", "The double click button was not pressed"
        assert result['right_click'] == "You have done a right click", "The right click button was not pressed"
        assert result['click'] == "You have done a dynamic click", "The dynamic click button was not pressed"

    class TestLinksPage:
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "the link is broken or url is incorrect"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400, "the link works or the status code in son 400"