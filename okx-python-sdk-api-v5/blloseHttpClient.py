from bllose.config.Config import bConfig
import okx.Account_api as Account
import okx.Funding_api as Funding
import okx.Market_api as Market
import okx.Public_api as Public
import okx.Trade_api as Trade
import okx.status_api as Status
import okx.subAccount_api as SubAccount
import okx.TradingData_api as TradingData
import okx.Broker_api as Broker
import okx.Convert_api as Convert
import okx.FDBroker_api as FDBroker
import okx.Rfq_api as Rfq
import okx.TradingBot_api as TradingBot
import okx.Finance_api as Finance
import okx.Copytrading_api as Copytrading
import okx.Recurring_api as Recurring
import okx.SprdApi_api as Sprd

class blloseHttpOKE():
    @bConfig()
    def __init__(self, config):
        self.api_key = config['okx.Bllose.apiKey']
        self.secret_key = config['okx.Bllose.secretKey']
        self.passphrase = config['okx.Bllose.passphrase']
        self.flag = config['okx.Bllose.flag']

        self.accountAPI = Account.AccountAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.tradingDataAPI = TradingData.TradingDataAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.fundingAPI = Funding.FundingAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.convertAPI = Convert.ConvertAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.marketAPI = Market.MarketAPI(self.api_key, self.secret_key, self.passphrase, True, self.flag)
        self.publicAPI = Public.PublicAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.tradeAPI = Trade.TradeAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.sprdAPI = Sprd.SprdAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        # 子账户API subAccount
        self.subAccountAPI = SubAccount.SubAccountAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.brokerAPI = Broker.BrokerAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.fdBrokerAPI = FDBroker.FDBrokerAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        self.rfqAPI = Rfq.RfqAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        # 网格交易
        self.tradingBot = TradingBot.TradingBotAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        # 金融产品 Finance API
        self.finance = Finance.FinanceAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        # 跟单
        self.copytrading = Copytrading.CopytradingAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        # 定投
        self.recurring = Recurring.RecurringAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
        # 系统状态API(仅适用于实盘) system status
        self.status = Status.StatusAPI(self.api_key, self.secret_key, self.passphrase, False, self.flag)
    
    def get_support_coin(self) -> list:
        """
        <h1>获取所支持的币种类型列表</h1>
        Returns:
            coin_list(list): 支持的币种列表。币种简称PS:BTC;ETH;XCH...
        """
        response = self.tradingDataAPI.get_support_coin()
        if response['code'] == '0':
            return response['data']['contract']
        
    def get_taker_volume(self, ccy='BTC', instType='SPOT', 
                         begin:str = '', end:str = '', period:str = '') -> list:
        """
        <h1>获取主动买入/卖出情况</h1>
        <p>获取taker主动买入和卖出的交易量</p>
        Args:
            ccy(str): 币种
            instType(str): 产品类型 SP: SPOT 币币
            begin(str): 开始时间，Unix时间戳的毫秒数格式，如 1597026383085
            end(str): 结束时间，Unix时间戳的毫秒数格式，如 1597026383011
            period(str): 时间粒度，默认值5m。支持[5m/1H/1D]
        Returns:
            list(list): 交易记录列表
            - ts(str): 数据产生时间
            - sellVol(str): 卖出量
            - buyVol(str): 买入量
        """
        response = self.tradingDataAPI.get_taker_volume(
            ccy=ccy, instType=instType)
        if response['code'] == '0':
            return response['data']

if __name__ == '__main__':
    print(blloseHttpOKE().get_taker_volume())