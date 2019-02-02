from locators.Locators import Locator


class HomeScreen:
    def __init__(self, driver):
        self.driver = driver

    def click_home_button(self):
        self.driver.find_element_by_xpath(Locator.home_icon).click()

    def click_access_weather_detail_option(self):
        self.driver.find_element_by_xpath(Locator.access_weather_detail_option).click()

    def click_more_icon(self):
        self.driver.find_element_by_xpath(Locator.more_icon).click()