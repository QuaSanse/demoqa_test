import random
import time

import allure
from selenium.common.exceptions import UnexpectedAlertPresentException

from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('check opened new tab ')
    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        text_result = self.switch_to_new_tab_or_windows(self.locators.TITLE_NEW)
        return text_result

    @allure.step('check opened new window')
    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        text_result = self.switch_to_new_tab_or_windows(self.locators.TITLE_NEW)
        return text_result


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('get text from alert')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    @allure.step('check alert appear after 5 sec')
    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        try:
            return self.switch_to_alert().text
        except UnexpectedAlertPresentException:
            return self.switch_to_alert().text

    @allure.step('check confirm alert')
    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        self.switch_to_alert().accept()
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    @allure.step('check prompt alert')
    def check_prompt_alert(self):
        text = f"autotest{random.randint(0, 999)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('check frame')
    def check_frame(self, frame_num):
        text, width, height = None, None, None
        if frame_num == 'frame1':
            text, width, height = self.get_data_frame(self.element_is_present(self.locators.FIRST_FRAME))
        if frame_num == 'frame2':
            text, width, height = self.get_data_frame(self.element_is_present(self.locators.SECOND_FRAME))
        return [text, width, height]

    def get_data_frame(self, element):
        frame = element
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.switch_to_frame(frame)
        text = self.get_text_from_an_element(self.locators.TITLE_FRAME)
        self.switch_to_default_content()
        return text, width, height


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.get_text_from_an_element(self.locators.PARENT_TEXT)
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.get_text_from_an_element(self.locators.CHILD_TEXT)
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('check modal small dialogs')
    def check_modal_small_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        height_modal_small_window = self.get_properties_element(self.locators.SMALL_MODAL_WINDOW, 'clientHeight')
        width_modal_small_window = self.get_properties_element(self.locators.SMALL_MODAL_WINDOW, 'clientWidth')
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        return [title_small, len(body_small_text), height_modal_small_window, width_modal_small_window, ]

    @allure.step('check modal large dialogs')
    def check_modal_large_dialogs(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        height_modal_large_window = self.get_properties_element(self.locators.SMALL_MODAL_WINDOW, 'clientHeight')
        width_modal_large_window = self.get_properties_element(self.locators.SMALL_MODAL_WINDOW, 'clientWidth')
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.BODY_LARGE_MODAL).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return [title_large, len(body_large_text), height_modal_large_window, width_modal_large_window, ]
