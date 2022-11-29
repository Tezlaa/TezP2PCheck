import time, os
import requests
import fake_useragent
from colorama import Fore, Style, init

init()
os.system("mode con cols=96 lines=60")

"""Style"""
R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.WHITE
Y = Fore.YELLOW
M = Fore.MAGENTA
C = Fore.CYAN
Bl= Fore.BLACK

S_b = Style.BRIGHT
S_n = Style.NORMAL

class Check_p2p_offers():
    def __init__(self, action, fiat, asset, bank):
        self.action = action
        self.fiat = fiat
        self.asset = asset
        self.bank = bank
        self.result_exchange_rate = []
        self.counter = 0
        self.request_text = self.get_response()
    
    def get_response(self):
        
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
            'payTypes': [
                self.bank,
            ],
            'countries': [],
            'publisherType': None,
            'asset': self.asset,
            'fiat': self.fiat,
            'tradeType': self.action,
        }
        

        print(G + S_n + "\n\n Loading..." + W + S_b); time.sleep(1.0) #Processing a request
        return requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', cookies=cookies, headers=headers, json=json_data).text

        
    def exchange_rate(self, request_text, to_start_word=None, to_start_min_trans=None, to_start_max_trans=None):
        
        word = request_text.find('price":"', to_start_word) + 8    #indent to price
        min_trans = request_text.find('minSingleTransAmount":"', to_start_min_trans) + 23    #indent to max trans this account
        max_trans = request_text.find('maxSingleTransAmount":"', to_start_max_trans) + 23
        
        result_word      = ""      #to add characters
        result_max_trans = "" 
        result_min_trans = ""
        
        if self.counter < 9 :   #how many offers
            for i in range(100):
                if request_text[word + i] != '"':   #example: "133.23 '"'<- to last char
                    to_start_for_word = word + i 
                    result_word += request_text[to_start_for_word]
                else:     
                    break
            for i in range(100):
                if request_text[min_trans + i] != '.':
                    to_start_for_mintr = min_trans + i
                    result_min_trans += request_text[to_start_for_mintr]
                else:
                    break
            for i in range(100):
                if request_text[max_trans + i] != '.':
                    to_start_for_maxtr = max_trans + i
                    result_max_trans += request_text[to_start_for_maxtr]
                else:
                    break
            
            self.counter += 1        
            
            self.result_exchange_rate.append([[result_word], [result_min_trans], [result_max_trans]])   #add in list with result     
            
            self.exchange_rate(self.request_text ,to_start_for_word, to_start_for_mintr, to_start_for_maxtr)   #recursive from an index that is checked

        
    def return_result(self):
        self.exchange_rate(self.request_text)
        return self.result_exchange_rate


def get_available_fiat():
    
    user = fake_useragent.UserAgent().random
    
    cookies = {
        'cid': 'N6JmU0Mq',
        'cid': '2v7KWpDw',
        'bnc-uuid': '6a10c4ff-d6bf-4f44-9584-f64e5c47f81a',
        'source': 'organic',
        'campaign': 'www.google.com',
        'sys_mob': 'no',
        '_gcl_au': '1.1.829176743.1667127504',
        'userPreferredCurrency': 'RUB_USD',
        'BNC_FV_KEY': '337cf71aac3ea65386d236e9e74b41dbade0eaf0',
        'fiat-prefer-currency': 'EUR',
        'videoViewed': 'yes',
        'OptanonAlertBoxClosed': '2022-11-22T15:09:47.696Z',
        'showBlockMarket': 'false',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0Mjg4YjA1NTliNTgtMDQ5MGU0MWUwZjRmOTMtMjYwMjFmNTEtMjA3MzYwMC0xODQyODhiMDU1YTljOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%7D',
        '_gid': 'GA1.2.157651800.1669556840',
        'BNC_FV_KEY_EXPIRE': '1669678516781',
        'common_fiat': 'UAH',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Nov+28+2022+20%3A33%3A00+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=2f1b0d22-fb53-46ac-892a-f79486ffd0f8&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=NL%3BNH',
        '_gat_UA-162512367-1': '1',
        '_ga_3WP50LGEEC': 'GS1.1.1669660360.17.1.1669660390.30.0.0',
        '_ga': 'GA1.1.1691793685.1667127501',
    }

    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'bnc-location': 'null',
        'bnc-uuid': '6a10c4ff-d6bf-4f44-9584-f64e5c47f81a',
        'cache-control': 'no-cache',
        'clienttype': 'web',
        'content-type': 'application/json',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA1MCIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUiLCJ0aW1lem9uZSI6IkdNVCsyIiwidGltZXpvbmVPZmZzZXQiOi0xMjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA3LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6IjM2YmI1NmI4Iiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKEFNRCkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChBTUQsIFJhZGVvbiBSWCA1ODAgU2VyaWVzIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiQWZyaWNhL1RyaXBvbGkiLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWMTA3LjAuMC4wIChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiNzlhZjg4YzZlYzExYzkzY2Y5ODlkNDU3M2RiZDYwY2QiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIifQ==',
        'fvideo-id': '337cf71aac3ea65386d236e9e74b41dbade0eaf0',
        'lang': 'ru',
        'pragma': 'no-cache',
        'referer': 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=UAH',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-trace-id': '2242937d-a8b8-4696-97f2-dfd7758732fb',
        'x-ui-request-trace': '2242937d-a8b8-4696-97f2-dfd7758732fb',
    }

    response = requests.get('https://p2p.binance.com/bapi/fiat/v1/public/fiatpayment/menu/currency', cookies=cookies, headers=headers).text

    favorite_currency = ["USD", "EUR", "UAH", "RUB", "JPY", "CNY", "GBP"]
    
    word_with_fiat = ""
    result_fiat = []

    index_last_char = 0

    search = True
    while search == True:
        find_with_response = response.find('"name":"', index_last_char) + 8
        
        word_with_fiat = ""
        
        for i in range(5):
            if response[find_with_response + i] != ":":
                if response[find_with_response + i] != '"':
                    word_with_fiat += response[find_with_response + i]
                else:
                    if word_with_fiat not in favorite_currency:
                        result_fiat.insert(-1, word_with_fiat)
                    else:
                        result_fiat.insert(0, word_with_fiat)
                        
                    index_last_char = find_with_response + i
                    break
            else:
                result_fiat.pop(-1)
                search = False
                break
        
    return result_fiat

