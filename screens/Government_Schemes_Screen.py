from locators.Locators import Locator


class GovernmentSchemesScreen:

    def __init__(self, driver):
        self.driver = driver

    def click_governmentschemes_option(self):
        self.driver.find_element_by_xpath(Locator.government_schemes_option).click()

    def get_loadmore_button_status(self):
        return self.driver.find_element_by_xpath(Locator.load_moreschemes_button).size != 0

    def click_search_icon(self):
        self.driver.find_element_by_xpath(Locator.search_icon).click()

    def input_search(self, texttoenter):
        self.driver.find_element_by_xpath(Locator.serachbox_input(texttoenter)).send_keys("schemes")

    def submit_search(self):
        self.driver.find_element_by_xpath(Locator.serachbox_input).submit()

    def get_schemes_list_status(self):
        return self.driver.find_element_by_xpath(Locator.schemes_list).size != 0
