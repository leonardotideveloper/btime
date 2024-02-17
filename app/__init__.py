from app.controller.price_controller import CotacaoController
from app.utils.webdriver_factory import WebDriverFactory


driver =  WebDriverFactory.create_driver()
controller = CotacaoController(driver)

def run():
    controller.main()