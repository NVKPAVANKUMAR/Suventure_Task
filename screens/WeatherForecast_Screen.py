import time

from locators.Locators import Locator


class WeatherForecastScreen:

    def __init__(self, driver):
        self.driver = driver

    def click_weather_forecast_bar(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(Locator.weather_forecast_bar).click()

    def scroll_to_lasttimeelement(self):
        self.driver.scroll(Locator.current_time_icon, Locator.last_time_icon)

    def get_time_text(self):
        return self.driver.find_element_by_xpath(Locator.time_text).text()