def get_bank_for_currency(fiat):
    
    user = fake_useragent.UserAgent().random
    
    cookies = {
        'cid': 'SUBOzm5y',
        'bnc-uuid': '6a10c4ff-d6bf-4f44-9584-f64e5c47f81a',
        'source': 'organic',
        'campaign': 'www.google.com',
        'sys_mob': 'no',
        '_gcl_au': '1.1.829176743.1667127504',
        'userPreferredCurrency': 'RUB_USD',
        'BNC_FV_KEY': '337cf71aac3ea65386d236e9e74b41dbade0eaf0',
        'fiat-prefer-currency': 'EUR',
        'videoViewed': 'yes',
        'OptanonAlertBoxClosed': '2022-11-22T15:09:47.696Z',
        '_gid': 'GA1.2.157651800.1669556840',
        'BNC_FV_KEY_EXPIRE': '1669758317689',
        'showBlockMarket': 'false',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Tue+Nov+29+2022+17%3A48%3A13+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=2f1b0d22-fb53-46ac-892a-f79486ffd0f8&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=NL%3BNH',
        '_gat_UA-162512367-1': '1',
        '_ga_3WP50LGEEC': 'GS1.1.1669736716.19.1.1669736899.52.0.0',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0Mjg4YjA1NTliNTgtMDQ5MGU0MWUwZjRmOTMtMjYwMjFmNTEtMjA3MzYwMC0xODQyODhiMDU1YTljOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%7D',
        'common_fiat': 'RUB',
        '_ga': 'GA1.2.1691793685.1667127501',
    }

    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'ru,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'bnc-uuid': '6a10c4ff-d6bf-4f44-9584-f64e5c47f81a',
        'c2ctype': 'c2c_merchant',
        'cache-control': 'no-cache',
        'clienttype': 'web',
        'content-type': 'application/json',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA1MCIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoicnUiLCJ0aW1lem9uZSI6IkdNVCsyIiwidGltZXpvbmVPZmZzZXQiOi0xMjAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTA3LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6IjM2YmI1NmI4Iiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKEFNRCkiLCJ3ZWJnbF9yZW5kZXJlciI6IkFOR0xFIChBTUQsIFJhZGVvbiBSWCA1ODAgU2VyaWVzIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiQWZyaWNhL1RyaXBvbGkiLCJkZXZpY2VfbmFtZSI6IkNocm9tZSBWMTA3LjAuMC4wIChXaW5kb3dzKSIsImZpbmdlcnByaW50IjoiNzlhZjg4YzZlYzExYzkzY2Y5ODlkNDU3M2RiZDYwY2QiLCJkZXZpY2VfaWQiOiIiLCJyZWxhdGVkX2RldmljZV9pZHMiOiIifQ==',
        'fvideo-id': '337cf71aac3ea65386d236e9e74b41dbade0eaf0',
        'lang': 'ru',
        'origin': 'https://p2p.binance.com',
        'pragma': 'no-cache',
        'referer': 'https://p2p.binance.com/ru/trade/all-payments/USDT?fiat=RUB',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-trace-id': '1080c5f1-8f51-4ff3-aab7-78911ff5dbaf',
        'x-ui-request-trace': '1080c5f1-8f51-4ff3-aab7-78911ff5dbaf',
    }

        
    data = {
        'fiat': fiat,
    }
    
    response = requests.post('https://p2p.binance.com/bapi/c2c/v2/public/c2c/adv/filter-conditions', cookies=cookies, headers=headers, json=data).text
    
    banks = []
    index_last_char = 0
    
    search = True
    while search == True:
        find_with_response = response.find('"tradeMethodName":"', index_last_char) + 19
        
        word_with_bank = ""
        
        for i in range(100):
            if response[find_with_response + i] != '"':
                word_with_bank += response[find_with_response + i]
            else:
                banks.append(word_with_bank)
                index_last_char = find_with_response + i
                
                break
            
        if (banks[-1] == "message"):
            banks.pop(-1)
        
            search = False

    return banks

        
