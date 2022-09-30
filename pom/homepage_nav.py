from base.base import SeleniumBase


class HomepageNav(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = "#nm-main-menu-ul>li"

    def get_nav_links(self):
        self.
