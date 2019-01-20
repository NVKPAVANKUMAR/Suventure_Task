from locators.Locators import Locator


class MoreScreen:

    def __init__(self, driver):
        self.driver = driver

    def click_more_icon(self):
        self.driver.find_element_by_xpath(Locator.more_icon).click()
