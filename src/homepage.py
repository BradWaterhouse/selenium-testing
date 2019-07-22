from selenium import webdriver
import unittest


class TestStringMethods(unittest.TestCase):

    browser = webdriver.Chrome("/Users/bradWaterhouse/Downloads/chromedriver")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })

    def test_pick_of_the_day(self):
        browser = webdriver.Chrome("/Users/bradWaterhouse/Downloads/chromedriver")
        browser.get('https://www.bunches.co.uk')
        self.assertTrue(browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/a/img').is_displayed())

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
