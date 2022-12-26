import time
import os
import requests
import fake_useragent

os.system("mode con cols=96 lines=60")

"""Style"""
R = '\x1b[31m'
G = '\x1b[32m'
B = '\x1b[34m'
W = '\x1b[37m'
Y = '\x1b[33m'
M = '\x1b[35m'
C = '\x1b[36m'
Bl = '\x1b[39m'

S_b = '\x1b[1m'
S_n = '\x1b[22m'


class P2parser:
    def __init__(self):
        self.available_data = {
            "action": ["BUY", "SELL"],
            "fiat": self.__all_fiat(),
            "asset": None,
            "bank": None,
        }

        self.__result_exchange_rate = []

    def parsing_asset(self, fiat) -> list:
        data_asset = self.__list_with_data(
            'asset', self.available_data["action"], fiat)
        cookies = data_asset[0]
        headers = data_asset[1]
        json_data = data_asset[2]

        response = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/portal/config',
                                 cookies=cookies, headers=headers, json=json_data)

        data = response.json()

        result_list = []

        for item in data["data"]["areas"][0]['tradeSides'][0]["assets"]:
            result_list.append(item["asset"])

        self.available_data["asset"] = result_list

    def parsing_bank(self, fiat) -> None:
        data_bank = self.__list_with_data(
            'bank', self.available_data["action"], fiat)
        cookies = data_bank[0]
        headers = data_bank[1]
        json_data = data_bank[2]

        response = requests.post('https://p2p.binance.com/bapi/c2c/v2/public/c2c/adv/filter-conditions',
                                 cookies=cookies, headers=headers, json=json_data)

        data_json = response.json()

        banks = []

        for bank in data_json["data"]["tradeMethods"]:
            banks.append(bank["identifier"])

        self.available_data["bank"] = banks

    def parsing_price(self) -> None:

        data_price = self.__list_with_data(
            "all", self.available_data["action"], self.available_data["fiat"], self.available_data["asset"], self.available_data["bank"])
        cookies = data_price[0]
        headers = data_price[1]
        json_data = data_price[2]

        response = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
                                 cookies=cookies, headers=headers, json=json_data)

        response_json = response.json()["data"]

        for data in response_json:
            self.__result_exchange_rate.append([[data["adv"]["price"]], [
                                               data["adv"]["minSingleTransAmount"]], [data["adv"]["dynamicMaxSingleTransAmount"]]])

    def set_available_data(self, data, choice) -> None:
        """
        data  --> 'action', 'fiat', 'asset', 'bank'\n                 
        choice --> user selection    
        """
        for key in self.available_data:
            if key in data:
                self.available_data[key] = choice

    def get_available_data(self):
        return self.available_data

    def get_result_parsing(self) -> list:
        return self.__result_exchange_rate

    @classmethod
    def __all_fiat(self) -> list:
        data_fiat = self.__list_with_data('fiat')
        cookies = data_fiat[0]
        headers = data_fiat[1]

        response = requests.get(
            'https://p2p.binance.com/bapi/fiat/v1/public/fiatpayment/menu/currency', cookies=cookies, headers=headers)
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

        return result_fiat

    @classmethod
    def __list_with_data(cls, method, action="BUY", fiat="UAH", asset="USDT", bank="Monobank") -> list:
        """method --> 'action', 'fiat', 'asset', 'bank', 'all'"""

        cls.method = method

        cls.action = action
        cls.fiat = fiat
        cls.asset = asset
        cls.bank = bank

        cookies = {
            'common_fiat': cls.fiat,
        }

        headers = {
            'referer': 'https://p2p.binance.com/trade/' + cls.bank + '/' + cls.asset + '?fiat=' + cls.fiat,
            'user-agent': fake_useragent.UserAgent().random,
        }

        json_data = {
            'proMerchantAds': False,
            'page': 1,
            'rows': 10,
            'payTypes': [cls.bank, ],
            'countries': [],
            'publisherType': None,
            'asset': cls.asset,
            'fiat': cls.fiat,
            'tradeType': cls.action,
        }

        if cls.method == "fiat":
            return [cookies, headers]
        elif cls.method == "asset" or cls.method == "bank" or cls.method == "all":
            return [cookies, headers, json_data]
        else:
            raise ValueError(
                "write one with method ('action', 'fiat', 'asset', 'bank', 'all')")


