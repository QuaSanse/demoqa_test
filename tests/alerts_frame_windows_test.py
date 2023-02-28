import time

import allure

from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite('Alerts, Frame & Windows')
class TestAlertsFrameWindow:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        link_browser_windows = "https://demoqa.com/browser-windows"

        @allure.title('Checking the opening of a new tab')
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, self.link_browser_windows)
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page', "the new tab has not opened or an incorrect tab has opened"

        @allure.title('Checking the opening of a new window')
        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, self.link_browser_windows)
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_window()
            assert text_result == 'This is a sample page', "the new window has not opened or an incorrect window has opened"

    @allure.feature('Alerts Page')
    class TestAlertsPage:
        link_alerts = "https://demoqa.com/alerts"

        @allure.title('Checking the opening of an alert')
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, self.link_alerts)
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert did not show up"

        @allure.title('Checking the opening of the alert after 5 seconds')
        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, self.link_alerts)
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert did not show up"

        @allure.title('Checking the opening of the alert with confirm')
        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, self.link_alerts)
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok', "Alert did not show up"

        @allure.title('Checking the opening of the alert with prompt')
        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, self.link_alerts)
            alert_page.open()
            text, alert_text = alert_page.check_prompt_alert()
            assert text in alert_text, "Alert did not show up"

    @allure.feature('Frame Page')
    class TestFramesPage:
        link_frames = "https://demoqa.com/frames"

        @allure.title('Check the page with frames')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, self.link_frames)
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], 'The frame does not exist'
            assert result_frame2 == ['This is a sample page', '100px', '100px'], 'The frame does not exist'

    @allure.feature('Nested Page')
    class TestNestedFramesPage:
        link_nestedframes = "https://demoqa.com/nestedframes"

        @allure.title('Check the page with nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, self.link_nestedframes)
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    @allure.feature('Modal Dialog Page')
    class TestModalDialogsPage:
        link_modal_dialogs = "https://demoqa.com/modal-dialogs"

        @allure.title('Check the page with small modal dialogs')
        def test_modal_small_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, self.link_modal_dialogs)
            modal_dialogs_page.open()
            result_small = modal_dialogs_page.check_modal_small_dialogs()
            assert result_small == ['Small Modal', 47, 219, 298], 'The small dialogs does not exist'

        @allure.title('Check the page with large modal dialogs')
        def test_modal_large_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, self.link_modal_dialogs)
            modal_dialogs_page.open()
            result_large = modal_dialogs_page.check_modal_large_dialogs()
            assert result_large == ['Large Modal', 574, 331, 798], 'The large dialogs does not exist'
