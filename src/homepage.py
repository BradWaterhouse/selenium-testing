from selenium import webdriver

def main():
    browser = webdriver.Chrome("/Users/bradWaterhouse/Downloads/chromedriver")

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })


    browser.get('https://www.bunches.co.uk')
    if browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/a/img').is_displayed():
        print('Pick of the day image exists')
        return True


if __name__ == '__main__':
    main()