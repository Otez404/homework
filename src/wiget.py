import datetime as dt
import re


from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(card_number: str) -> str:
    """Функция маскировки как банковского счета, так и номера карты"""
    only_numbers = re.findall(r'\d+', card_number)
    str_only_numbers = ''.join(only_numbers)
    name_card = ' '.join([num for num in card_number.split() if num.isalpha()])
    if 'Счет' in card_number:
        return f"{name_card} {get_mask_account(str_only_numbers)}"
    else:
        return f"{name_card} {get_mask_card_number(str_only_numbers)}"


def get_date(date_format: str) -> str:
    """Функция изменения формата даты"""
    date_object = dt.datetime.strptime(date_format[0:10], '%Y-%m-%d')
    date_class_str = date_object.strftime('%d.%m.%Y')
    return date_class_str
