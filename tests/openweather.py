from weather import openweather

def test_openweather():
    """
    Calls OpenWeather API
    """
    weather.get_weather("d4afb596768c77e175bb8136037eed6a", "seattle", "us")
