from locator import *
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):
    '''
    Creates link to web driver
    Arguments:
        - driver (selenium.webdriver.<browser>.webdriver.WebDriver) : driver to run the browser
    '''
    def __init__(self, driver):
        self.driver = driver
    
class MainPage(BasePage):
    def is_title_matches(self):
        '''
        Checks if The Sparks Foundation is present in page title
        '''
        return "The Sparks Foundation" in self.driver.title
    def is_header_matches(self):
        ''''
        Checks if brand name and brand tag line is present in header
        '''
        return ("The Sparks Foundation" in self.driver.find_element(*MainPageLocator.MAIN_HEADER).text
            and 
        "inspiring,innovating,integrating" in self.driver.find_element(*MainPageLocator.MAIN_HEADER).text)
    def check_know_more(self):
        '''
        Checks Know More button in main page
        '''
        self.driver.find_element(*MainPageLocator.KNOW_MORE).click()
    def check_learn_more(self):
        ''''
        Checks Learn More button in main page
        '''
        self.driver.find_element(*MainPageLocator.LEARN_MORE).click()
    def socials_link_check(self, link_index, error_line):
        '''
        Checks Social Link
        '''
        socials = self.driver.find_element(*MainPageLocator.SOCIAL_LINKS).find_elements_by_tag_name("a")
        parent_handle = self.driver.window_handles[0]
        socials[link_index].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        check = error_line not in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        return check

class SearchLinkPage(BasePage):
    def is_page_load(self):
        '''
        Checks is the link page successfully loaded
        '''
        return "Page not yet Ready!" not in self.driver.find_element_by_tag_name("h3").text
