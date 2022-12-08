import time, os
import requests
import fake_useragent
from colorama import Fore, Style, init

init()
# os.system("mode con cols=96 lines=60")

"""Style"""
R = '\x1b[31m'
G = '\x1b[32m'
B = '\x1b[34m'
W = '\x1b[37m'
Y = '\x1b[33m'
M = '\x1b[35m'
C = '\x1b[36m'
Bl= '\x1b[39m'

S_b = '\x1b[1m'
S_n = '\x1b[22m'

class P2parser:
    def __init__(self):
        self.available_data = {
            "action": ["BUY", "SELL"],
            "fiat" : None, 
            "asset": None, 
            "bank" : None, 
        }
        
    def all_fiat(self):
        
        data_fiat = self.__list_with_data('fiat')
        
        cookies = data_fiat[0]
        headers = data_fiat[1]
        
        response = requests.get('https://p2p.binance.com/bapi/fiat/v1/public/fiatpayment/menu/currency', cookies=cookies, headers=headers)
        
        response_json = response.json()
        
        favorite_currency = ["USD", "EUR", "UAH", "RUB", "JPY", "CNY", "GBP"]
        
        result_fiat = []
        
        temp = ""

        for item in response_json["data"]["currencyList"]:
            if item["name"] in favorite_currency:
                for f_c_i in range(len(favorite_currency)):
                    if favorite_currency[f_c_i] == item["name"]:
                        
                        """Sorted"""
                        try:
                            temp = result_fiat[f_c_i]
                            result_fiat.pop(f_c_i)
                            result_fiat.insert(f_c_i, item["name"])
                            result_fiat.append(temp)
                            break
                        except IndexError:
                            result_fiat.insert(f_c_i, item["name"])
            else:
                result_fiat.append(item["name"])
        
        self.available_data["fiat"] =  result_fiat 
        
        return self.available_data["fiat"]   
    
    @classmethod
    def __list_with_data(self, method, action="BUY", fiat="UAH", asset="USDT", bank="Monobank"):
        """method --> 'fiat', 'bank', """
        
        self.method = method
        
        self.action = action
        self.fiat = fiat
        self.asset = asset
        self.bank = bank
        
        
        cookies = {
            'cid': 'NVFN3uqS',
            'bnc-uuid': '6a10c4ff-d6bf-4f44-9584-f64e5c47f81a',
            'source': 'organic',
            'campaign': 'www.google.com',
            'sys_mob': 'no',
            '_gcl_au': '1.1.829176743.1667127504',
            'userPreferredCurrency': 'RUB_USD',
            'BNC_FV_KEY': '337cf71aac3ea65386d236e9e74b41dbade0eaf0',
            'fiat-prefer-currency': 'EUR',
            'videoViewed': 'yes',
            'common_fiat': self.fiat,
            '_gid': 'GA1.2.789651845.1669128700',
            'BNC_FV_KEY_EXPIRE': '1669150304344',
            'showBlockMarket': 'false',
            'OptanonAlertBoxClosed': '2022-11-22T15:09:47.696Z',
            'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0Mjg4YjA1NTliNTgtMDQ5MGU0MWUwZjRmOTMtMjYwMjFmNTEtMjA3MzYwMC0xODQyODhiMDU1YTljOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%7D',
            '_gat_UA-162512367-1': '1',
            '_ga': 'GA1.2.1691793685.1667127501',
            '_ga_3WP50LGEEC': 'GS1.1.1669144267.6.1.1669144277.50.0.0',
            'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Nov+22+2022+21%3A11%3A17+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=2f1b0d22-fb53-46ac-892a-f79486ffd0f8&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=NL%3BNH',
        }

        headers = {
            'authority': 'p2p.binance.com',
            'accept': '*/*',
            'accept-language': 'ru,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'bnc-uuid': '6a10c4ff-d6bf-4f44-9584-f64e5c47f81a',
            'c2ctype': 'c2c_merchant',
            'cache-control': 'no-cache',
            'clienttype': 'web',
            'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
            'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjkwMCwxNDQwIiwiYXZhaWxhYmxlX3NjcmVlbl9yZXNvbHV0aW9uIjoiODcwLDE0NDAiLCJzeXN0ZW1fdmVyc2lvbiI6IldpbmRvd3MgMTAiLCJicmFuZF9tb2RlbCI6InVua25vd24iLCJzeXN0ZW1fbGFuZyI6InJ1IiwidGltZXpvbmUiOiJHTVQrMiIsInRpbWV6b25lT2Zmc2V0IjotMTIwLCJ1c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNy4wLjAuMCBTYWZhcmkvNTM3LjM2IiwibGlzdF9wbHVnaW4iOiJQREYgVmlld2VyLENocm9tZSBQREYgVmlld2VyLENocm9taXVtIFBERiBWaWV3ZXIsTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlcixXZWJLaXQgYnVpbHQtaW4gUERGIiwiY2FudmFzX2NvZGUiOiIzNmJiNTZiOCIsIndlYmdsX3ZlbmRvciI6Ikdvb2dsZSBJbmMuIChBTUQpIiwid2ViZ2xfcmVuZGVyZXIiOiJBTkdMRSAoQU1ELCBSYWRlb24gUlggNTgwIFNlcmllcyBEaXJlY3QzRDExIHZzXzVfMCBwc181XzAsIEQzRDExKSIsImF1ZGlvIjoiMTI0LjA0MzQ3NTI3NTE2MDc0IiwicGxhdGZvcm0iOiJXaW4zMiIsIndlYl90aW1lem9uZSI6IkFmcmljYS9Ucmlwb2xpIiwiZGV2aWNlX25hbWUiOiJDaHJvbWUgVjEwNy4wLjAuMCAoV2luZG93cykiLCJmaW5nZXJwcmludCI6Ijc2YTRlYmY4OWUyNzk4NWIwMzNlZjMyZTVlMDI1OTZlIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiIn0=',
            'fvideo-id': '337cf71aac3ea65386d236e9e74b41dbade0eaf0',
            'lang': 'ru',
            'origin': 'https://p2p.binance.com',
            'pragma': 'no-cache',
            'referer': 'https://p2p.binance.com/trade/'+ self.bank +'/'+ self.asset +'?fiat=' + self.fiat,
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': fake_useragent.UserAgent().random,
            'x-trace-id': 'ecd92505-6ca3-4ddc-a011-fc6b16624512',
            'x-ui-request-trace': 'ecd92505-6ca3-4ddc-a011-fc6b16624512',
        }

        json_data = {
            'proMerchantAds': False,
            'page': 1,
            'rows': 10,
            'payTypes': [self.bank, ],
            'countries': [],
            'publisherType': None,
            'asset': self.asset,
            'fiat': self.fiat,
            'tradeType': self.action,
        }
        
        if self.method in "fiat":
            return [cookies, headers]
            


if __name__=="__main__":
    parsing = P2parser()
    
    
    
    print(parsing.all_fiat())
    
    