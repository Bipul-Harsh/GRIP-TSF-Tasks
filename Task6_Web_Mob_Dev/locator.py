from selenium.webdriver.common.by import By

class MainPageLocator(object):
    MAIN_HEADER = (By.CLASS_NAME, "navbar-brand")
    NAVBAR_LINKS = (By.CLASS_NAME, "dropdown-toggle")
    KNOW_MORE = (By.LINK_TEXT, "KNOW MORE")
    LEARN_MORE = (By.LINK_TEXT, "LEARN MORE")