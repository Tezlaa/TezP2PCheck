import requests

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
    # Requests sorts cookies= alphabetically
    # 'cookie': 'cid=N6JmU0Mq; cid=2v7KWpDw; bnc-uuid=6a10c4ff-d6bf-4f44-9584-f64e5c47f81a; source=organic; campaign=www.google.com; sys_mob=no; _gcl_au=1.1.829176743.1667127504; userPreferredCurrency=RUB_USD; BNC_FV_KEY=337cf71aac3ea65386d236e9e74b41dbade0eaf0; fiat-prefer-currency=EUR; videoViewed=yes; OptanonAlertBoxClosed=2022-11-22T15:09:47.696Z; showBlockMarket=false; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg0Mjg4YjA1NTliNTgtMDQ5MGU0MWUwZjRmOTMtMjYwMjFmNTEtMjA3MzYwMC0xODQyODhiMDU1YTljOCJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22184288b0559b58-0490e41e0f4f93-26021f51-2073600-184288b055a9c8%22%7D; _gid=GA1.2.157651800.1669556840; BNC_FV_KEY_EXPIRE=1669678516781; common_fiat=UAH; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Nov+28+2022+20%3A33%3A00+GMT%2B0200+(%D0%92%D0%BE%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B0%D1%8F+%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D0%B0%2C+%D1%81%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82%D0%BD%D0%BE%D0%B5+%D0%B2%D1%80%D0%B5%D0%BC%D1%8F)&version=6.34.0&isIABGlobal=false&hosts=&consentId=2f1b0d22-fb53-46ac-892a-f79486ffd0f8&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&geolocation=NL%3BNH; _gat_UA-162512367-1=1; _ga_3WP50LGEEC=GS1.1.1669660360.17.1.1669660390.30.0.0; _ga=GA1.1.1691793685.1667127501',
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
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-trace-id': '2242937d-a8b8-4696-97f2-dfd7758732fb',
    'x-ui-request-trace': '2242937d-a8b8-4696-97f2-dfd7758732fb',
}

response = requests.get('https://p2p.binance.com/bapi/fiat/v1/public/fiatpayment/menu/currency', cookies=cookies, headers=headers).text

word_with_fiat = ""
result_fiat = []

i_last_char = 0

search = True
while search == True:
    find_with_response = response.find('"name":"', i_last_char) + 8
    
    
    for i in range(5):
        if response[find_with_response + i] != ":":
            if response[find_with_response + i] != '"':
                word_with_fiat += response[find_with_response + i]
            else:
                result_fiat.append(word_with_fiat)
                word_with_fiat = ""
                i_last_char = find_with_response + i
                break
        else:
            result_fiat.pop(-1)
            search = False
            break
    
print(sorted(result_fiat))