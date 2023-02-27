from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """ Ожидает пока элемент станет виден """
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """ Ожидает пока все элементы станут видны """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_not_visible(self, locator, timeout=5):
        """ Ожидает пока не видимый элемент станет доступен """
        return wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def element_is_present(self, locator, timeout=5):
        """ Находит элемент в DOM дереве (для случаев если элемент не виден или скрыт)"""
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator, timeout=5):
        """ Ожидает пока элемент станет виден """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def element_is_clickable(self, locator, timeout=5):
        """ Ожидает пока кликабельный элемент станет доступен для клика """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """ Функция со скриптом для скролла к элементу """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def action_double_click(self, element):
        """ Функция делает двойной клик на элемент """
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element):
        """ Функция делает клик на элемент правой кнопкой """
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def remove_footer(self):
        """ Функция удаления элементов скриптом JS """
        self.driver.execute_script('document.querySelector("#app > footer").remove();')
        self.driver.execute_script('document.querySelector("#fixedban").remove();')

    def switch_to_new_tab_or_windows(self, element):
        """ Функция перевода фокуса на новую вкладку или окно """
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(element).text
        return text_title

    def switch_to_alert(self):
        """ Функция перевода фокуса на окно alert """
        alert_window = self.driver.switch_to.alert
        return alert_window

    def switch_to_frame(self, element):
        """ Функция перевода фокуса на frame """
        frame = self.driver.switch_to.frame(element)
        return frame

    def switch_to_default_content(self):
        """ Функция возвращения на дефолтное окно """
        self.driver.switch_to.default_content()

    def get_text_from_an_element(self, element):
        """ Функция получает текст элемента """
        text = self.element_is_present(element).text
        return text
