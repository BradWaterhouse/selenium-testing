from selenium import webdriver
import unittest

browser = webdriver.Chrome("/Users/bradWaterhouse/Downloads/chromedriver")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})


class TestStringMethods(unittest.TestCase):

    def test_page_has_rendered_correctly(self):
        chrome_options.add_experimental_option("detach", True)
        browser.get('https://www.bunches.co.uk')

        self.assertTrue(browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/a/img').is_displayed())
        self.assertTrue(browser.find_element_by_xpath('// *[ @ id = "navigation-menu"] / li[1] / div / a').is_displayed())


if __name__ == '__main__':
    unittest.main()
