from locator import *
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    
class MainPage(BasePage):
    def is_title_matches(self):
        return "The Sparks Foundation" in self.driver.title
    def is_header_matches(self):
        return ("The Sparks Foundation" in self.driver.find_element(*MainPageLocator.MAIN_HEADER).text
            and 
        "inspiring,innovating,integrating" in self.driver.find_element(*MainPageLocator.MAIN_HEADER).text)
    def check_know_more(self):
        self.driver.find_element(*MainPageLocator.KNOW_MORE).click()
    def check_learn_more(self):
        self.driver.find_element(*MainPageLocator.LEARN_MORE).click()

class SearchLinkPage(BasePage):
    def is_page_load(self):
        return "Page not yet Ready!" not in self.driver.find_element_by_tag_name("h3").text