def write_available_chouice(select, available_data) -> None:
    """
    write action(buy or sell)--> 'action'\n
    write fiat--> 'fiat'\n
    write asset--> 'asset'\n
    write bank--> 'bank'
    """

    if select == "action":
        print("_" * 96 + "\n")

        for i in range(len(available_data["action"])):
            if i == 0:
                print(f' {1}-{G + available_data["action"][i] + W}', end=" ")
            else:
                print(f' {2}-{R + available_data["action"][i] + W}', end=" ")

        print("\n")
    if select == "fiat":
        print("_" * 96 + "\n")

        for i in range(len(available_data["fiat"])):
            if i < 7:
                print(f' {i+1}-{G + available_data["fiat"][i] + W}', end="  ")
                if i == 6:
                    print("\n" + (S_n + Bl) + "_" * 96)
            else:
                print(
                    f'{S_n + Bl}{i+1}-{G + available_data["fiat"][i]}', end=" ")

        print("\n" + (W + S_b))
    if select == "asset":
        print("_" * 96 + "\n")

        for i in range(len(available_data["asset"])):
            print(f' {i+1}-{G + available_data["asset"][i] + W}', end=" ")

        print("\n")
    if select == "bank":
        print("_" * 96 + "\n")
        G_2 = G  # Style for change colors

        index1 = 0
        index2 = 1

        count_indent = 45

        for i in range(len(available_data["bank"])):

            number_of_spaces = (
                count_indent - len(available_data['bank'][index1]))

            print(
                f'{G_2} {W}{index1+1}-{G_2 + available_data["bank"][index1] + W}', end=(" " * number_of_spaces))
            print(
                f'{G_2} {W}{index2+1}-{G_2 + available_data["bank"][index2] + W}')

            index1 += 2
            index2 += 2

            if index1 == 10 or index1 == 100 or index1 == 1000:
                G_2 = G_2 + S_n  # style change after 10

                print(f'{Y}{S_b}{"-" * 96}')
                quation = input(
                    f'{G}\n 00{W}-{S_n}More banks\t\n\n {S_b}{G}>>> {W}')
                if quation != "00":
                    return int(quation) - 1
                else:
                    print(f'{S_b}{G}\n\nLoading...\n{W}')
                    time.sleep(1)

                count_indent -= 1

            if index2 >= len(available_data['bank']):
                break

        print("\n", S_b)


def user_сhoice(available_data) -> None:
    # action
    while True:
        print(S_b)

        write_available_chouice("action", available_data)
        try:
            select_action = int(input(" Select an action: ")) - 1
            if select_action <= len(available_data['action'])-1 and select_action >= 0:
                break
            else:
                print(f'{R} ERORR{W}')
                time.sleep(0.70)
        except:
            print(f'{R} ERORR{W}')
            time.sleep(0.70)

    parsing.set_available_data(
        "action", available_data["action"][select_action])

    # fiat
    while True:
        write_available_chouice("fiat", available_data)
        try:
            select_fiat = int(input(" Select the fiat to be parsed: ")) - 1
            if select_fiat <= len(available_data["fiat"])-1 and select_fiat >= 0:
                break
            else:
                print(f'{R} ERORR{W}')
                time.sleep(0.70)
        except:
            print(f'{R} ERORR{W}')
            time.sleep(0.70)

    parsing.parsing_asset(available_data["fiat"][select_fiat])
    parsing.parsing_bank(available_data["fiat"][select_fiat])

    parsing.set_available_data("fiat", available_data["fiat"][select_fiat])

    # asset
    while True:
        write_available_chouice("asset", available_data)
        try:
            select_asset = int(input(" Select the asset to be parsed: ")) - 1
            if select_asset <= len(available_data["asset"])-1 and select_asset >= 0:
                break
            else:
                print(f'{R} ERORR{W}')
                time.sleep(0.70)
        except:
            print(f'{R} ERORR{W}')
            time.sleep(0.70)

    parsing.set_available_data("asset", available_data["asset"][select_asset])

    # bank
    while True:
        for_check_on_digit = write_available_chouice("bank", available_data)
        try:
            if for_check_on_digit == None:
                select_bank = int(input(" Select the bank to be parsed: ")) - 1
                if select_bank <= len(available_data["bank"])-1 and select_bank >= 0:
                    break
                else:
                    print(f'{R} ERORR{W}')
                    time.sleep(0.70)
            else:
                select_bank = for_check_on_digit
                if select_bank <= len(available_data["bank"])-1 and select_bank >= 0:
                    break
                else:
                    print(f'{R} ERORR{W}')
                    time.sleep(0.70)
        except:
            print(f'{R} ERORR{W}')
            time.sleep(0.70)

    parsing.set_available_data("bank", available_data["bank"][select_bank])


