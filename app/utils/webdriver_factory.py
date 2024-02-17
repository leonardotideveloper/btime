from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class WebDriverFactory:
    @staticmethod
    def create_driver():
        options = Options()
        options.add_argument('--disable-logging')
        options.add_argument("--log-level=3")
        options.add_argument("--headless")        

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)

        return driver