from selenium import webdriver
import unittest
import page
import time

class SearchSparkWeb(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.thesparksfoundationsingapore.org')
        self.search_result_page = page.SearchLinkPage(self.driver)

    def test_1_MainPage(self):
        print("Main Page")
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        print("Title Checked")
        assert mainPage.is_header_matches()
        print("Header Checked")
        mainPage.check_know_more()
        assert self.search_result_page.is_page_load()
        self.driver.back()
        print("Know More Checked")
        mainPage.check_learn_more()
        assert self.search_result_page.is_page_load()      
        print("Learn More Checked")
        print("-------------------")
        print("Socials Link Check")
        print("-------------------")
        socials = self.driver.find_element_by_class_name("top-header-agile-right").find_elements_by_tag_name("a")
        parent_handle = self.driver.window_handles[0]
        socials[0].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "This page isn't available" not in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        print("Facebook Link Checked")
        socials[1].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "This page is not availabe" not in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        print("Linked Link Checked")
        socials[2].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "Page Not Found" not in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        print("Medium Link Checked")
        socials[3].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "This account doesn't exist" not in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        print("Twitter Link Checked")
        socials[4].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "This site can't be reached" not in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        print("Website Link Checked")
        socials[5].click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "Sorry, this page isn't available." not in self.driver.page_source
        self.driver.close()
        self.driver.switch_to.window(parent_handle)
        print("Instagram Link Checked")
        print("----------------")
        print("Page Check")
        print("-----------------")
        self.driver.find_elements_by_class_name("dropdown-toggle")[0].click()
        self.driver.find_elements_by_class_name("dropdown-menu")[0].click()
        assert self.search_result_page.is_page_load()
        print("About Page Checked")
        self.driver.back()
        self.driver.find_elements_by_class_name("dropdown-toggle")[1].click()
        self.driver.find_elements_by_class_name("dropdown-menu")[1].click()
        assert self.search_result_page.is_page_load()
        print("Policies Page Checked")
        self.driver.back()
        self.driver.find_elements_by_class_name("dropdown-toggle")[2].click()
        self.driver.find_elements_by_class_name("dropdown-menu")[2].click()
        assert self.search_result_page.is_page_load()
        print("Programs Page Checked")
        self.driver.back()
        self.driver.find_elements_by_class_name("dropdown-toggle")[3].click()
        self.driver.find_elements_by_class_name("dropdown-menu")[3].click()
        assert self.search_result_page.is_page_load()
        print("Links Page Checked")
        self.driver.back()
        self.driver.find_elements_by_class_name("dropdown-toggle")[4].click()
        self.driver.find_elements_by_class_name("dropdown-menu")[4].click()
        assert self.search_result_page.is_page_load()
        print("Join Us Page Checked")
        self.driver.back()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()