def write_available_chouice(select):
    """
    write action(buy or sell)--> 'action'
    
    write fiat--> 'fiat'
    
    write asset--> 'asset'
    
    write bank--> 'bank'
    """
    
    if select == "action":
        print( "_" * 96 + "\n")
        
        for i in range(len(available_data["action"])):
            if i == 0:
                print(f' {1}-{G + available_data["action"][i] + W}', end=" ")
            else:
                print(f' {2}-{R + available_data["action"][i] + W}', end=" ")
            
        print("\n")
    
    if select == "fiat":
        print("_" * 96 + "\n")
        
        favorite_currency = ["USD", "EUR", "UAH", "RUB", "JPY", "CNY", "GBP"]
        
        for i in range(len(available_data["fiat"])):
            if i < 7:
                print(f' {i+1}-{G + available_data["fiat"][i] + W}', end="  ")
                if i == 6:
                    print("\n" + (S_n + Bl) + "_" * 96)
            else:
                print(f'{S_n + Bl}{i+1}-{G + available_data["fiat"][i]}', end=" ")
        
        print("\n" + (W + S_b))
    if select == "asset":
        print("_" * 96 + "\n")
        
        for i in range(len(available_data["asset"])):
            print(f' {i+1}-{G + available_data["asset"][i] + W}', end=" ")
            
        print("\n")
    if select == "bank":
        print("_" * 96 + "\n")
        
        for i in range(len(available_data["bank"])):
            print(f' {i+1}-{G + available_data["bank"][i] + W}', end="\n")
            
        print("\n")

def user_сhoice():
    
    write_available_chouice("action")
    select_action = int(input(" Select an action: ")) - 1
    
    write_available_chouice("fiat")
    select_fiat = int(input(" Select the fiat to be parsed: ")) - 1
    
    available_data['bank'] = get_bank_for_currency(available_data['fiat'][select_fiat])  #adding a bank of fiat selections
    
    write_available_chouice("asset")
    select_asset = int(input(" Select the asset to be parsed: ")) - 1
    
    write_available_chouice("bank")
    select_bank = int(input(" Select the bank to be parsed: ")) - 1 
    
    selected = [available_data["action"][select_action], available_data["fiat"][select_fiat], available_data["asset"][select_asset], available_data["bank"][select_bank]]    #place the selected item on the list to return
    return selected     #returns a list with the selected 

def print_offers(list_with_result, list_with_data):
    action  = list_with_data[0]
    fiat = list_with_data[1]
    asset  = list_with_data[2]
    bank = list_with_data[3]
    
    os.system('cls||clear')
    
    print(M + "\n" + "_" * 96 + "\n\n" + W)
    
    for i in range(len(list_with_result)):
        if action == "BUY":
            print(f' {S_n}{i + 1}){S_b} {G + action + W} Offer: {C}1-{asset + W} = {M}{", ".join(map(str, list_with_result[i][0]))} {G + fiat + W} {B}\t|{S_n + W} {", ".join(map(str, list_with_result[i][1]))} - {Y + ", ".join(map(str, list_with_result[i][2])) + W} {G + fiat + W + S_b}')
        else:
            print(f' {S_n}{i + 1}){S_b} {R + action + W} Offer: {C}1-{asset + W} = {M}{", ".join(map(str, list_with_result[i][0]))} {G + fiat + W} {B}\t|{S_n + W} {", ".join(map(str, list_with_result[i][1]))} - {", ".join(map(str, list_with_result[i][2]))} {G + fiat + W + S_b}')
    
    print(M + "\n" + "_" * 96 + W)
  
if __name__=="__main__":
    print(S_b)
    
    all_fiat = get_available_fiat()
    
    cycle_menu = True
    while cycle_menu == True:
        available_data = {
            "action": ["BUY", "SELL"],
            "fiat" : all_fiat, 
            "asset": ["USDT", "BTC", "BUSD", "BNB", "ETH", "UAH", "SHIB", ], 
            "bank" : None, 
        }
        
        os.system('cls||clear')
        
        print(f'''{M}
    ╭
    ████████╗███████╗███████╗██████╗░██████╗░██████╗░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
    ╚══██╔══╝██╔════╝╚════██║██╔══██╗╚════██╗██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
    ░░░██║░░░█████╗░░░░███╔═╝██████╔╝░░███╔═╝██████╔╝██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
    ░░░██║░░░██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░██╔═══╝░██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
    ░░░██║░░░███████╗███████╗██║░░░░░███████╗██║░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
    ░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
    {W}''')
        
        user_selected = user_сhoice() 
        
        parsing = Check_p2p_offers(user_selected[0], user_selected[1], user_selected[2], user_selected[3]) #put all the selected items into a class for parsing 
        
        print_offers(parsing.return_result(), user_selected)
        
        input(f'\n\n{R}  EXIT IN MENU {Bl}(type any key){W}')
