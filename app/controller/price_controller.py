import csv

from app.utils.log import log_wrapper
from app.entities.price_actions import PriceActions
from selenium.common.exceptions import TimeoutException
from json import loads

class PriceController:
    def __init__(self, driver):
        self.driver = driver
    @log_wrapper
    def close(self):
        self.driver.quit()

    @log_wrapper
    def get(self):
        url = 'https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/cotacoes/'
        self.driver.get(url)

    @log_wrapper
    def write_to_csv(self, data, file_name):
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=PriceActions.__annotations__.keys())
            writer.writeheader()

            for item in data:
                writer.writerow(item.__dict__)

    @log_wrapper 
    def fetch_data(self, key):
        try:
            request = self.driver.wait_for_request('api/v1/InstrumentPriceFluctuation/ibov', timeout=10)    
            body = loads(request.response.body.decode('utf-8'))[key]
            data = []
            for item in body:
                data.append(
                    PriceActions(
                        price=float(item['SctyQtn']['curPrc']),
                        price_fluctuation=round(float(item['SctyQtn']['prcFlcn']), 2),
                        name=item['symb'],
                        description=item['desc']
                    )
                )
            return data
        
        except TimeoutException:
            raise 'Request timed out'

        except Exception as error:
            raise error
        
    def main(self):
        self.get()
        high_price = self.fetch_data(key='SctyHghstIncrLst')
        self.write_to_csv(high_price, 'high_price.csv')

        low_price = self.fetch_data(key='SctyHghstDrpLst')
        self.write_to_csv(low_price, 'low_price.csv')

        self.close()