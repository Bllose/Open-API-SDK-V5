from bllose.config.Config import class_config
from okx.TradingData_api import TradingDataAPI

@class_config
class blloseHttpOKE():
    def __init__(self, config):
        self.api_key = config['okx.Bllose.apiKey']
        self.secret_key = config['okx.Bllose.secretKey']
        self.passphrase = config['okx.Bllose.passphrase']
        self.flag = config['okx.Bllose.flag']

        self.tradingDataAPI = TradingDataAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)

    def get_taker_volume(self, ccy='BTC'):
        """
        <p>获取taker主动买入和卖出的交易量</p>
        <p>url: https://www.okx.com/docs-v5/zh/#trading-statistics-rest-api-get-taker-volume</p>
        @param ccy: 币种

        """
        result = self.tradingDataAPI.get_taker_volume(ccy='BTC', instType='SPOT')
        print(result)

if __name__ == '__main__':
    blloseHttpOKE().get_taker_volume()