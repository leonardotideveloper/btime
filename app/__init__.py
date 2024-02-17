from app.controller.price_controller import PriceController
from app.utils.webdriver_factory import WebDriverFactory


driver =  WebDriverFactory.create_driver()
controller = PriceController(driver)

def run():
    controller.main()