import unittest
from datetime import datetime, timedelta
from time import sleep

from appium import webdriver

from screens.Government_Schemes_Screen import GovernmentSchemesScreen
from screens.Home_Screen import HomeScreen
from screens.More_Screen import MoreScreen
from screens.WeatherForecast_Screen import WeatherForecastScreen


def get_custom_time():
    twenty_three_hours_from_now = datetime.now() + timedelta(hours=23)
    return '{:%I %p}'.format(twenty_three_hours_from_now)


class FarmRiseAndroidTests(unittest.TestCase):

    def setUp(self):
        """Setup for the test"""
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '8.0',
                        'deviceName': 'P8B4C18105007441',
                        'noReset': 'true',
                        'appPackage': 'com.climate.farmrise',
                        'appActivity': 'com.climate.farmrise.base.FarmriseHomeActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        """Tear down the test"""
        self.driver.quit()

    def scrollToElement(self, exact_text):
        self.driver.find_element_by_android_uiautomator(
            "new UiScrollable(new UiSelector()).scrollIntoView(text(\"" + exact_text + "\")).click()")

    def test_timing_AccessWeatherDetails(self):
        home_screen = HomeScreen(self.driver)
        home_screen.click_home_button()
        sleep(2)
        home_screen.click_access_weather_detail_option()
        weather_screen = WeatherForecastScreen(self.driver)
        weather_screen.click_weather_forecast_bar()
        weather_screen.scroll_to_lasttimeelement()
        time_value = weather_screen.get_time_text()
        self.assertEqual(get_custom_time(), time_value, "Assertion Failure")

    def test_government_schemes_screen(self):
        more_screen = MoreScreen(self.driver)
        more_screen.click_more_icon()
        government_schemes_screen = GovernmentSchemesScreen(self.driver)
        government_schemes_screen.click_governmentschemes_option()
        self.scrollToElement("LOAD MORE SCHEMES")
        sleep(5)
        self.assertTrue(government_schemes_screen.get_loadmore_button_status())
        government_schemes_screen.click_search_icon()
        government_schemes_screen.input_search("schemes")
        government_schemes_screen.submit_search()
        self.assertTrue(government_schemes_screen.get_schemes_list_status())


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FarmRiseAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
