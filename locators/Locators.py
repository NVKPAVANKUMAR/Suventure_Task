class Locator:
    # Home Screen objects
    home_icon = "//android.widget.FrameLayout[@resource-id='com.climate.farmrise:id/action_home']"
    access_weather_detail_option = "//android.widget.RelativeLayout[@resource-id='com.climate.farmrise:id/checkWeatherView']"
    login_button_id = "MemberLoginForm_LoginForm_action_doLogin"
    more_icon = "//android.widget.FrameLayout[@resource-id='com.climate.farmrise:id/action_more']"

    #  Government Schemes Screen Objects
    weather_forecast_bar = "//android.widget.LinearLayout[@resource-id='com.climate.farmrise:id/hourlyWeatherForecastLayout']"
    current_time_icon = "//android.widget.LinearLayout[@index = '0']"
    last_time_icon = "//android.widget.LinearLayout[@index = '23']"
    time_text = "//android.widget.LinearLayout[@index = '23']/android.widget.TextView[@index='0']"

    # Government Schemes Screen objects
    government_schemes_option = "//android.widget.LinearLayout[@resource-id='com.climate.farmrise:id/more_govtSchemes']"
    load_moreschemes_button = "//android.widget.Button[@resource-id='com.climate.farmrise:id/loadMore']"
    search_icon = "//android.widget.ImageView[@content-desc='Search']"
    serachbox_input = "//android.widget.EditText[@resource-id='android:id/search_src_text']"
    schemes_list = "//android.widget.LinearLayout[@index='0']"
