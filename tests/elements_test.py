from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

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


