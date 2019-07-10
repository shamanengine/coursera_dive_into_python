from bs4 import BeautifulSoup
from decimal import Decimal
#
import requests
import lxml


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(
        f"http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}")  # Использовать переданный requests
    # ...
    soup = BeautifulSoup(response.content, 'xml')
    # print(soup.prettify())

    # Nominal ед. валюты = Value рублей.
    if cur_from == cur_to:
        return Decimal(amount).quantize(Decimal('.0001'))
    elif cur_from == 'RUR':
        cur_to_value = soup.find('CharCode', text=cur_to).find_next_sibling('Value').string.replace(',', '.')
        cur_to_nominal = soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string
        return (Decimal(amount) * Decimal(cur_to_nominal) / Decimal(cur_to_value)).quantize(Decimal('.0001'))
    elif cur_to == 'RUR':
        cur_from_value = soup.find('CharCode', text=cur_from).find_next_sibling('Value').string.replace(',', '.')
        cur_from_nominal = soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string
        return (Decimal(amount) * Decimal(cur_from_value) / Decimal(cur_from_nominal)).quantize(Decimal('.0001'))
    else:
        cur_from_value = soup.find('CharCode', text=cur_from).find_next_sibling('Value').string.replace(',', '.')
        cur_from_nominal = soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string
        cur_to_value = soup.find('CharCode', text=cur_to).find_next_sibling('Value').string.replace(',', '.')
        cur_to_nominal = soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string
        return (Decimal(amount)
                * Decimal(cur_from_value) / Decimal(cur_from_nominal)
                * Decimal(cur_to_nominal) / Decimal(cur_to_value)).quantize(Decimal('.0001'))

    # 100 en = 2 rybla
    # 5 usd = 3 ryblya
    # 7 en = x usd

    # print(cur_from_value)
    # print(cur_from_value)
    #
    # result = Decimal('3754.8057')
    # result = Decimal('7.325').quantize(Decimal('.0001'))
    #
    # return result  # не забыть про округление до 4х знаков после запятой


if __name__ == '__main__':
    print(convert(Decimal("1.001"), 'USD', 'UAH', "17/02/2019", requests))
    # print(convert(Decimal("1000.1000"), 'RUR', 'JPY', "17/02/2005", requests))
    # print(convert(Decimal("1.001"), 'RUR', 'RUR', "17/02/2019", requests))
