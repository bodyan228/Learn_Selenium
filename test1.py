import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestSelenium(unittest.TestCase):

    def test_devops(self):
        driver = webdriver.Chrome(
            executable_path='./chromedriver.exe'
        )
        driver.get('https://ekaterinburg.hh.ru/')
        search_field = driver.find_element(By.NAME, 'text')
        search_field.send_keys('python developer')
        search_field.send_keys(Keys.RETURN)

        devops = driver.find_element(By.XPATH, '//*[@id="a11y-main-content"]/div[5]/div/div[1]/div[1]/div[3]/h3/span/a')
        devops.click()
        self.assertTrue("Python Developer" in driver.page_source)
        driver.close()

    def test_ural(self):
        driver = webdriver.Chrome(
            executable_path='./chromedriver.exe'
        )
        driver.get('https://ekaterinburg.hh.ru/')
        search_field = driver. \
            find_element(By.XPATH,
                         '//*[@id="HH-React-Root"]/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/button/span')
        search_field.click()