def print_offers(list_with_result, list_with_data) -> None:

    os.system('cls||clear')
    print(f"{G}{S_b}\n\n  Loading...{W}\n\n")
    time.sleep(0.80)
    os.system('cls||clear')

    action = list_with_data["action"]
    fiat = list_with_data["fiat"]
    asset = list_with_data["asset"]
    bank = list_with_data["bank"]

    os.system('cls||clear')

    if len(list_with_result) == 0:
        print(f'{R}\n\tNO ORDERS{W}')
        return

    print(M + "\n" + "_" * 96 + "\n\n" + W)

    for i in range(len(list_with_result)):
        if action == "BUY":
            if i + 1 == 10:
                print(
                    f' {S_n}{i + 1}){S_b}{G + action + W} Offer({S_n}{Y}{bank}{S_b}{W}): {C}1-{asset + W} = {M}{", ".join(map(str, list_with_result[i][0]))} {G + fiat + W} {B}\t|{S_n + W} {", ".join(map(str, list_with_result[i][1]))} - {Y + ", ".join(map(str, list_with_result[i][2])) + W} {G + fiat + W + S_b}')
            else:
                print(
                    f' {S_n}{i + 1}){S_b} {G + action + W} Offer({S_n}{Y}{bank}{S_b}{W}): {C}1-{asset + W} = {M}{", ".join(map(str, list_with_result[i][0]))} {G + fiat + W} {B}\t|{S_n + W} {", ".join(map(str, list_with_result[i][1]))} - {Y + ", ".join(map(str, list_with_result[i][2])) + W} {G + fiat + W + S_b}')
        else:
            if i + 1 == 10:
                print(
                    f' {S_n}{i + 1}){S_b}{R + action + W} Offer({S_n}{Y}{bank}{S_b}{W}): {C}1-{asset + W} = {M}{", ".join(map(str, list_with_result[i][0]))} {G + fiat + W} {B}\t|{S_n + W} {", ".join(map(str, list_with_result[i][1]))} - {Y + ", ".join(map(str, list_with_result[i][2])) + W} {G + fiat + W + S_b}')
            else:
                print(
                    f' {S_n}{i + 1}){S_b} {R + action + W} Offer({S_n}{Y}{bank}{S_b}{W}): {C}1-{asset + W} = {M}{", ".join(map(str, list_with_result[i][0]))} {G + fiat + W} {B}\t|{S_n + W} {", ".join(map(str, list_with_result[i][1]))} - {Y + ", ".join(map(str, list_with_result[i][2])) + W} {G + fiat + W + S_b}')

    print(M + "\n" + "_" * 96 + W)


if __name__ == "__main__":

    cycle_menu = True
    while cycle_menu == True:
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

        parsing = P2parser()

        user_сhoice(parsing.get_available_data())

        parsing.parsing_price()

        print_offers(parsing.get_result_parsing(),
                     parsing.get_available_data())

        input(f'\n\n{R}  EXIT IN MENU {Bl}(type any key){W}')
