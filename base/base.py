from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class SeleniumBase:

    def __int__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, 0.3)

    def __get_selenium_by(self, find_by: str):
        find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'name': By.NAME,
            'xpath': By.XPATH,
            'id': By.ID,
            'class_name': By.CLASS_NAME,
            'link_text': By.LINK_TEXT,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebDriverWait:
        return self.wait.until(ec.visibility_of_element_located((self.get_selenium_by(find_by), locator)))

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebDriverWait:
        return self.wait.until(ec.presence_of_element_located((self.get_selenium_by(find_by), locator)))

    def is_not_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebDriverWait:
        return self.wait.until(ec.invisibility_of_element_located((self.get_selenium_by(find_by), locator)))

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebDriverWait:
        return self.wait.until(ec.visibility_of_all_elements_located((self.get_selenium_by(find_by), locator)))

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> WebDriverWait:
        return self.wait.until(ec.presence_of_all_elements_located((self.get_selenium_by(find_by), locator)))

